'''
Kayla Robinson
5/14/2014
DPW
Inheritance
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

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
        self._body = 'Filler'
        self._close = '''
    </body>
</html>
        '''
    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constrctor function for the super class
        super(FormPage, self).__init__()
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
