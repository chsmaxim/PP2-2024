def copy(source_path, destination_path):
        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)



if __name__ == "__main__":
    source_file_path = "../dir-and-files/test.txt"
    destination_file_path = "../dir-and-files/6-txt/A.txt"

    copy(source_file_path, destination_file_path)
