import pygame
import random
import psycopg2

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
CELL = 20


db_params = {
    'host': 'localhost',
    'database': 'snake',
    'user': 'postgres',
    'password': '1234'
}


try:
    conn = psycopg2.connect(**db_params)
    print('Connected to the PostgreSQL database server.')
except psycopg2.Error as e:
    print("Unable to connect to the database:", e)
    quit()


def create_tables():
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(255) UNIQUE NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS user_scores (
                        user_id INT PRIMARY KEY,
                        level INT DEFAULT 1,
                        score INT DEFAULT 0,
                        CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id)
                    );
                """)
                print("Database tables created successfully.")
    except psycopg2.Error as e:
        print("Error creating database tables:", e)

create_tables()


def get_user(username):
    """Retrieve user details from the database."""
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT user_id, username FROM users WHERE username = %s", (username,))
                return cursor.fetchone()
    except psycopg2.Error as e:
        print("Error fetching user:", e)
        return None

def create_user(username):
    """Create a new user and initialize their score."""
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
                user_id = cursor.fetchone()[0]
                cursor.execute("INSERT INTO user_scores (user_id) VALUES (%s)", (user_id,))
                return user_id
    except psycopg2.Error as e:
        print("Error creating user:", e)
        return None

def load_user_score(user_id):
    """Load user's score and level."""
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT level, score FROM user_scores WHERE user_id = %s", (user_id,))
                return cursor.fetchone()
    except psycopg2.Error as e:
        print("Error loading user score:", e)
        return (1, 0)  # Default level 1, score 0

# Snake class
class Snake:
    def __init__(self):
        self.body = [pygame.Vector2(10, 10), pygame.Vector2(9, 10), pygame.Vector2(8, 10)]
        self.direction = pygame.Vector2(1, 0) 
        self.score = 0
        self.level = 1  # Initial

    def update(self):
    
        new_head = self.body[0] + self.direction
        self.body.insert(0, new_head)
        self.body.pop()


        if not (0 <= self.body[0].x < WIDTH / CELL and 0 <= self.body[0].y < HEIGHT / CELL):
            # Snake hits the window boundary, game over
            print("Game Over")
            # Update user score and level in the database
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("UPDATE user_scores SET level = %s, score = %s WHERE user_id = %s",
                                   (self.level, self.score, self.user_id))
                    print("User score updated in the database")
            # Reset score and level for the next game
            self.score = 0
            self.level = 1
            return False
        return True

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def grow(self):
        
        tail = self.body[-1]
        self.body.append(tail)


class Food:
    def __init__(self):
        self.position = pygame.Vector2(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position.x * CELL, self.position.y * CELL, CELL, CELL))

# Game initialization
def initialize_game():
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    return screen, clock, font


def draw_grid(screen):
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            colors = [(255, 255, 255), (200, 200, 200)]
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

def main():
    screen, clock, font = initialize_game()

    username = input("Enter your username: ")
    user_details = get_user(username)

    if not user_details:
        print("Creating new user...")
        user_id = create_user(username)
    else:
        print("Welcome back", username)
        user_id = user_details[0]

    
    level, score = load_user_score(user_id)

    snake = Snake()
    snake.user_id = user_id 
    snake.score = score 
    snake.level = level  
    food = Food()

    # Game loop
    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear the screen

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Save game state to database
                    with conn:
                        with conn.cursor() as cursor:
                            cursor.execute("UPDATE user_scores SET level = %s, score = %s WHERE user_id = %s",
                                           (snake.level, snake.score, user_id))
                            print("Game saved")

                if event.key == pygame.K_RIGHT and snake.direction.x != -1:
                    snake.direction = pygame.Vector2(1, 0)
                elif event.key == pygame.K_LEFT and snake.direction.x != 1:
                    snake.direction = pygame.Vector2(-1, 0)
                elif event.key == pygame.K_DOWN and snake.direction.y != -1:
                    snake.direction = pygame.Vector2(0, 1)
                elif event.key == pygame.K_UP and snake.direction.y != 1:
                    snake.direction = pygame.Vector2(0, -1)

        if not snake.update():
            running = False

        # Check for collision with food
        if snake.body[0] == food.position:
            snake.grow()
            snake.score += 10
            if snake.score >= 100:
                # Increase level after reaching 100 score
                snake.level += 1
                snake.score = 0  # Reset score for the next level
                print(f"Level up! You are now on Level {snake.level}")
            food.position = pygame.Vector2(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

        # Draw game elements
        draw_grid(screen)
        snake.draw(screen)
        food.draw(screen)

        # Display score and level
        score_text = font.render(f"Score: {snake.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        level_text = font.render(f"Level: {snake.level}", True, (0, 0, 0))
        screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

        pygame.display.flip()
        clock.tick(5) 

    pygame.quit()

if __name__ == '__main__':
    main()
