#create one class the class consisting of 3 variables with intitialization we have to take two methods the first method is a 2 argumented function first one is string type of argument and second one is integer inside of the method the string reverse value is print i have to print square of integer argument value with a  string varaible
#second method consists of method name is display results inside of the method length of the string and print modulo division of two integer variables and pass the values
#at run time.

class shi:
    x = input("enter a string = ")
    y = int(input("enter any integer = "))
    z = int(input("enter any integer = "))

    def sri(self, a, b):
        # a string ,b int
        print("reverse of given string = ", a[::-1])
        print("the square of a given 1st int = ", b * b)

    def display_results(self, x, y, z):
        print("the len of the string = ", len(x))
        print("mod of the 1st int and 2nd int = ", y % z)


obj = s()
obj.sri(obj.x, obj.y)
obj.display_results(obj.x, obj.y, obj.z)