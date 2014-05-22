'''
Kayla Robinson
5/22/2014
DPW
What does the Fox say?
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>What does the fox say?</title>
    </head>
    <body>
        '''
        self._body = '<div id="animals">'
        self._close = '''
        </div>
    </body>
</html>
        '''
    def print_out(self):
        return self._head + self._body + self._close

class RedFox(Page):
    def __init__(self):
        super(RedFox, self).__init__()
        self._red_name = 'Red Fox'
        self._red_phylum = 'Chordata'
        self._red_class = 'Mammalia'
        self._red_order = 'Carnivora'
        self._red_family = 'Cannidae'
        self._red_genus = 'Vulpes'
        self._red_image = 'http://www.nhptv.org/natureworks/graphics/redfox1sm.jpg'
        self._red_lifespan = '2-4 years'
        self._red_habitat = 'Woods, prairies and farmlands'
        self._red_geolocation = 'Europe, Asia and North America'
        self._red_fox = ''
        self._red_info = [self._red_name, self._red_phylum, self._red_class, self._red_order, self._red_family, self._red_genus, self._red_image, self._red_lifespan, self._red_habitat, self._red_geolocation]

        self._red_fox += '<h2>' + self._red_info[0] + '</h2>' + '<p><strong>Phylum:</strong> ' + self._red_info[1] + '</p><p><strong>Class:</strong> ' + self._red_info[2] + '</p><p><strong>Order:</strong> ' + self._red_info[3] + '</p><p><strong>Family:</strong> ' + self._red_info[4] + '</p><p><strong>Genus:</strong> ' + self._red_info[5] + '</p><p><strong>Image:</strong> ' + self._red_info[6] + '</p><p><strong>Average Lifespan:</strong> ' + self._red_info[7] + '</p><p><strong>Habitat:</strong> ' + self._red_info[8] + '</p><p><strong>Geolocation:</strong> ' + self._red_info[9]

        print self._red_fox

    def print_out(self):
        return self._head + self._body + self._red_fox + '<div id="say"><h3>What does the Red Fox say?</h3><p>"Wa-pa-pa-pa-pa-pa-pow"</p></div>' + self._close

class Zebra(Page):
    def __init__(self):
        super(Zebra, self).__init__()
        self._zebra_name = 'Zebra'
        self._zebra_phylum = 'Chordata'
        self._zebra_class = 'Mammalia'
        self._zebra_order = 'Perissodactyla'
        self._zebra_family = 'Equidae'
        self._zebra_genus = 'Equus'
        self._zebra_image = 'http://www.nhptv.org/natureworks/graphics/redfox1sm.jpg'
        self._zebra_lifespan = '20-30 years'
        self._zebra_habitat = 'Grassy Plains, open woodlands and grassy mountain slopes'
        self._zebra_geolocation = 'Africa'
        self._zebra = ''
        self._zebra_info = [self._zebra_name, self._zebra_phylum, self._zebra_class, self._zebra_order, self._zebra_family, self._zebra_genus, self._zebra_image, self._zebra_lifespan, self._zebra_habitat, self._zebra_geolocation]

        self._zebra += '<h2>' + self._zebra_info[0] + '</h2>' + '<p><strong>Phylum:</strong> ' + self._zebra_info[1] + '</p><p><strong>Class:</strong> ' + self._zebra_info[2] + '</p><p><strong>Order:</strong> ' + self._zebra_info[3] + '</p><p><strong>Family:</strong> ' + self._zebra_info[4] + '</p><p><strong>Genus:</strong> ' + self._zebra_info[5] + '</p><p><strong>Image:</strong> ' + self._zebra_info[6] + '</p><p><strong>Average Lifespan:</strong> ' + self._zebra_info[7] + '</p><p><strong>Habitat:</strong> ' + self._zebra_info[8] + '</p><p><strong>Geolocation:</strong> ' + self._zebra_info[9]

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
        self._panda_image = 'http://www.nhptv.org/natureworks/graphics/redfox1sm.jpg'
        self._panda_lifespan = '20 years'
        self._panda_habitat = 'Bamboo Forests'
        self._panda_geolocation = 'Western China'
        self._panda = ''
        self._panda_info = [self._panda_name, self._panda_phylum, self._panda_class, self._panda_order, self._panda_family, self._panda_genus, self._panda_image, self._panda_lifespan, self._panda_habitat, self._panda_geolocation]

        self._panda += '<h2>' + self._panda_info[0] + '</h2>' + '<p><strong>Phylum:</strong> ' + self._panda_info[1] + '</p><p><strong>Class:</strong> ' + self._panda_info[2] + '</p><p><strong>Order:</strong> ' + self._panda_info[3] + '</p><p><strong>Family:</strong> ' + self._panda_info[4] + '</p><p><strong>Genus:</strong> ' + self._panda_info[5] + '</p><p><strong>Image:</strong> ' + self._panda_info[6] + '</p><p><strong>Average Lifespan:</strong> ' + self._panda_info[7] + '</p><p><strong>Habitat:</strong> ' + self._panda_info[8] + '</p><p><strong>Geolocation:</strong> ' + self._panda_info[9]

        print self._panda

    def print_out(self):
        return self._head + self._body + self._panda + '<div id="say"><h3>What does the Zebra say?</h3><p>"bleat"</p></div>' + self._close



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
