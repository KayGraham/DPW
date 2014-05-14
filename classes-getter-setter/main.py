'''
Kayla Robinson
5/8/2014
DPW
Classes 2
'''
import webapp2
from pages import Page #from package import Class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My page!"
        p.css = "css/main.css"
        p.body = "Miss Piggy like Kermit De Frog!"

        self.response.write(p.whole_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
