'''
Kayla Robinson
5/22/2014
DPW
What does the Fox say?
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        arr = []



class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>What does the fox say?</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self._body = '''
        <header>
            <img src="images/logo.png" alt="Albany Zoo" width="800px"/>
        </header>
        <nav>
            <ul>
                <h2>Select an Animal</h2>
                <li><a href="?name=red">Red Fox</a></li>
                <li><a href="?name=zebra">Zebra</a></li>
                <li><a href="?name=panda">Giant Panda</a></li>
            </ul>
        </nav>
        <div id="animals">
        '''
        self._close = '''
        </div>
    </body>
</html>
        '''
    def print_out(self):
        return self._head + self._body + self._close

class Animal(object):
    def __init__(self):
        self.animal_name = ''
        self.animal_phylum = ''
        self.animal_class = ''
        self.animal_order = ''
        self.animal_family = ''
        self.animal_genus = ''
        self.animal_image = ''
        self.animal_lifespan = ''
        self.animal_habitat = ''
        self.animal_geolocation = ''

    def animal_sound(self):
        sound = ''

class RedFox(Animal):
    def __init__(self):
        super(RedFox, self).__init__()
        self.animal_name = 'Red Fox'
        self.animal_phylum = 'Chordata'
        self.animal_class = 'Mammalia'
        self.animal_order = 'Carnivora'
        self.animal_family = 'Cannidae'
        self.animal_genus = 'Vulpes'
        self.animal_image = 'images/fox.png'
        self.animal_lifespan = '2-4 years'
        self.animal_habitat = 'Woods, prairies and farmlands'
        self.animal_geolocation = 'Europe, Asia and North America'

    def animal_sound(self):
        sound = 'Wa-pa-pa-pa-pa-pa-pow'

class Zebra(Animal):
    def __init__(self):
        super(Zebra, self).__init__()
        self.animal_name = 'Zebra'
        self.animal_phylum = 'Chordata'
        self.animal_class = 'Mammalia'
        self.animal_order = 'Perissodactyla'
        self.animal_family = 'Equidae'
        self.animal_genus = 'Equus'
        self.animal_image = 'images/zebra.png'
        self.animal_lifespan = '20-30 years'
        self.animal_habitat = 'Grassy Plains, open woodlands and grassy mountain slopes'
        self.animal_geolocation = 'Africa'

    def animal_sound(self):
        sound = 'Yip'

class Panda(Animal):
    def __init__(self):
        super(Panda, self).__init__()
        self.animal_name = 'Giant Panda'
        self.animal_phylum = 'Chordata'
        self.animal_class = 'Mammalia'
        self.animal_order = 'Carnivora'
        self.animal_family = 'Ursidae'
        self.animal_genus = 'Ailuropoda'
        self.animal_image = 'images/panda.png'
        self.animal_lifespan = '20 years'
        self.animal_habitat = 'Bamboo Forests'
        self.animal_geolocation = 'Western China'

    def animal_sound(self):
        sound = 'bleat'

class Select(Page):
    def __init__(self):
        super(Select, self).__init__()
        self._body ='''
        <header>
            <img src="images/logo.png" alt="Albany Zoo" width="800px"/>
        </header>

        <nav>

            <ul>
                <h2>Select an Animal</h2>
                <li><a href="?name=red">Red Fox</a></li>
                <li><a href="?name=zebra">Zebra</a></li>
                <li><a href="?name=panda">Giant Panda</a></li>
            </ul>
        </nav>
        '''
        self._close = '''
    </body>
</html>
        '''

        print self._body

    def print_out(self):
        return self._head + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
