class Page(object):
    def __init__(self):
        self.__title = "Welcome!"   #private title attribute
        self.__css = "css/main.css"     #private css attribute
        self.head = """
<DOCTYPE HTML>
<hml>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.__body = "Welcome to my OOP Python page!"
        self.close = """
    </body>
</html>
        """

        self.whole_page = ""

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()

    @property   #Creating getter property
    def title(self):
        return self.__title

    @title.setter   #setter
    def title(self, new_title):
        self.__title = new_title
        self.update()

    @property
    def css(self):
       return self.__css

    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file
        self.update()
