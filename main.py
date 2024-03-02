
try:
    with open('/home/fozil/test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
