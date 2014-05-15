'''
Kayla Robinson
5/15/20014
DPW
Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
        <link href="" rel="stylesheet" type="text/css" />
    </head>
    <body>
    '''
        page_body = '''
        <form method="GET">
            <label>Name: </label><input type="text" name="user"/>
            <label>Email: </label><input type="text" name="email"/>
            <label>Age: </label><input type="checkbox" name="age" value="18-29">18-29<br>
            <input type="checkbox" name="age" value="30-39">30-39<br>
            <input type="checkbox" name="age" value="40-49">40-49<br>
            <input type="checkbox" name="age" value="50+">50+
            <label>City: </label><input type="text" name="city"/>
        '''
        page_close = '''
        </form>
    </body>
</html>
'''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
