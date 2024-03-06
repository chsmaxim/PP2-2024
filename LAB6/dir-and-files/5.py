def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

list_to_write = ["1", "11", "111", "1111"]
output_file_path = "test.txt"

write_list_to_file(output_file_path, list_to_write)
