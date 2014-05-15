'''
Kayla Robinson
5/14/2014
DPW
Encapsulated
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

#Rental property class object
class Rental(object):
    def __init__(self):
        #attributes
        self.location = ""
        self.mortgage_amount = 0
        self.rent = 0
        self.monthly_profit = 0
        self.annual_profit = 0

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
