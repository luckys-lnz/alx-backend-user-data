# 0x03. User authentication service

## Flask API Basics

### This README explains how to:

- Declare API routes in a Flask app.
- Get and set cookies.
- Retrieve form data from requests.
- Return various HTTP status codes.

## Setup

```
pip install flask
```

Create a file named app.py for your Flask application.

**Declaring API Routes**

In Flask, API routes are declared using decorators like @app.route().

```
from flask import Flask

app = Flask(__name__)

@app.route('/example', methods=['GET'])
def example():
    return "Hello, World!"
```

Methods: Specify HTTP methods using the methods parameter (e.g., ['GET', 'POST'])

```
@app.route('/submit', methods=['POST'])
def submit_data():
    return "Data submitted!"
```

## Working with Cookies

**Setting a Cookie**

Use the make_response function to set cookies.

```
from flask import make_response

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie has been set!")
    response.set_cookie('username', 'JohnDoe')
    return response
```

**Getting a Cookie**

Use request.cookies to retrieve a cookie.

```
from flask import request

@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f"Username is {username}"
```

**Retrieving Request Form Data**

Use request.form to retrieve data from a form sent via a POST request.

```
from flask import request

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Name: {name}, Email: {email}"
```

Ensure the form uses POST as the method and includes Content-Type: application/x-www-form-urlencoded.


**Returning HTTP Status Codes**

You can return status codes along with a response using a tuple.
```
@app.route('/not-found')
def not_found():
    return "This resource was not found", 404
```

**Common Status Codes:**

- 200 OK: Request succeeded.
- 201 Created: Resource created.
- 400 Bad Request: Invalid request.
- 404 Not Found: Resource not found.
- 500 Internal Server Error: Server encountered an error.


##  Example App
```
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie has been set!")
    response.set_cookie('username', 'JohnDoe')
    return response

@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f"Username is {username}"

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Name: {name}, Email: {email}"

@app.route('/not-found')
def not_found():
    return "This resource was not found", 404

if __name__ == '__main__':
    app.run(debug=True)
```
- Save the code in a file called app.py
- Run the flask app with:
```
python3 app.py
```
- Open your browser or use tools like Postman to interact with the endpoints.

**Test the api with:**

1. Set a Cookie:
Visit /set-cookie in your browser to set a cookie.

2. Get a Cookie:
Visit /get-cookie to retrieve the cookie.

3. Submit Form Data:
Use a tool like Postman to send a POST request with form data to /submit-form.

4. Return Status Code:
Visit /not-found to see a 404 Not Found response.