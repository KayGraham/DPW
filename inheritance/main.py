'''
Kayla Robinson
5/14/2014
DPW
Inheritance
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
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
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        #<input type="text" value="" name="first_name" placeholder="First Name" />
        # ['first_name', 'text', 'First Name']
        #<input type="text" value="" name="last_name" placeholder="Last Name" />
        #<input type="submit" value="Submit" />



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
