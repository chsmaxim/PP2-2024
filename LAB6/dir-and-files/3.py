import os

def analyze_path(input_path):
    if os.path.exists(input_path):
        print(f"The path '{input_path}' exists.")

        filename = os.path.basename(input_path)
        directory = os.path.dirname(input_path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{input_path}' does not exist.")


given_path = "../built-in-functions/"
analyze_path(given_path)
