try:
    file1 = open('sample.txt','r')
    reading_file = file1.read()
    print('Reading file contain :')
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("Error : The file 'sample.txt' not found")
