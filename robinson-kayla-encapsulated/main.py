'''
Kayla Robinson
5/14/2014
DPW
Encapsulated
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Option 1 Object
        option1 = Rental()
        option1.name = "Rental Property 1"
        option1.mortgage_amount = 30000
        option1.rent = 300
        option1.calc_monthly_profit()
        option1.calc_annual_profit()
        #self.response.write("monthly profit $" + str(option1.monthly_profit))
        #self.response.write("annual profit $" + str(option1.annual_profit))

        #Option 2 Object
        option2 = Rental()
        option2.name = "Rental Property 2"
        option2.mortgage_amount = 65000
        option2.rent = 550
        option2.calc_monthly_profit()
        option2.calc_annual_profit()
        #self.response.write("monthly profit $" + str(option2.monthly_profit))
        #self.response.write("annual profit $" + str(option2.annual_profit))

        #Option 3 Object
        option3 = Rental()
        option3.name = "Rental Property 3"
        option3.mortgage_amount = 75000
        option3.rent = 650
        option3.calc_monthly_profit()
        option3.calc_annual_profit()
        #self.response.write("monthly profit $" + str(option3.monthly_profit))
        #self.response.write("annual profit $" + str(option3.annual_profit))

        #Option 4 Object
        option4 = Rental()
        option4.name = "Rental Property 4"
        option4.mortgage_amount = 49000
        option4.rent = 500
        option4.calc_monthly_profit()
        option4.calc_annual_profit()
        #self.response.write("monthly profit $" + str(option4.monthly_profit))
        #self.response.write("annual profit $" + str(option4.annual_profit))

        #Option 5 Object
        option5 = Rental()
        option5.name = "Rental Property 5"
        option5.mortgage_amount = 95000
        option5.rent = 825
        option5.calc_monthly_profit()
        option5.calc_annual_profit()
        #self.response.write("monthly profit $" + str(option5.monthly_profit))
        #self.response.write("annual profit $" + str(option5.annual_profit))



        p = Page()
        #Array to hold the 5 objects
        p.properties = [option1, option2, option3, option4, option5]
        self.response.write(p.print_out())

        #Print data to html
        if self.request.GET:
            #var form url
            name = self.request.GET['name']
            mortgage = self.request.GET['mortgage']
            rent = self.request.GET['rent']
            monthly = self.request.GET['monthly']
            annual = self.request.GET['annual']
            message = '''
            <p>
            <strong>Property:</strong> {name}
            <br /><strong>Mortgage:</strong> {mortgage}
            <br /><strong>Rent:</strong> {rent}
            <br /><strong>Monthly Profit:</strong> {monthly}
            <br /><strong>Annual Profit:</strong> {annual}
            </p>
            '''
            message = message.format(**locals())
            self.response.write(message)
class Page(object):
    def __init__(self):
        self.__open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Rental Property Profit Calculator</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
    '''

        self.__content = '''
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" x="0px" y="0px" width="165.893px" height="117.86px" viewBox="0 0 165.893 117.86" enable-background="new 0 0 165.893 117.86" xml:space="preserve"><g id="Layer_1"><g><path fill="#00944B" d="M-621.309 397.25c0 0 2.3 0.8 6.6 2.17c1.082 0.4 2.3 0.8 3.6 1.2 c0.663 0.2 1.4 0.5 2.1 0.704c0.728 0.2 1.5 0.4 2.3 0.683c3.136 0.9 6.7 2 10.8 3.2 c4.089 1.1 8.6 2.3 13.5 3.515c4.951 1.1 10.2 2.5 16 3.514c1.434 0.3 2.9 0.6 4.4 0.8 c1.475 0.3 3 0.6 4.5 0.838c3.058 0.5 6.2 1 9.4 1.527c3.231 0.5 6.6 0.8 10 1.3 c3.394 0.5 6.9 0.8 10.5 1.096c1.78 0.2 3.6 0.3 5.4 0.507c1.822 0.1 3.7 0.2 5.5 0.3 c1.856 0.1 3.7 0.2 5.6 0.315c1.888 0.1 3.8 0.1 5.7 0.158c3.852 0.1 7.8 0.3 11.7 0.2 c1.987-0.018 3.99-0.035 6.007-0.053c1.008-0.011 2 0 3.035-0.027c1.015-0.041 2.034-0.082 3.056-0.122 c16.353-0.547 33.559-2.082 51.244-4.698c2.211-0.324 4.432-0.649 6.662-0.976l1.674-0.243l0.209-0.03 c0.097-0.015-0.096 0 0.086-0.015l0.424-0.076l0.849-0.152c1.132-0.203 2.266-0.407 3.402-0.61 c2.273-0.404 4.554-0.81 6.843-1.216c2.248-0.428 4.439-0.909 6.674-1.363c2.229-0.476 4.456-0.886 6.708-1.418 c2.255-0.527 4.517-1.057 6.784-1.587c4.548-0.997 9.069-2.28 13.634-3.441c18.228-4.841 36.529-10.929 54.771-17.347 c18.243-6.428 36.447-13.183 54.594-19.385c4.55-1.524 9.049-3.107 13.59-4.546c4.523-1.478 9.029-2.926 13.553-4.259 c2.268-0.682 4.527-1.362 6.78-2.04c2.238-0.631 4.468-1.26 6.69-1.886c4.494-1.2 9.018-2.43 13.491-3.449 c8.952-2.118 17.854-3.905 26.678-5.062c2.194-0.347 4.398-0.571 6.589-0.794c2.191-0.215 4.358-0.505 6.538-0.602 c2.174-0.131 4.334-0.261 6.48-0.391c2.152-0.031 4.292-0.062 6.416-0.093c2.121-0.079 4.2 0.1 6.3 0.1 c2.095 0.1 4.2 0.1 6.2 0.342c2.058 0.2 4.1 0.4 6.1 0.55c2.014 0.3 4 0.6 6 0.9 c0.988 0.2 2 0.3 3 0.473c0.972 0.2 1.9 0.4 2.9 0.611c1.92 0.4 3.8 0.8 5.7 1.3 c3.715 1.1 7.4 1.9 10.9 3.283c1.745 0.6 3.5 1.2 5.2 1.858c1.666 0.7 3.3 1.4 4.9 2.1 c0.813 0.4 1.6 0.7 2.4 1.044c0.876 0.4 1.6 0.8 2.4 1.146c1.523 0.8 3 1.5 4.5 2.2 c2.981 1.4 5.8 3.1 8.6 4.583c1.385 0.8 2.8 1.5 4.1 2.289c1.313 0.8 2.6 1.6 3.9 2.4 c1.271 0.8 2.5 1.5 3.8 2.286c1.233 0.7 2.4 1.6 3.5 2.353c2.292 1.6 4.6 3 6.6 4.6 c4.098 3.1 7.9 5.9 11.1 8.787c1.619 1.4 3.2 2.7 4.6 3.949c1.367 1.3 2.6 2.6 3.8 3.7 c1.19 1.2 2.3 2.2 3.3 3.198c0.977 1 1.8 2 2.6 2.82c3.065 3.4 4.7 5.2 4.7 5.195l-1.051 0.9 c0 0-1.69-1.723-4.86-4.952c-0.799-0.8-1.658-1.724-2.663-2.682c-1.036-0.926-2.168-1.937-3.39-3.028 c-1.222-1.091-2.533-2.263-3.933-3.514c-1.473-1.165-3.037-2.403-4.69-3.712c-3.237-2.699-7.131-5.286-11.272-8.213 c-2.093-1.434-4.372-2.779-6.678-4.255c-1.169-0.714-2.318-1.502-3.56-2.191c-1.236-0.695-2.494-1.402-3.772-2.121 c-1.277-0.718-2.574-1.448-3.893-2.188c-1.315-0.744-2.703-1.386-4.082-2.099c-2.787-1.38-5.564-2.888-8.628-4.21 c-1.51-0.684-3.039-1.377-4.587-2.079c-0.757-0.335-1.593-0.739-2.297-1.023c-0.787-0.307-1.58-0.614-2.377-0.925 c-1.591-0.619-3.201-1.247-4.829-1.881c-1.644-0.586-3.347-1.066-5.042-1.613c-3.371-1.171-6.949-1.892-10.541-2.792 c-1.801-0.429-3.663-0.671-5.516-1.021c-0.929-0.163-1.861-0.326-2.799-0.491c-0.935-0.174-1.895-0.231-2.846-0.354 c-1.907-0.215-3.83-0.432-5.769-0.65c-1.95-0.106-3.915-0.214-5.896-0.322c-1.976-0.155-3.979-0.114-5.992-0.12 c-2.015 0.019-4.039-0.062-6.082 0.087c-16.341 0.611-33.474 3.585-50.807 8.308c-4.361 1.132-8.651 2.438-13.041 3.8 c-2.203 0.692-4.413 1.387-6.631 2.084c-2.179 0.728-4.365 1.457-6.558 2.189c-4.413 1.444-8.823 3.016-13.262 4.6 c-4.445 1.527-8.877 3.21-13.343 4.827c-17.836 6.585-35.84 13.769-54.024 20.68c-18.185 6.905-36.494 13.737-54.98 19.4 c-4.639 1.37-9.22 2.856-13.875 4.065c-2.319 0.63-4.633 1.258-6.939 1.885c-2.312 0.613-4.689 1.124-7.022 1.7 c-2.337 0.541-4.689 1.119-6.995 1.623c-2.282 0.445-4.556 0.89-6.821 1.332c-1.134 0.22-2.265 0.438-3.394 0.656l-0.847 0.2 l-0.423 0.081l-0.554 0.096l-1.727 0.275c-2.301 0.365-4.593 0.729-6.875 1.091c-18.292 2.699-36.204 3.975-53.185 3.9 c-4.243 0.086-8.432-0.175-12.552-0.296c-4.122-0.084-8.173-0.469-12.155-0.736c-1.989-0.176-3.965-0.267-5.914-0.515 c-1.949-0.227-3.88-0.45-5.794-0.673c-1.912-0.223-3.806-0.442-5.681-0.661c-1.867-0.287-3.715-0.572-5.543-0.854 c-14.631-2.204-27.85-5.308-39.324-8.737c-5.772-1.593-11.039-3.532-15.947-5.142c-1.231-0.39-2.41-0.859-3.564-1.312 c-1.155-0.45-2.284-0.891-3.388-1.321c-2.204-0.859-4.306-1.68-6.3-2.457c-7.907-3.391-14.022-6.145-18.048-8.264 c-4.068-2.058-6.239-3.155-6.239-3.155L-621.309 397.25z"/></g><polyline fill="#00944B" points="-363.6,401.9 -363.6,259.9 -290.6,259.9 -290.6,375.9"/><g><path fill="#00944B" d="M14.956 101.538c0 0 0.5 0.2 1.6 0.497c1.023 0.4 2.5 0.8 4.4 1.2 c1.942 0.4 4.3 0.9 7 1.128c2.725 0.3 5.8 0.3 9.2 0.078c3.36-0.232 6.991-0.742 10.839-1.398 c3.85-0.688 7.909-1.415 12.109-2.166c1.055-0.204 2.117-0.41 3.188-0.617c1.063-0.217 2.173-0.383 3.197-0.678 c1.046-0.264 2.098-0.53 3.155-0.797l1.594-0.393l1.603-0.473c2.142-0.631 4.307-1.248 6.452-1.997 c2.155-0.705 4.315-1.442 6.471-2.213c4.311-1.524 8.633-3.089 12.928-4.531c2.146-0.724 4.312-1.362 6.43-2.035 c2.127-0.627 4.276-1.193 6.396-1.672c4.246-0.935 8.466-1.502 12.488-1.406c2.011 0 4 0.3 5.8 0.6 c1.855 0.4 3.6 0.8 5.3 1.45c0.834 0.3 1.6 0.7 2.4 0.979c0.77 0.4 1.5 0.7 2.2 1.1 c1.398 0.7 2.7 1.5 3.9 2.217c2.389 1.5 4.4 2.9 5.9 4.284c0.78 0.6 1.4 1.3 2 1.8 c0.281 0.3 0.5 0.5 0.8 0.756c0.224 0.2 0.4 0.5 0.6 0.67c0.724 0.8 1.1 1.2 1.1 1.228l-0.254 0.2 c0 0-0.4-0.407-1.149-1.169c-0.188-0.19-0.396-0.402-0.626-0.636c-0.245-0.219-0.513-0.457-0.802-0.715 c-0.572-0.522-1.236-1.112-2.033-1.712c-1.546-1.253-3.556-2.611-5.953-3.995c-1.199-0.699-2.506-1.359-3.903-2.036 c-0.709-0.317-1.454-0.668-2.185-0.979c-0.76-0.276-1.509-0.629-2.32-0.86c-1.596-0.544-3.314-0.921-5.103-1.211 c-1.798-0.236-3.669-0.402-5.601-0.354c-3.859 0.055-7.917 0.684-12.028 1.718c-2.058 0.525-4.119 1.129-6.215 1.8 c-2.076 0.725-4.188 1.411-6.295 2.187c-4.218 1.548-8.47 3.223-12.757 4.874c-2.135 0.842-4.286 1.655-6.447 2.4 c-2.142 0.819-4.326 1.533-6.485 2.264l-1.616 0.545l-1.652 0.478c-1.103 0.31-2.199 0.618-3.289 0.9 c-1.098 0.334-2.164 0.514-3.232 0.756c-1.066 0.229-2.126 0.455-3.176 0.68l-0.395 0.08l-0.453 0.08l-0.788 0.1 c-0.523 0.088-1.045 0.176-1.564 0.263c-1.041 0.17-2.073 0.339-3.094 0.506c-2.046 0.329-4.058 0.632-6.027 0.9 c-3.938 0.526-7.718 0.862-11.231 0.865c-3.511 0.026-6.739-0.309-9.542-0.826c-2.812-0.49-5.179-1.268-7.098-1.927 c-1.909-0.739-3.373-1.357-4.321-1.861c-0.966-0.478-1.48-0.733-1.48-0.733L14.956 101.538z"/></g><polyline fill="#00944B" points="73.4,97.9 73.4,63.9 91.4,63.9 91.4,91.9"/></g><g id="Layer_3"><path fill="none" stroke="#00944B" stroke-width="14" stroke-linejoin="round" stroke-miterlimit="10" d="M-440.576 420.9 c0 0 4-145-72-256l185-118l165 121c0 0-69 138-48 183"/><path fill="none" stroke="#00944B" stroke-width="3.3943" stroke-linejoin="round" stroke-miterlimit="10" d="M55.14 102.9 c0 0 0.97-35.156-17.456-62.068L82.537 12.23l40.005 29.337c0 0-16.729 33.458-11.638 44.4"/></g><g id="Layer_4"><g><path fill="#00944B" d="M-536.986 159.268l2.935-2.569l2.969-2.516l5.939-5.032l12.028-9.831c1.995-1.654 4.023-3.256 6.059-4.848 l6.093-4.795c4.068-3.188 8.112-6.412 12.199-9.57l24.696-18.683l12.458-9.172c4.145-3.07 8.342-6.06 12.524-9.072 c4.191-2.999 8.351-6.045 12.576-8.991l12.637-8.898c4.207-2.975 8.472-5.86 12.705-8.794c4.249-2.911 8.463-5.873 12.74-8.741 l12.808-8.637l6.404-4.317l6.447-4.252l12.895-8.504c4.285-2.855 8.632-5.613 12.954-8.412l0.093-0.06 c4.833-3.13 10.951-2.718 15.3 0.552l11.332 8.558c3.788 2.8 7.5 5.8 11.3 8.648l11.245 8.674l11.167 8.8 c3.714 2.9 7.5 5.8 11.1 8.808l11.074 8.903c3.701 3 7.4 6 11 8.964l10.986 9.02l10.906 9.1 c3.653 3 7.2 6.1 10.8 9.236l10.784 9.29c3.584 3.1 7.2 6.2 10.7 9.354l10.623 9.506l5.312 4.8 c1.767 1.6 3.5 3.2 5.2 4.844c3.482 3.2 7 6.5 10.5 9.735c3.425 3.3 6.9 6.6 10.3 9.973l-0.898 1.2 l-45.709-33.72l-45.582-33.89L-330.46 26.08l1.691 0.054c-8.603 5.659-17.251 11.249-25.886 16.858l-25.911 16.82l-51.822 33.6 l-51.822 33.64l-51.956 33.434L-536.986 159.268z"/></g><g><path fill="#00944B" d="M31.765 39.476l2.871-2.453l2.917-2.384c0.968-0.801 1.965-1.557 2.946-2.338l2.957-2.32l5.987-4.53 l6.064-4.413c1.015-0.729 2.014-1.482 3.045-2.186l3.074-2.141l3.075-2.141c1.028-0.708 2.041-1.441 3.083-2.128l6.232-4.155 l3.115-2.077c1.033-0.702 2.096-1.358 3.146-2.034l0.044-0.029c1.163-0.748 2.633-0.643 3.7 0.147l5.475 4.2 c1.831 1.4 3.6 2.8 5.4 4.228l5.392 4.288c1.808 1.4 3.5 2.9 5.3 4.373c1.768 1.5 3.6 2.9 5.3 4.4 c1.738 1.5 3.5 3 5.2 4.52c1.709 1.5 3.5 3.1 5.1 4.632c1.702 1.6 3.4 3.2 5 4.778l-0.217 0.3 L81.839 7.181l0.407 0.013L31.964 39.78L31.765 39.476z"/></g></g><g id="Layer_5"><g><path fill="#00944B" d="M-474.576 114.896c0.072-1.384 0.124-2.754 0.132-4.125c-0.002-1.372 0.028-2.731-0.008-4.092 c-0.072-2.721-0.211-5.419-0.442-8.094c-0.109-1.337-0.245-2.669-0.419-3.993c-0.146-1.324-0.345-2.641-0.555-3.948l-0.333-1.956 l-0.376-1.941c-0.279-1.286-0.558-2.567-0.885-3.832c-0.297-1.271-0.681-2.516-1.04-3.761c-0.418-1.228-0.771-2.469-1.237-3.668 c-0.414-1.218-0.939-2.388-1.417-3.571c-0.531-1.159-1.02-2.333-1.62-3.449c-0.545-1.144-1.206-2.22-1.813-3.321 c-0.311-0.546-0.661-1.067-0.988-1.602c-0.327-0.535-0.661-1.064-1.032-1.568l-1.076-1.533l-1.152-1.472 c-0.728-1.01-1.607-1.898-2.396-2.855l-0.054-0.066c-1.725-2.095-1.425-5.192 0.67-6.917c0.653-0.538 1.425-0.882 2.202-1.034 l4.986-0.953l4.995-0.905c3.327-0.622 6.668-1.158 10.004-1.728c3.334-0.579 6.685-1.061 10.027-1.596l5.024-0.735l5.028-0.711 l4.948 6.096c0.014-0.097-0.151 0.486-0.251 0.847c-0.125 0.37-0.215 0.841-0.302 1.319c-0.167 0.951-0.402 1.854-0.493 2.9 l-0.405 3.007c-0.148 1-0.175 2.053-0.27 3.079l-0.266 3.102c-0.116 1.031-0.116 2.087-0.167 3.134l-0.309 6.311l-0.143 6.4 l-0.099 3.194c-0.033 1.065-0.096 2.134-0.083 3.201c-0.001 2.134-0.081 4.279-0.116 6.425c-0.046 2.147-0.143 4.303-0.269 6.5 c-0.576-2.08-1.122-4.168-1.618-6.267c-0.485-2.1-1.014-4.2-1.464-6.311c-0.483-2.107-0.78-4.244-1.16-6.373l-0.518-3.203 c-0.163-1.07-0.351-2.137-0.495-3.212l-0.666-6.49c-0.089-1.087-0.23-2.164-0.253-3.267l-0.134-3.299 c-0.018-1.106-0.105-2.193-0.065-3.319l0.091-3.377c0.008-1.108 0.186-2.306 0.299-3.47c0.058-0.579 0.12-1.165 0.264-1.829 c0.146-0.677 0.17-1.148 0.545-2.251l4.947 6.096l-4.971 1.039l-4.976 1.015c-3.325 0.631-6.641 1.316-9.973 1.9 c-3.331 0.597-6.656 1.227-9.996 1.772l-5.005 0.845l-5.014 0.797l2.817-8.016c0.916 1.2 1.9 2.3 2.7 3.524l1.278 1.8 l1.17 1.896c0.401 0.6 0.8 1.3 1.1 1.926c0.349 0.7 0.7 1.3 1 1.956c0.638 1.3 1.3 2.7 1.8 4 c0.58 1.4 1 2.7 1.5 4.12c0.409 1.4 0.8 2.8 1.2 4.207c0.363 1.4 0.6 2.8 0.9 4.2 c0.219 1.4 0.5 2.8 0.6 4.27c0.188 1.4 0.3 2.9 0.3 4.272c0.061 1.4 0.1 2.8 0.1 4.3 c-0.022 1.418-0.06 2.832-0.152 4.239c-0.083 1.408-0.227 2.81-0.388 4.205c-0.155 1.395-0.376 2.782-0.613 4.2 c-0.226 1.38-0.543 2.746-0.854 4.104c-0.331 1.356-0.645 2.708-1.074 4.036C-473.617 112.293-474.036 113.617-474.576 114.896z"/></g><g><path fill="#00944B" d="M46.896 28.717c0.07-1.338 0.027-2.657-0.075-3.955c-0.019-0.324-0.075-0.646-0.107-0.968 c-0.023-0.322-0.086-0.639-0.131-0.957c-0.042-0.318-0.104-0.632-0.177-0.944c-0.071-0.311-0.125-0.625-0.213-0.929l-0.241-0.915 l-0.309-0.888c-0.089-0.299-0.236-0.575-0.356-0.86c-0.121-0.284-0.224-0.576-0.381-0.841l-0.43-0.811 c-0.16-0.259-0.339-0.506-0.505-0.759c-0.158-0.26-0.344-0.499-0.543-0.726l-0.565-0.706l-0.027-0.034 c-0.407-0.509-0.325-1.251 0.183-1.659c0.156-0.125 0.34-0.205 0.523-0.239c1.613-0.299 3.223-0.62 4.846-0.867l2.43-0.396 c0.812-0.123 1.626-0.228 2.438-0.342c0.594-0.084 1.1 0.3 1.2 0.923c0.015 0.1 0 0.216-0.003 0.32l-0.035 0.2 c-0.028 0.175-0.099 0.26-0.122 0.536l-0.101 0.711l-0.121 0.713c-0.046 0.236-0.035 0.499-0.056 0.7 c-0.05 1.008-0.107 2.02-0.195 3.039c0.012 2.051-0.019 4.117-0.165 6.218c-0.513-2.021-0.926-4.078-1.266-6.149 c-0.103-1.05-0.175-2.107-0.238-3.169c-0.01-0.268-0.052-0.525-0.033-0.803l0.04-0.831l0.062-0.832 c-0.004-0.245 0.109-0.651 0.189-0.982l1.189 1.464c-0.804 0.168-1.605 0.347-2.41 0.506l-2.42 0.5 c-1.61 0.319-3.233 0.563-4.853 0.831l0.679-1.932l0.66 0.859c0.229 0.3 0.4 0.6 0.6 0.9 c0.176 0.3 0.4 0.6 0.5 0.938l0.434 0.979c0.157 0.3 0.3 0.7 0.4 0.998c0.102 0.3 0.2 0.7 0.3 1 l0.224 1.028l0.146 1.034c0.062 0.3 0.1 0.7 0.1 1.036s0.032 0.7 0 1.033c0.007 0.687-0.044 1.37-0.126 2 C47.679 26.1 47.4 27.5 46.9 28.717z"/></g></g><g id="Layer_6"></g></svg>
        <h1>Select a Property</h1>

        '''
        self.__close = '''
    </body>
</html>'''

        self.__properties = []

    #Get properties
    @property
    def properties(self):
        pass

    @properties.setter
    def properties(self, p):
        self.__properties = p
        self.links()

    def links(self):
        for properties in self.__properties:
            self.__content += '<a href="?name=' + properties.name + '&mortgage=' + str(properties.mortgage_amount) + '&rent=' + str(properties.rent) + '&monthly=' + str(properties.monthly_profit) + '&annual=' + str(properties.annual_profit)+ '">' + properties.name + '</a><br />'

    def print_out(self):
        return self.__open + self.__content + self.__close

#Rental property class data object
class Rental(object):
    def __init__(self):
        #attributes
        self.name = ""
        self.mortgage_amount = 0
        self.rent = 0
        self.__monthly_profit = 0
        self.__annual_profit = 0

    #Calculate Monthly Profit
    @property
    def monthly_profit(self):
        return self.__monthly_profit

    @monthly_profit.setter
    def monthly_profit(self, new_monthly_profit):
        self.__monthly_profit = new_monthly_profit

    def calc_monthly_profit(self):
        #calculate monthly profit
        self.__monthly_profit = (self.rent - ((self.mortgage_amount / 10))/12)

    #Calculate Annual Profit
    @property
    def annual_profit(self):
        return self.__annual_profit

    @annual_profit.setter
    def annual_profit(self, new_annual_profit):
        self.__annual_profit = new_annual_profit

    def calc_annual_profit(self):
        #calculate annual profit
        self.__annual_profit = (self.monthly_profit * 12)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
