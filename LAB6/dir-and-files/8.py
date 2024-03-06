import os
import time

def delete_file(file_path):
        if os.path.exists(file_path):
            if os.access(file_path, os.W_OK):
                print("file exists")
                print("file is accessable")
                print("file will be deleted after 5 second")
                time.sleep(5)
                os.remove(file_path)
                print(f"file '{file_path}' deleted")
            else:
                print(f"no write access to '{file_path}'")
        else:
            print(f"file '{file_path}' does not exist")


if __name__ == "__main__":
    file_to_delete = "delete_example.txt"

    delete_file(file_to_delete)
