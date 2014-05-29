'''
Kayla Robinson
5/27/2014
API
'''
import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['category', 'text', 'category'],['city', 'text', 'locality'],['state', 'text', 'region'],['Submit', 'submit']]

        if self.request.GET:
            #Create Venue Model
            vm = VenueModel()

            #Sends category from url to the model
            vm.category = self.request.GET['category']
            #Sends city from url to the model
            vm.category = self.request.GET['locality']
            #Sends state from url to the model
            vm.category = self.request.GET['region']

            #Connect to API
            vm.callApi()

            #Create view
            vv = VenueView()

            #Take data from model and sends to view
            vv.vdos = vm.dos

            p._body = vv.content

            self.response.write(p.print_out())

class VenueView(object):
    '''Handles how user is shown data'''
    def __init__(self):
        self.__vdos = []
        self.__content = '<br />'

    def update(self):
        for do in self.__vdos:
            self.__content += do.name + "Address: " + do.locality + "<br />" + do.region + "<br />"

    @property
    def content(self):
        return self.__content

    @property
    def vdos(self):
        pass

    @vdos.setter
    def vdos(self, arr):
        self.__vdos = arr
        self.update()
        


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
