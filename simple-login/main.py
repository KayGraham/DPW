'''
Kayla Robinson
5/6/2014
DPW
Setting up the Launcher
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #fuctuin that starts everything  Catalyst
        self.response.write('Hello world!')
        #code goes here

    def additional_functions(self):
        pass
        #code goes here

#never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
