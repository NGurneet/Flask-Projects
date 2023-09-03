from flask import *
from MongoDB_Helper import MongoDBHelper
import datetime
import hashlib
from bson.objectid import ObjectId

ol_app = Flask("Teja Singh & Sons")
@ol_app.route("/")
def index():
    #return "Hello Ji"
    return render_template("index.html")

@ol_app.route("/register")
def register():
    return render_template('register.html')

@ol_app.route("/register-user",methods =["POST"])

def register_user():

    ind_user_data = {
        'name': request.form['name'],
        'email' : request.form['email'].lower(),
        'firm_name': (request.form['firm_name'].upper()),
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
        'createdOn': datetime.datetime.today()
    }
    print(ind_user_data)
    db = MongoDBHelper(collection='ind_user')
    db.insert(ind_user_data)

    return render_template('index.html',firm_name = request.form['firm_name'],email=request.form['email'], name=request.form['name'])

@ol_app.route("/login-ind-user", methods=['POST'])
def login_ind_user():
    ind_user_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }
    print(ind_user_data)
    db = MongoDBHelper(collection="ind_user")
    documents = list(db.fetch(query = ind_user_data))
    print(documents, type(documents))
    if len(documents) == 1:


        session['ind_user_id'] = str(documents[0]['_id'])
        session['ind_user_firm_name'] = documents[0]['firm_name']
        session['ind_user_email'] = documents[0]['email']
        session['ind_user_name'] = documents[0]['name']
        print(vars(session))
        return render_template('home.html',firm_name = session['ind_user_firm_name'], email=session['ind_user_email'], name=session['ind_user_name'])
    else:
        return render_template('error.html')

@ol_app.route("/logout")
def logout():
    session['ind_user_id'] = ""
    session['ind_user_email'] = ""
    return redirect("/")

@ol_app.route("/place-order" , methods = ["POST"])
def place_order():

    order_data = {
        'firm_name': request.form['firm_name'].upper(),
        'customer_name': request.form['customer_name'],
        'phone': request.form['phone'].strip(' '),
        'product': request.form['product'],
        'order_type': request.form['order_type'],
        'order_specification': request.form['order_specification'],
        'address': request.form['address'],

        'order_status': request.form['order_status'],
        'services': request.form['services'],
        'ind_user_email': session['ind_user_email'],
        'ind_user_id': session['ind_user_id'],
        'ind_user_firm_name': session['ind_user_firm_name'],
        'createdOn': datetime.datetime.today()
    }
    if len(order_data['order_specification'])==0:
        order_data['order_specification']= "None"
    print(order_data)
    db = MongoDBHelper(collection='orders')
    db.insert(order_data)

    return render_template('success.html', message=" Order Placed for {}".format(order_data['firm_name']))

@ol_app.route('/home')
def place_order_page():
    return render_template('home.html', firm_name=session['ind_user_firm_name'], email=session['ind_user_email'],
                           name=session['ind_user_name'])
@ol_app.route("/fetch-all-orders")
def fetch_orders_of_ind_user():
    db = MongoDBHelper(collection='orders')
    query = {'ind_user_firm_name':session['ind_user_firm_name']}
    #query = {'_id': session['vet_id']}
    documents = (db.fetch(query))
    print(documents,type(documents))
    #return "Data Printed"
    return render_template('orders.html',firm_name = session['ind_user_firm_name'], email=session['ind_user_email'], name=session['ind_user_name'], documents=documents)

@ol_app.route("/fetch-pending-orders")
def fetch_pending_orders_of_ind_user():
    db = MongoDBHelper(collection='orders')
    query = {'ind_user_firm_name':session['ind_user_firm_name'],'order_status':'Pending'}
    #query = {'_id': session['vet_id']}
    documents = (db.fetch(query))
    
    print(documents,type(documents))
    #return "Data Printed"
    return render_template('pending_orders.html',firm_name = session['ind_user_firm_name'], email=session['ind_user_email'], name=session['ind_user_name'], documents=documents)


@ol_app.route("/fetch-fulfilled-orders")
def fetch_fulfilled_orders_of_ind_user():
    db = MongoDBHelper(collection='orders')
    query = {'ind_user_firm_name': session['ind_user_firm_name'], 'order_status': 'Done'}
    # query = {'_id': session['vet_id']}
    documents = (db.fetch(query))

    print(documents, type(documents))
    # return "Data Printed"
    return render_template('fulfilled_orders.html', firm_name=session['ind_user_firm_name'], email=session['ind_user_email'],
                           name=session['ind_user_name'], documents=documents)

@ol_app.route("/update-order/<id>")
def update_order(id):
    db = MongoDBHelper(collection='orders')
    query = {'_id': ObjectId(id)}
    order = db.fetch(query=query)[0]
    #return "Order Updated"
    return render_template('update order.html',
                          message="Order for Firm Name {} Updated Successfully".format(id, order['firm_name']), firm_name=session['ind_user_firm_name'], email=session['ind_user_email'],
                        name=session['ind_user_name'],order = order, order_id = ObjectId(id))

@ol_app.route("/update-order-in-db/<id>" , methods = ["POST"])
def update_order_in_db(id):

    order_data_to_update = {
        'firm_name': request.form['firm_name'],
        'customer_name': request.form['customer_name'],
        'phone': request.form['phone'],
        'product': request.form['product'],
        'order_type': request.form['order_type'],
        'order_specification': request.form['order_specification'],
        'address': request.form['address'],
        'order_status': request.form['order_status'],
        'services': request.form['services'],


    }
    print(order_data_to_update)
    db = MongoDBHelper(collection='orders')
    query = {'_id': ObjectId(id)}
    db.update(order_data_to_update,query)

    return render_template('success.html', message="Order for {} Updated successfully".format(order_data_to_update['firm_name']))

@ol_app.route("/searchbar-order-post",methods = ["POST"])
def search_customer():
    db =MongoDBHelper(collection='orders')
    query = {'firm_name':request.form['firm_name'].upper(), 'ind_user_firm_name': session['ind_user_firm_name']}
    #query = db.users.find({ name: { $regex: "john", $options: "i" } })

    orders = db.fetch(query)

    if len(orders)>=1:
        order = orders[0]
        print(order)
        #return "Found the Customer with name: {}".format(order['firm_n<<>ame'])
        return render_template("firm_profile.html",firm_name=session['ind_user_firm_name'], email=session['ind_user_email'],
                           name=session['ind_user_name'], order=order)
    else:
        return render_template("error.html",message = "Customer Not Found")
@ol_app.route("/place-order/<firm_name>")
def place_order_for_firm(firm_name):
    db = MongoDBHelper(collection='orders')
    query = {'firm_name': firm_name, 'ind_user_firm_name': session['ind_user_firm_name']}
    firm = db.fetch(query)
    if len(firm)==1:
        firm = firm[0]
    #return "Place Order "
    return render_template('order_for_firm.html',firm_name = session['ind_user_firm_name'], email=session['ind_user_email'], name=session['ind_user_name'],buyer_firm = firm_name,firm_address = firm)

@ol_app.route("/fetch-orders/<firm_name>")
def fetch_orders_of_firm(firm_name):
    db = MongoDBHelper(collection='orders')
    query = {'ind_user_firm_name':session['ind_user_firm_name'],'firm_name' : firm_name}
    #query = {'_id': session['vet_id']}
    documents = (db.fetch(query))
    print(documents,type(documents))
    #return "Data Printed"
    return render_template('orders.html',firm_name = session['ind_user_firm_name'], email=session['ind_user_email'], name=session['ind_user_name'], documents=documents)

@ol_app.route("/delete-order/<id>")
def delete_order(id):
    db = MongoDBHelper(collection='orders')
    query = {'_id': ObjectId(id)}
    order = db.fetch(query=query)[0]
    db.delete(query)
    return render_template('success.html', message=" Order no {} Deleted for {}".format(id,order['firm_name']))

@ol_app.route("/order-fulfilled/<id>")
def done_order(id):
    order_status = {
        'order_status': 'Done'
    }
    db = MongoDBHelper(collection='orders')
    query = {'_id': ObjectId(id)}

    order = db.fetch(query=query)[0]
    db.update(order_status,query)
    return render_template('success.html', message=" Order Status updated for {}".format(id,order['firm_name']))

def main():

    ol_app.secret_key = "OrderLogix-1"
    ol_app.run(port=5005)

if __name__ =="__main__":
    main()