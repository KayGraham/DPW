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

class RedFox(Page):
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

class Zebra(Page):
    def __init__(self):
        super(Zebra, self).__init__()
        self._zebra_name = 'Zebra'
        self._zebra_phylum = 'Chordata'
        self._zebra_class = 'Mammalia'
        self._zebra_order = 'Perissodactyla'
        self._zebra_family = 'Equidae'
        self._zebra_genus = 'Equus'
        self._zebra_image = 'images/zebra.png'
        self._zebra_lifespan = '20-30 years'
        self._zebra_habitat = 'Grassy Plains, open woodlands and grassy mountain slopes'
        self._zebra_geolocation = 'Africa'
        self._zebra = ''
        self._zebra_info = [self._zebra_name, self._zebra_phylum, self._zebra_class, self._zebra_order, self._zebra_family, self._zebra_genus, self._zebra_image, self._zebra_lifespan, self._zebra_habitat, self._zebra_geolocation]

        self._zebra += '<h2>' + self._zebra_info[0] + '</p><img src=" ' + self._zebra_info[6] + '" /></h2>' + '<p><strong>Phylum:</strong> ' + self._zebra_info[1] + '</p><p><strong>Class:</strong> ' + self._zebra_info[2] + '</p><p><strong>Order:</strong> ' + self._zebra_info[3] + '</p><p><strong>Family:</strong> ' + self._zebra_info[4] + '</p><p><strong>Genus:</strong> ' + self._zebra_info[5] + '" </p><p><strong>Average Lifespan:</strong> ' + self._zebra_info[7] + '</p><p><strong>Habitat:</strong> ' + self._zebra_info[8] + '</p><p><strong>Geolocation:</strong> ' + self._zebra_info[9]

        print self._zebra

    def print_out(self):
        return self._head + self._body + self._zebra + '<div id="say"><h3>What does the Zebra say?</h3><p>"Yip"</p></div>' + self._close

class Panda(Page):
    def __init__(self):
        super(Panda, self).__init__()
        self._panda_name = 'Giant Panda'
        self._panda_phylum = 'Chordata'
        self._panda_class = 'Mammalia'
        self._panda_order = 'Carnivora'
        self._panda_family = 'Ursidae'
        self._panda_genus = 'Ailuropoda'
        self._panda_image = 'images/panda.png'
        self._panda_lifespan = '20 years'
        self._panda_habitat = 'Bamboo Forests'
        self._panda_geolocation = 'Western China'
        self._panda = ''
        self._panda_info = [self._panda_name, self._panda_phylum, self._panda_class, self._panda_order, self._panda_family, self._panda_genus, self._panda_image, self._panda_lifespan, self._panda_habitat, self._panda_geolocation]

        self._panda += '<h2>' + self._panda_info[0] + '</p><img src=" ' + self._panda_info[6] + '" /></h2>' + '<p><strong>Phylum:</strong> ' + self._panda_info[1] + '</p><p><strong>Class:</strong> ' + self._panda_info[2] + '</p><p><strong>Order:</strong> ' + self._panda_info[3] + '</p><p><strong>Family:</strong> ' + self._panda_info[4] + '</p><p><strong>Genus:</strong> ' + self._panda_info[5] + '" </p><p><strong>Average Lifespan:</strong> ' + self._panda_info[7] + '</p><p><strong>Habitat:</strong> ' + self._panda_info[8] + '</p><p><strong>Geolocation:</strong> ' + self._panda_info[9]

        print self._panda

    def print_out(self):
        return self._head + self._body + self._panda + '<div id="say"><h3>What does the Giant Panda say?</h3><p>"bleat"</p></div>' + self._close

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
