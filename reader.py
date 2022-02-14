def reader():
    data = open('dictionary.txt', 'r') 
    print(data.read())
    
    data.close()

reader()
