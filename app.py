from flask import Flask, render_template,request,redirect,url_for,session
from models.customer_info import Customer,Service_Package
from gmail import GMail,Message
from mlab import mlab_connect


app = Flask(__name__)
app.config["SECRET_KEY"] = "falsdkfjlskjfw"
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/service', methods = ["GET","POST"])
def service():
    if request.method == "GET":
        return render_template('service.html')
    elif request.method == "POST":
        form = request.form
        packages = {}
        for key, value in form.items():
            packages[key] = value
        session['packages'] = packages
        print(packages)

        return redirect(url_for('pay', packages = packages))

@app.route('/pay')
def pay():
    packages = session
    return render_template('pay.html')

@app.route('/form_customer', methods = ["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('pay/form_customer.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        phone = form['phone']
        address = form['address']
        email = form['email']
        note = form['note']
        new_order = Customer(name = name, phone = phone, address = address, email = email, note = note)
        # new_order.save()
        return redirect(url_for('send_email'))


@app.route('/thankyou')
def send_email():
    html = open('templates/mail.html').read()
    gmail = GMail('thinhbahuong@gmail.com','123@123a')
    msg = Message('Test Message', to = "damsontung124@gmail.com", html = html)
    gmail.send(msg)
    return render_template('mail.html')

if __name__ == '__main__':
  app.run(debug=True)
