'''
Kayla Robinson
5/15/20014
DPW
Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Setup page head
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Savvy Shoppers</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <header>
            <img src="images/logo.png" alt="Savvy Shopper" height="95px"/>
            <div id="shop"><h1>Savvy Shoppers</h1>
            <p>Sign up for exclusive deals and coupons!</p></div>
        </header>
    '''
         #Setup page body
        page_body = '''
        <div id="signUp">
        <form method="GET">
            <div id="labels">
                <label>Name: </label><br />
                <label>Email: </label><br />
                <label>Age: </label><br /><br /><br /><br /><br />
                <label>City: </label><br />
                <label>State: </label>
            </div>
            <div id="inputs">
                <input type="text" name="user" /><br />
                <input type="text" name="email"/><br />
                <input type="checkbox" name="age" value="18-29">18-29<br>
                <input type="checkbox" name="age" value="30-39">30-39<br>
                <input type="checkbox" name="age" value="40-49">40-49<br>
                <input type="checkbox" name="age" value="50+">50+<br />
                <input type="text" name="city"/><br />
                <select name="state">
                    <option value="Alabama">Alabama</option>
                    <option value="Alaska">Alaska</option>
                    <option value="Arizona">Arizona</option>
                    <option value="Arkansas">Arkansas</option>
                    <option value="California">California</option>
                    <option value="Colorado">Colorado</option>
                    <option value="Connecticut">Connecticut</option>
                    <option value="Delaware">Delaware</option>
                    <option value="Florida">Florida</option>
                    <option value="Georgia">Georgia</option>
                    <option value="Hawaii">Hawaii</option>
                    <option value="Idaho">Idaho</option>
                    <option value="Illinois">Illinois</option>
                    <option value="Indiana">Indiana</option>
                    <option value="Iowa">Iowa</option>
                    <option value="Kansas">Kansas</option>
                    <option value="Kentucky">Kentucky</option>
                    <option value="Louisiana">Louisiana</option>
                    <option value="Maine">Maine</option>
                    <option value="Maryland">Maryland</option>
                    <option value="Massachusetts">Massachusetts</option>
                    <option value="Michigan">Michigan</option>
                    <option value="Minnesota">Minnesota</option>
                    <option value="Mississippi">Mississippi</option>
                    <option value="Missouri">Missouri</option>
                    <option value="Montana">Montana</option>
                    <option value="Nebraska">Nebraska</option>
                    <option value="Nevada">Nevada</option>
                    <option value="New Hampshire">New Hampshire</option>
                    <option value="New Jersey">New Jersey</option>
                    <option value="New Mexico">New Mexico</option>
                    <option value="New York">New York</option>
                    <option value="North Carolina">North Carolina</option>
                    <option value="North Dakota">North Dakota</option>
                    <option value="Ohio">Ohio</option>
                    <option value="Oklahoma">Oklahoma</option>
                    <option value="Oregon">Oregon</option>
                    <option value="Pennsylvania">Pennsylvania</option>
                    <option value="Rhode Island">Rhode Island</option>
                    <option value="South Carolina">South Carolina</option>
                    <option value="South Dakota">South Dakota</option>
                    <option value="Tennessee">Tennessee</option>
                    <option value="Texas">Texas</option>
                    <option value="Utah">Utah</option>
                    <option value="Vermont">Vermont</option>
                    <option value="Virginia">Virginia</option>
                    <option value="Washington">Washington</option>
                    <option value="West Virginia">West Virginia</option>
                    <option value="Wisconsin">Wisconsin</option>
                    <option value="Wyoming">Wyoming</option>
                </select>
            </div>
            <div id="submit">
                <input type="submit" value="Sign Up" />
            </div>
        '''
        #Setup page close
        page_close = '''
        </form></div>
    </body>
</html>
'''
        #Get var form url
        if self.request.GET:
            #vars from url
            user = self.request.GET['user']
            email = self.request.GET['email']
            age = self.request.GET['age']
            city = self.request.GET['city']
            state = self.request.GET['state']
            #print information entered on to html
            self.response.write(page_head + '<div id="confirm">' + '<div id="info"><div id="labels"> <label>Name: </label><br /><label>Email: </label><br /><label>Age: </label><br /><label>City: </label><br /> <label>State: </label>' +  '</div><div id="userInfo">' + user + '<br />' + email + '<br />' + age + '<br />' + city + '<br />' + state + '</div></div>' + page_close)

        #if form not submitted print
        else:
            #print page
            self.response.write(page_head + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)