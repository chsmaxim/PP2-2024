def num_of_lines(file_path):
 with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)
    print(f"number of lines in the file is {line_count}")


text_file_path = "../dir-and-files/test.txt"
num_of_lines(text_file_path)
