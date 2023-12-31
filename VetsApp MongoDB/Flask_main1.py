# Flask Web App :)
# HTML Tutorial -> https://www.w3schools.com/html/
# Bootstrap tutorial -> https://www.w3schools.com/bootstrap5/index.php/index.php
from flask import *
import datetime
from MongoDBHelperC import MongoDBHelper
import hashlib
web_app = Flask("Vets App")
@web_app.route("/")
def index():
    # return "This is Amazing. Its: {}".format(datetime.datetime.today())
    return render_template('index.html')
@web_app.route("/register")
def register():
    return render_template('register.html')


@web_app.route("/home")
def home():
    return render_template('Home.html', email=session['vet_email'])


@web_app.route("/register-vet", methods=['POST'])
def register_vet():

    vet_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
        'createdOn': datetime.datetime.today()
    }
    print(vet_data)
    db = MongoDBHelper(collection="vets")
    db.insert(vet_data)

    #return render_template('Home.html')
    return render_template('Home.html', email=session['vet_email'])


@web_app.route("/add-customer", methods=['POST'])
def add_customer():

    # if len(session['vet_id']) == 0:
    #     return redirect("/")

    customer_data = {
        'name': request.form['name'],
        'phone': request.form['phone'],
        'email': request.form['email'],
        'age': int(request.form['age']),
        'gender': request.form['gender'],
        'address': request.form['address'],
        'vet_id': session['vet_id'],
        'vet_email': session['vet_email'],
        'createdOn': datetime.datetime.today()
    }

    if len(customer_data['name']) == 0 or len(customer_data['phone']) == 0 or len(customer_data['email']) == 0:
        return render_template('error.html', message="Name, Phone and Email cannot be Empty")

    print(customer_data)
    db = MongoDBHelper(collection="Customer")
    db.insert(customer_data)

    return render_template('success.html', message="{} added successfully".format(customer_data['name']))


@web_app.route("/login-vet", methods=['POST'])
def login_vet():
    vet_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }
    print(vet_data)
    db = MongoDBHelper(collection="vets")
    documents = list(db.fetch(vet_data))
    print(documents, type(documents))
    if len(documents) == 1:
        #return render_template('home.html')
        session['vet_id'] = str(documents[0]['_id'])
        session['vet_email'] = documents[0]['email']
        session['vet_name'] = documents[0]['name']
        print(vars(session))
        return render_template('home.html', email=session['vet_email'], name=session['vet_name'])
    else:
        return render_template('error.html')


@web_app.route("/logout")
def logout():
    session['vet_id'] = ""
    session['vet_email'] = ""
    return redirect("/")


def main():
    # In order to use session object in flask, we need to set some key as secret_key in app
    web_app.secret_key = 'vetsapp-key-1'
    web_app.run()

if __name__ == '__main__':
    main()