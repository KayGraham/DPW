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

        '''
        page_close = '''
        </form>
    </body>
</html>
'''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
