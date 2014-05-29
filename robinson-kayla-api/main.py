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

class VenueModel(object):
    def __init__(self):
        self.__url = "https://api.locu.com/v1_0/venue/search/?"
        self.__category = ''
        self.__locality = ''
        self.__region = ''

    def callApi(self):
        json_obj = urllib2.urlopen(self.__url + self.__category + '&' + self.__locality + '&' + self.__region)
        data = json.load((json_obj))

        self._dos = []

        for item in data['objects']:
            do = VenueData()
            do.name = item['name']
            do.locality = item['locality']
            do.address = item['street_address']
            do.state = item['region']
            do.zip = item['postal_code']
            do.phone = item['phone']
            do.cat = item['categories']
            do.url = item['website_url']
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def category(self):
        pass

    @category.setter
    def category(self, c):
        self.__category = c

    @property
    def locality(self):
        pass

    @locality.setter
    def locality(self, l):
        self.__locality = l

    @property
    def region(self):
        pass

    @region.setter
    def region(self, r):
        self.__region = r

class VenueData(object):
    '''Holds data from model and shown in view'''
    def __init__(self):
        self.name = ''
        self.locality = ''
        self.address = ''
        self.state = ''
        self.state = ''
        self.zip = ''
        self.phone = ''
        self.cat = ''
        self.url = ''

class Page(object):
    def __init__(self):
        self._head = '''
<html>
    <head>
        <title></title>
    </head>
    <body>'''
        self._body = ''
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
