def reader():
    with open('dictionary.txt', 'r') as file:
        for item in file:
            print(item)