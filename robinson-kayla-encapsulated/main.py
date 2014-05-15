'''
Kayla Robinson
5/14/2014
DPW
Encapsulated
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        option1 = Rental()
        option1.name = "Rental Property 1"
        option1.mortgage_amount = 30000
        option1.rent = 400
        option1.calc_monthly_profit()
        #option1.calc_annual_profit()
        self.reponse.write("monthly profit" + str(option1.monthly_profit))

#Rental property class object
class Rental(object):
    def __init__(self):
        #attributes
        self.name = ""
        self.mortgage_amount = 0
        self.rent = 0
        self.__monthly_profit = 0
        self.__annual_profit = 0

    @property
    def monthly_profit(self):
        return self.__monthly_profit

    @monthly_profit.setter
    def monthly_profit(self, new_monthly_profit):
        self.__monthly_profit = new_monthly_profit

    def calc_monthly_profit(self):
        #calculate monthly profit
        self.__monthly_profit = ((self.mortgage_amount / 12) - self.rent)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
