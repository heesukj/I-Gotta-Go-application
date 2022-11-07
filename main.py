'''https://realpython.com/python-web-applications/#set-up-your-project

After you create the Flask app, you write a Python decorator on line 5 called @app.route that 
Flask uses to connect URL endpoints with code contained in functions. The argument to @app.route 
defines the URL’s path component, which is the root path ("/") in this case.
The code on lines 6 and 7 makes up index(), which is wrapped by the decorator. 
This function defines what should be executed if the defined URL endpoint is requested by a user. 
Its return value determines what a user will see when they load the page.'''

# main.py is the file that Flask uses to deliver your content
from flask import Flask, render_template, request  
from service import Service 
app = Flask(__name__)     # create an instance of a Flask app

# instantiate an instance of Service class and save it as 'service'
service = Service()

# Python decorator (Flask app) - 200: ok, 404: not found - has info only about route
@app.route("/", methods=["GET", "POST"])      # / is home route - Rest API call
def index():
    ''' Pass the results of bathroom locations, form, and num_locations to UI through index.html'''
    locations, form, num_locations, error_msg = service.index_route(request)
    return render_template("index.html", locations=locations, form=form, num_locations=num_locations, error_msg=error_msg)

#  tell Flask to start the web server at host="127.0.0.1" and port=8080
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)