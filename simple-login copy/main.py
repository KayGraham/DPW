'''
Kayla Robinson
5/6/2014
DPW
Setting up the Launcher
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #fuctuin that starts everything  Catalyst
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()
        #code goes here

    def additional_functions(self):
        pass
        #code goes here
class Button(object):
    def __init__(self):
        self.label = "" #public attribute
        self.__size = 60 #priavate attribute - two underscores
        self._color = "0x00000" #protected attribute - one underscore
        #self.on_roll_over("Hello!!")


    def click(self):
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button" + message

    def show_label(self):
        print "My label is " + self.label

#never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
