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


@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/pay')
def pay():
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
        new_order = Customer(name = name,phone = phone, address = address, email = email, note = note)
        # new_order.save()
        return redirect(url_for('send_email'))

@app.route('/form_package', methods = ["GET","POST"])
def form_package():
    if request.method == "GET":
        return render_template('pay/form_package.html')
    elif request.method == "POST":
        form = request.form
        packages = []
        for package in form.values():
            packages.append(package)
        session['packages'] = packages
        return redirect(url_for('pay', package = package))


@app.route('/thankyou/<service_id>')
def send_email(service_id):
    customer_id = Customer.objects().with_id(service_id)
    content = '''     '''
    gmail = GMail('thinhbahuong@gmail.com','123@123a')
    msg = Message('Test Message',to = customer_id.email, html = content)
    # msg = Message("Test message", to = "kirisaki124@yahoo.com", html = content)
    gmail.send(msg)
    return 'thank you'
if __name__ == '__main__':
  app.run(debug=True)
