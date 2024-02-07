class String:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("string: ")

    def printString(self):
        print("uppercase: ", self.input_string.upper())


string = String()
string.getString()
string.printString()
