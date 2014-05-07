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


#Getting user inputs



#Getting first number from user and adding them to numbers array

response = raw_input("Enter a number. This number should be greater than 10. ")
numbers.append(response)
#print numbers[0]


#Updating strings dict with user input for Room

response = raw_input("Enter a room in your house. (living room, office, guest room) ")
strings["Room"]= response
#print strings["Room"]


#Updating strings dict with user input for My object

response = raw_input("Enter an object that can be found in this room. ")
strings["My object"]= response
#print strings["My object"]


#Updating strings dict with user input for Adj man

response = raw_input("Enter an adjective. (mean, funny, aggressive) ")
strings["Adj man"]= response
#print strings["Adj man"]


#Updating strings dict with user input for Man object

response = raw_input("Enter a random object. (shoe, car, bat) ")
strings["Man object"]= response
#print strings["Man object"]


#Updating strings dict with user input for Adj woman

response = raw_input("Enter another adjective. (mean, funny, aggressive) ")
strings["Adj woman"]= response
#print strings["Adj woman"]


#Getting second number (float) from user and adding them to numbers array

response = raw_input("Enter a decimal number. (35.6, 9.8, 1.2) ")
numbers.append(response)
#print numbers[1]


#Updating strings dict with user input for Gender

response = raw_input("Are you a man or a woman. ")
strings["Gender"]= response
#print strings["Gender"]


#Updating strings dict with user input for Adj user

response = raw_input("Enter an adjective that describes you. ")
strings["Adj user"]= response
#print strings["Adj user"]


#Updating strings dict with user input for Neighbor

response = raw_input("Enter a person you have a close relationship with. (friend, mom, sister) ")
strings["Neighbor"]= response
#print strings["Neighbor"]


#Getting a number from user and adding them to numbers array

response = raw_input("Enter any number. (22, 58, 2) ")
numbers.append(response)
#print numbers[2]


#Getting a number from user and adding them to numbers array

response = raw_input("Enter one more number. (22, 58, 2) ")
numbers.append(response)
#print numbers[3]

#Creating story

#Functions

#Math problem function

def calcVol(a, b, c):
    volume = a * b * c
    return volume

#Room size function

def calcSize(x,y):
    measure = x * y

    if measure>200:
        size = "large"
        return size
    else:
        size = "small"
        return size

#Calling math function

v1 = 2
v2 = 3
v3 = 4

v = calcVol(v1, v2, v3);

#Calculating new volume

vol2 = v /2

#Calling size function
x = 9
y = 10

s = calcSize(x,y)

#Locals
num1 = numbers[0]
room = strings["Room"]
man = strings["Adj man"]
vol = v
object1 = strings["My object"]
object2 = strings["Man object"]
woman = strings["Adj woman"]
num2 = numbers[1]
user = strings["Adj user"]
gender = strings["Gender"]
room_size = s
person = strings["Neighbor"]
num3 = numbers[2]
minutes = int(numbers[0])/2
items = 9
years = int(numbers[0])-8

#Print message
message = '''
The Last Nap

About {num1} years ago on a lazy Saturday I decided to take a nap in my {room}.
I tried to do a math problem in my head. I always hated math, so that should have put me to sleep in no time.
So if I have a box and its sides measure {v1}, {v2} and {v3}, the volume would be {v1} * {v2} * {v3}, which is {vol}.
 If I cut that box in have the new volume would be {vol2}. That did not work so I began counting sheep to lull my self to sleep.
'''
message = message.format(**locals())
print message

#  While loop for counting sheep
i = 1
ii = 5
while i<ii:
    if i<ii-1:
        print i, "sheep"
        i += 1
    else:
        print i, "sheep..."
        i += 1

message = '''
This was not your normal nap. You see just as I had fallen a sleep a(n) {man} man broke down my front door
and awoke me. He ran into the {room} and began yelling at me, "I want that {object1}". I then told him,
"You are not taking my {object1}," which was a bad idea because then he pulled out a(n) {object2} and threatened
me with it. Just then a {woman} woman came barging into the {room} and said to the man, "You have {num2}
seconds to hand over my {object2}." The {man} man refused and the two began fighting over the {object2}.
The {object2} flew in my direction and I had no choice but to try and catch it to prevent getting hurt.
That was when the {woman} woman noticed me and yelled to the man, "Are you seriously going to rob this
{user} {gender}." I knew this was my only opportunity to make a run for it. It was a {room_size} room so you
can imagine how long it took to get to the other side of the room. I quietly made it to the other side and climbed out
of the window. I was too scared to run fearing I might be spotted, so I crawled all the way to my {person}'s house {num3}
blocks away. Once safely inside I called 911 to report this crazy incident. Can you believe that it took
{minutes} minutes for the cops to get there. After they had sorted the situation out, both the man and the woman had
gotten away and one of them had taken {items} item(s) from my house. That was the last time I napped during the day.
And it's only been {years} years since I could rest peacefully at night.
'''
message = message.format(**locals())
print message