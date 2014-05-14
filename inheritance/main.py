'''
Kayla Robinson
5/14/2014
DPW
Inheritance
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Page(object): #barrowing stuff form the object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>
        '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
