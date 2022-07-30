
from dbms import *
from flask import Flask, flash, render_template,request,redirect,session
from pymysql import *

app = Flask(__name__)
app.secret_key="abc"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# main counsumers

@app.route("/custom",methods=["POST"])
def customers():
    itemc=request.form['itemname']
    shopname,itemname=searchTable('shops',itemc)
    return render_template('customers.html',shopname=shopname,itemname=itemname)

@app.route("/custo")
def cust():
    i=it_me
    shopname,itemname=searchTable('shops',i)
    return render_template ('customers.html',shopname=shopname,itemname=itemname)

# main counsumer2

@app.route("/customer")
def customer():
    return render_template ('customer.html')

# signup customers

@app.route("/savelinkc",methods=["POST"])
def save_funcc():
    cust1_name=request.form['cust_name']
    cust1_pass=request.form['cust_pass']
    cust1_add=request.form['cust_add']
    insertTable1('shopping', 'cust_list' ,'cust_name', 'cust_pass', 'cust_add', cust1_name, cust1_pass, cust1_add)
    return redirect("customer")

# login customers

@app.route("/savelinklc",methods=["POST"])
def login_savec():
    if request.method=='POST' and 'cust_name' in request.form and 'cust_pass' in request.form:
        cust_name=request.form['cust_name']
        cust_pass=request.form['cust_pass']
        c=connect_shop('shopping')
        marker=c.cursor()
        marker.execute("select * from cust_list where cust_name='{}' AND cust_pass='{}';".format(cust_name,cust_pass))
        result=marker.fetchone()
        if result:
            session['k']=True
            return redirect("customer")
        else:
            return redirect("home")

# logout customers

@app.route('/logoutlinkc')
def logout_funcc():
    session.pop('name',None)
    session.pop('password',None)
    return redirect("home")


@app.route('/logoutlinkca')
def logout_funca():
    session.pop('name',None)
    session.pop('password',None)
    return redirect("home")


# main shops

@app.route("/shops")
def shops():
    infoshops=showTable('shops',shop)
    return render_template('shops.html',shname=shop,data=infoshops)

# signup shops

@app.route("/savelinks",methods=["POST"])
def save_funcs():
    if request.method=='POST' and 'shop_name' in request.form and 'shop_pass' in request.form:
        shop_name=request.form['shop_name']
        shop_pass=request.form['shop_pass']
        c=connect_shop('shopping')
        marker=c.cursor()
        marker.execute("select * from shop_list where shop_name='{}' AND shop_pass='{}'".format(shop_name,shop_pass))
        result=marker.fetchone()
        if result:
            session['k']=True
            return redirect("home")
        else:
            shop1_name=request.form['shop_name']
            shop1_pass=request.form['shop_pass']
            shop1_add=request.form['shop_add']
            global shop
            shop = shop1_name
            insertTable1('shopping', 'shop_list' ,'shop_name', 'shop_pass', 'shop_add', shop1_name, shop1_pass, shop1_add)
            createTable('shops',shop1_name)
        return redirect("shops")
    


# login shops

@app.route("/savelinkls",methods=["POST"])
def login_saves():
    if request.method=='POST' and 'shop_name' in request.form and 'shop_pass' in request.form:
        shop_name=request.form['shop_name']
        shop_pass=request.form['shop_pass']
        global shop
        shop=shop_name
        c=connect_shop('shopping')
        marker=c.cursor()
        marker.execute("select * from shop_list where shop_name='{}' AND shop_pass='{}'".format(shop_name,shop_pass))
        result=marker.fetchone()
        if result:
            session['k']=True
            return redirect("shops")
        else:
            return redirect("home")
        

# logout shops

@app.route('/logoutlinks')
def logout_funcs():
    session.pop('name',None)
    session.pop('password',None)
    return redirect("home")

# edit shops data

@app.route("/updatelink/<id>/<nm>",methods=["POST"])
def update_data(id,nm):
    new_count=request.form['buy']
    updateTable('shops',nm,new_count,id)
    #infoshops=showTable('shops',nm)
    return redirect ("/shops")

# add shop items

@app.route("/addlink/<id>",methods=["POST"])
def add_data(id):
    item=request.form['add_item']
    price=request.form['add_price']
    quantity=request.form['add_quantity']
    insertTable2('shops',id,item,price,quantity)
    return redirect ("/shops")

# edit counsumer items 

@app.route("/updatelink/<sh>/<it>/<int:c>",methods=["POST"])
def buy_data(sh,it,c):
    buy=request.form['buy']
    buy=int(buy)
    #global sh_me
    #sh_me=sh
    global it_me
    it_me=it
    if c>=buy:
        c=c-buy
        updateTable('shops',sh,c,it)
        return redirect ("/custo")
    else:
        return redirect ("/custo")

# about

@app.route("/about")
def abt():
    return render_template("about.html")

if __name__ =='__main__':
    app.run(debug=True)




