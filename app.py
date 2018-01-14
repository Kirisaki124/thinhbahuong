
from flask import Flask, render_template
from flask import Flask, render_template,request,redirect,url_for
from random import choice
from models.info import Customer


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/pay')
def pay():
    return render_template('pay.html')

@app.route('/form', methods = ["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        phone = form['phone']
        address = form['address']
        email = form['email']
        message = form['message']
        package = form['package']
        new_order = Customer(package = package,name = name,phone = phone, address = address, email = email, message = message)
        new_order.save()
        return render_template('thankyou.html')

if __name__ == '__main__':
  app.run(debug=True)
