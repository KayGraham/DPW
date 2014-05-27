'''
Kayla Robinson
5/27/2014
API
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['name', 'text', 'name'],['category', 'text', 'category'],['city, state or zip code', 'text', 'location'],['Submit', 'submit']]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
