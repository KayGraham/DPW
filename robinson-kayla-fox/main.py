'''
Kayla Robinson
5/22/2014
DPW
What does the Fox say?
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #array to hold animal classes
        arr = []
        redobj = RedFox()
        zebraobj = Zebra()
        pandaobj = Panda()

        #adding instance of animal classes to array
        arr.append(redobj)
        arr.append(zebraobj)
        arr.append(pandaobj)

        #ckeck for name var in url
        if self.request.GET:
            name = self.request.GET['name']
            animal1 = 'red'
            animal2 = 'zebra'
            animal3 = 'panda'

            #select animal
            if name == animal1:
                x = 0
                s = redobj.animal_sound()
                p = Page()
                #print animal info to html
                self.response.write(p.print_out() + '<div id="animals"><div id="animalsImg"><img src=" ' + str(arr[x].animal_image) + '" />' + '</div><div id="name"><img src=" ' + str(arr[x].animal_print) + '" /><h3>' + str(arr[x].animal_name) + '</h3></div><p><h4>Phylum: </h4>' + str(arr[x].animal_phylum) + '</p><p><h4>Class:</h4> ' + str(arr[x].animal_class) + '</p><p><h4>Order:</h4> ' + str(arr[x].animal_order) + '</p><p><h4>Family:</h4> ' + str(arr[x].animal_family) + '</p><p><h4>Genus:</h4> ' + str(arr[x].animal_genus) + '</p><p><h4>Lifespan:</h4> ' + str(arr[x].animal_lifespan) + '</p><p><h4>Habitat:</h4> ' + str(arr[x].animal_habitat) + '</p><p><h4>Geolocation:</h4> ' + str(arr[x].animal_geolocation) + '</p><p><h4>What sound does the Red Fox make?</h4> ' + s)

            elif name == animal2:
                x = 1
                s = zebraobj.animal_sound()
                p = Page()
                #print animal info to html
                self.response.write(p.print_out() + '<div id="animals"><div id="animalsImg"><img src=" ' + str(arr[x].animal_image) + '" />' + '</div><div id="name"><img src=" ' + str(arr[x].animal_print) + '" /><h3>' + str(arr[x].animal_name) + '</h3></div><p><h4>Phylum: </h4>' + str(arr[x].animal_phylum) + '</p><p><h4>Class:</h4> ' + str(arr[x].animal_class) + '</p><p><h4>Order:</h4> ' + str(arr[x].animal_order) + '</p><p><h4>Family:</h4> ' + str(arr[x].animal_family) + '</p><p><h4>Genus:</h4> ' + str(arr[x].animal_genus) + '</p><p><h4>Lifespan:</h4> ' + str(arr[x].animal_lifespan) + '</p><p><h4>Habitat:</h4> ' + str(arr[x].animal_habitat) + '</p><p><h4>Geolocation:</h4> ' + str(arr[x].animal_geolocation) + '</p><p><h4>What sound does the Zebra make?</h4> ' + s)
            elif name == animal3:
                x = 2
                s = pandaobj.animal_sound()
                p = Page()
                #print animal info to html
                self.response.write(p.print_out() + '<div id="animals"><div id="animalsImg"><img src=" ' + str(arr[x].animal_image) + '" />' + '</div><div id="name"><img src=" ' + str(arr[x].animal_print) + '" /><h3>' + str(arr[x].animal_name) + '</h3></div><p><h4>Phylum: </h4>' + str(arr[x].animal_phylum) + '</p><p><h4>Class:</h4> ' + str(arr[x].animal_class) + '</p><p><h4>Order:</h4> ' + str(arr[x].animal_order) + '</p><p><h4>Family:</h4> ' + str(arr[x].animal_family) + '</p><p><h4>Genus:</h4> ' + str(arr[x].animal_genus) + '</p><p><h4>Lifespan:</h4> ' + str(arr[x].animal_lifespan) + '</p><p><h4>Habitat:</h4> ' + str(arr[x].animal_habitat) + '</p><p><h4>Geolocation:</h4> ' + str(arr[x].animal_geolocation) + '</p><p><h4>What sound does the Panda make?</h4> ' + s)

        #print if no var in url
        else:
            p = Page()
            self.response.write(p.print_out())

#html template
class Page():
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
                <li><a href="?name=red">Red Fox</a></li>
                <li><a href="?name=zebra">Zebra</a></li>
                <li><a href="?name=panda">Giant Panda</a></li>
            </ul>
        </nav>

        '''
        self._close = '''
        </div>
    </body>
</html>
        '''
    def print_out(self):
        return self._head + self._body

#Animal super class
class Animal(object):
    def __init__(self):
        self.animal_name = ''
        self.animal_phylum = ''
        self.animal_class = ''
        self.animal_order = ''
        self.animal_family = ''
        self.animal_genus = ''
        self.animal_image = ''
        self.animal_print = ''
        self.animal_lifespan = ''
        self.animal_habitat = ''
        self.animal_geolocation = ''

    def animal_sound(self):
        sound = ''

#Red Fox subclass
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
        self.animal_print = 'images/foxprint.png'
        self.animal_lifespan = '2-4 years'
        self.animal_habitat = 'Woods, prairies and farmlands'
        self.animal_geolocation = 'Europe, Asia and North America'

    #sound method override
    def animal_sound(self):
        self.sound = 'Wa-pa-pa-pa-pa-pa-pow'
        return self.sound

#Zebra subclass
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
        self.animal_print = 'images/zebraprint.png'
        self.animal_lifespan = '20-30 years'
        self.animal_habitat = 'Grassy Plains, open woodlands and grassy mountain slopes'
        self.animal_geolocation = 'Africa'

    #sound method override
    def animal_sound(self):
        self.sound = 'Yip'
        return self.sound

#Panda subclass
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
        self.animal_print = 'images/pandaprint.png'
        self.animal_lifespan = '20 years'
        self.animal_habitat = 'Bamboo Forests'
        self.animal_geolocation = 'Western China'

    #sound method override
    def animal_sound(self):
        self.sound = 'bleat'
        return self.sound


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
