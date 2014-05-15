'''
Kayla Robinson
5/14/2014
DPW
Encapsulated
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Option 1 Object
        option1 = Rental()
        option1.name = "Rental Property 1"
        option1.mortgage_amount = 30000
        option1.rent = 300
        option1.calc_monthly_profit()
        option1.calc_annual_profit()
        self.response.write("monthly profit $" + str(option1.monthly_profit))
        self.response.write("annual profit $" + str(option1.annual_profit))

        #Option 2 Object
        option2 = Rental()
        option2.name = "Rental Property 2"
        option2.mortgage_amount = 60000
        option2.rent = 400
        option2.calc_monthly_profit()
        option2.calc_annual_profit()
        self.response.write("monthly profit $" + str(option2.monthly_profit))
        self.response.write("annual profit $" + str(option2.annual_profit))

class Page(object):
    def __init__(self):
        self.__open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Rental Property Profit Calculator</title>
    </head>
    <body>
    '''

        self.__content = ''
        self.__close = '''
    </body>
</html>'''

#Rental property class object
class Rental(object):
    def __init__(self):
        #attributes
        self.name = ""
        self.mortgage_amount = 0
        self.rent = 0
        self.__monthly_profit = 0
        self.__annual_profit = 0

    #Calculate Monthly Profit
    @property
    def monthly_profit(self):
        return self.__monthly_profit

    @monthly_profit.setter
    def monthly_profit(self, new_monthly_profit):
        self.__monthly_profit = new_monthly_profit

    def calc_monthly_profit(self):
        #calculate monthly profit
        self.__monthly_profit = (self.rent - ((self.mortgage_amount / 10))/12)

    #Calculate Annual Profit
    @property
    def annual_profit(self):
        return self.__annual_profit

    @annual_profit.setter
    def annual_profit(self, new_annual_profit):
        self.__annual_profit = new_annual_profit

    def calc_annual_profit(self):
        #calculate annual profit
        self.__annual_profit = (self.monthly_profit * 12)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
