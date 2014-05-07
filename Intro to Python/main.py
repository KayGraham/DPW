#print "hello world!"

#one lined comments
'''
Doc strings- explain what functions do
http://legacy.python.org/devs/peps/pep-0008/

'''
first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter your name  ")
#print "Hello there, ", response

birth_year = 1966
current_year = 2014
age = current_year -birth_year
#print "You are "+ str(age) + " years old."

#int(var)

'''
if(condition){

    //stuff to do
}

if condition:
    stuff to do
'''
budget = 90

if budget > 100:
    brand = "nike"
    print "Yay! we can by cool " + brand + " shoes!"
elif budget > 50:
    #print "We can at least get some generic sneakers."
    pass
else:
    #print "No cool shoes for me."
    pass

'''
*Empty else

else:
    pass
'''

characters =  ["leia","luke","chewy","lando"]


#add to array
characters.append("obi won")
#print characters
#print characters[0]

movies = dict() #create dictionay object
movies = {"Star Wars":"Darth Vader","Silence of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]

#Loops

#While Loop
'''
i = 0
while i<9:
    print "The count is", i
    i += 1
'''

'''
#For loop
for i in range(0,10):
    print "The count is", i
    i += 1
'''


#"For Each" Loop
rappers = ["Tupac","Nas","Biggie Smalls"]
for r in rappers:
    #print "One of the best rappers is " + r
    pass

#Functions

x = 2

def calcArea(h, w):
    area = h * w
    return area + x

a = calcArea(20, 40);
#print "My area is " + str(a) + "sqft."

'''
weight = 200
height = 63
message = '''
#Your height is {height} and your weight is {weight}.
'''

message = message.format(**locals())
print message
'''
title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
message = message.format(**locals())
print message