def find_data(search_data):
    with open('dictionary.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines
