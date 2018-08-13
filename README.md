# python-exercise - autocomplete with Trie

## Summary
The present code represents a simple webAPI based on the Flask web framework that reports a list of strings from a list based on the initial characters of a string.

### Prerequisites
To run the present application:
```
Linux Server
Postman (or other method of executing HTTP requests)
```

### Installing
As specified, this application must run on a linux machine. For this reason, a virtual environment was created with the OS ubuntu 18.
The application was also developed with the help of virtualenv.

For deployment, simply copy the files in the repo to the desired location, install the requirements, and run the application by simply running the app.py script.


#### Requirements
This web service has the following dependencies:

* aniso8601==3.0.2
* click==6.7
* Flask==1.0.2
* Flask-RESTful==0.3.6
* itsdangerous==0.24
* Jinja2==2.10
* MarkupSafe==1.0
* pkg-resources==0.0.0
* pygtrie==2.3
* pytz==2018.5
* six==1.11.0
* Werkzeug==0.14.1

To install the required modules:
  pip install -r requirements.txt
  
For HTTP requests, Postman was used.

## Running the application
The applications sends and recieves JSON files.

#### GET
A GET method was implemented that returns the full list of apps that was loaded into the application.

#### POST
A POST method was also implemented that receives a JSON input with the characters that will allow the strings search:

```
{
'prefix':"Fac"
}
```

The result is then:



## Tests
A simple test was implemented using unittest

