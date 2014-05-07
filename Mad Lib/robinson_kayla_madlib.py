'''
Kayla Robinson
5/7/2014
DPW
Mad Lib
'''


#List/array to hold all number input by user

numbers = []


#Dictonary that will hold strings input by user

strings = dict()
strings = {"Room":"","Adj man":"","My object":"","Man object":"","Adj woman":"","Gender":"","Adj user":"","Neighbor":""}


#Var to hold the number of sheep to count

sheep = 3


#Getting user inputs



#Getting first number from user and adding them to numbers array

response = raw_input("Enter a number. This number should be greater than 10.")
numbers.append(response)
#print numbers[0]


#Updating strings dict with user input for Room

response = raw_input("Enter a room in your house. (living room, office, guest room)")
strings["Room"]= response
#print strings["Room"]


#Updating strings dict with user input for My object

response = raw_input("Enter an object that can be found in this room.")
strings["My object"]= response
#print strings["My object"]


#Updating strings dict with user input for Adj man

response = raw_input("Enter an adjective. (mean, funny, aggressive)")
strings["Adj man"]= response
#print strings["Adj man"]


#Updating strings dict with user input for Man object

response = raw_input("Enter a random object. (shoe, car, bat)")
strings["Man object"]= response
#print strings["Man object"]


#Updating strings dict with user input for Adj woman

response = raw_input("Enter another adjective. (mean, funny, aggressive)")
strings["Adj woman"]= response
#print strings["Adj woman"]


