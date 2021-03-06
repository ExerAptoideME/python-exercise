# python-exercise - autocomplete with Trie

## Summary
The present code represents a simple webAPI based on the Flask web framework that reports a list of strings from a list based on the initial characters of a string.

### Prerequisites
To run the present application:
```
Linux Server
Postman (or other method of executing HTTP requests)
List of apps in csv format (strings)
```

### Installing
As specified, this application must run on a linux machine. For this reason, a virtual environment was created with the OS ubuntu 18. The application was also developed with the help of virtualenv.

For deployment, simply copy the files in the repo to the desired location, install the requirements, and run the application by simply running the app.py script with line 36 of the script uncommented (app.run(host="127.1.1.1", port=6000, debug=True, load_dotenv=True)).

For search purposes, the pygtrie modukes was used to quickly implement a Trie data structure into the project.

The apps list in cvs should be on the same folder as the app.py script. The filename/path is specified on line 13 of app.py:
```
applist = load.loader('190titles.csv')
```

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
The application sends and recieves JSON files that correspond to the App list data and to the auto-complete reponse.

On a local server application, the host is 127.1.1.1 on port 6000.

To run in standalone, please uncomment the following code line present in the 
app.py file: app.run(host="127.1.1.1", port=6000, debug=True, load_dotenv=True)

#### GET on '/'
A GET method was implemented that returns the full list of apps that was loaded into the application.

#### POST on '/output'
A POST method was also implemented that receives a JSON input with the characters that will allow the strings search:

```
{
'prefix':"Fac"
}
```
The result is then:

```
{
    "results": [
        "Facebook",
        "Facebook Lite",
        "Facebook Pages Manager"
    ],
    "total": 3
}
```

## Tests
A simple test was implemented using unittest.

