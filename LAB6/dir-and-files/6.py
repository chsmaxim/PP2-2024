import string
import os

def generate_txt(output_path):
    for letter in string.ascii_uppercase:
        file_name = os.path.join(output_path, f"{letter}.txt")
        with open(file_name, 'w') as file:
            file.write(f"Content for file {letter}.txt\n")


if __name__ == "__main__":
    specified_path = "../dir-and-files/6-txt/"
    generate_txt(specified_path)
