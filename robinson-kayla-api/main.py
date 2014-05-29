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
        p.inputs = [['category', 'text', 'category'],['city', 'text', 'location'],['state', 'text', 'region'],['zip code', 'text', 'postal_code'],['Submit', 'submit']]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
