import psycopg2
from configparser import ConfigParser
import csv

# Function to load database configuration from 'database.ini'
def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # Get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return config

# Function to connect to the PostgreSQL database
def connect(config):
    try:
        # Connecting to the PostgreSQL server
        conn = psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)
        return None

# Function to create 'contacts' table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                contact_id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255),
                phone_number VARCHAR(20) NOT NULL
            )
        """)
        conn.commit()
        print("Table 'contacts' created successfully!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error creating table:", e)

# Function to insert data into 'contacts' table from CSV file
def insert_from_csv(conn, filename):
    try:
        cursor = conn.cursor()
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)  # Skip header row
            for row in csvreader:
                first_name, last_name, phone_number = row
                cursor.execute("""
                    INSERT INTO contacts (first_name, last_name, phone_number)
                    VALUES (%s, %s, %s)
                """, (first_name, last_name, phone_number))
        conn.commit()
        print("Data inserted from CSV successfully!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data from CSV:", e)

# Function to insert data into 'contacts' table from console input
def insert_from_console(conn):
    try:
        cursor = conn.cursor()
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        cursor.execute("""
            INSERT INTO contacts (first_name, last_name, phone_number)
            VALUES (%s, %s, %s)
        """, (first_name, last_name, phone_number))
        conn.commit()
        print("Data inserted from console successfully!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data from console:", e)

# Function to update data in 'contacts' table
def update_contact(conn):
    try:
        cursor = conn.cursor()
        contact_id = input("Enter contact ID to update: ")
        first_name = input("Enter new first name (leave blank to keep current): ")
        last_name = input("Enter new last name (leave blank to keep current): ")
        phone_number = input("Enter new phone number (leave blank to keep current): ")

        update_query = "UPDATE contacts SET"
        update_fields = []

        if first_name:
            update_fields.append(f"first_name = '{first_name}'")
        if last_name:
            update_fields.append(f"last_name = '{last_name}'")
        if phone_number:
            update_fields.append(f"phone_number = '{phone_number}'")

        if update_fields:
            update_query += " " + ", ".join(update_fields)
            update_query += f" WHERE contact_id = {contact_id}"
            cursor.execute(update_query)
            conn.commit()
            print("Contact updated successfully!")
        else:
            print("No fields to update specified.")

    except psycopg2.Error as e:
        conn.rollback()
        print("Error updating contact:", e)

# Function to query data from 'contacts' table with filters
def query_contacts(conn):
    try:
        cursor = conn.cursor()
        print("Query contacts:")
        first_name = input("Enter first name (leave blank if not needed): ").strip()
        last_name = input("Enter last name (leave blank if not needed): ").strip()

        query = "SELECT * FROM contacts WHERE TRUE"

        if first_name:
            query += f" AND first_name = '{first_name}'"
        if last_name:
            query += f" AND last_name = '{last_name}'"

        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            print("Matching contacts:")
            for row in rows:
                print(row)
        else:
            print("No matching contacts found.")

    except psycopg2.Error as e:
        print("Error querying contacts:", e)

# Function to delete data from 'contacts' table
def delete_contact(conn):
    try:
        cursor = conn.cursor()
        print("Delete contacts:")
        print("1. Delete a specific contact by phone number")
        print("2. Delete all contacts")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            phone_number = input("Enter phone number of the contact to delete: ").strip()
            cursor.execute("DELETE FROM contacts WHERE phone_number = %s", (phone_number,))
            conn.commit()
            print("Contact deleted successfully!")

        elif choice == '2':
            confirm = input("Are you sure you want to delete all contacts? (yes/no): ").strip().lower()
            if confirm == 'yes':
                cursor.execute("DELETE FROM contacts")
                conn.commit()
                print("All contacts deleted successfully!")
            else:
                print("Deletion canceled.")

        else:
            print("Invalid choice. Please enter either 1 or 2.")

    except psycopg2.Error as e:
        conn.rollback()
        print("Error deleting contacts:", e)

if __name__ == '__main__':
    try:
        # Load database configuration from 'database.ini'
        config = load_config()

        # Connect to PostgreSQL
        conn = connect(config)

        if conn is not None:
            # Create 'contacts' table if it doesn't exist
            create_table(conn)

            try:
                while True:
                    print("\nChoose an option:")
                    print("1. Insert data (from console or CSV)")
                    print("2. Update contact information")
                    print("3. Query contacts")
                    print("4. Delete contacts")
                    print("5. Exit")

                    choice = input("Enter your choice (1-5): ").strip()

                    if choice == '1':
                        insert_option = input("Add from terminal (T) or CSV file (C)? ").strip().lower()
                        if insert_option == 't':
                            insert_from_console(conn)
                        elif insert_option == 'c':
                            csv_file = input("Enter CSV filename: ").strip()
                            insert_from_csv(conn, csv_file)
                        else:
                            print("Invalid option. Please try again.")

                    elif choice == '2':
                        update_contact(conn)

                    elif choice == '3':
                        query_contacts(conn)

                    elif choice == '4':
                        delete_contact(conn)

                    elif choice == '5':
                        print("Exiting...")
                        break

                    else:
                        print("Invalid choice. Please enter a valid option (1-5).")

            finally:
                # Reset contact_id sequence
                cursor = conn.cursor()
                cursor.execute("ALTER SEQUENCE contacts_contact_id_seq RESTART WITH 1")
                conn.commit()
                print("Contact_id sequence reset successfully.")

                # Close the database connection
                conn.close()
                print("Connection closed.")

    except Exception as e:
        print("An error occurred:", e)
