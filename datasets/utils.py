def read_file_contents_list(file_name):
    print(f'Reading from file list txt {file_name}')
    with open(file_name) as file:
        lines = [line.rstrip('\n') for line in file]
        return lines