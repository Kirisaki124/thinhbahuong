from flask import Flask, render_template,request,redirect,url_for,session
from models.customer_info import Customer,Service_Package
from gmail import GMail,Message
from mlab import mlab_connect
from sheettest import sheet

app = Flask(__name__)
app.config["SECRET_KEY"] = "falsdkfjlskjfw"
mlab_connect()
Customer = []
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
            Customer.append(value)
        session['packages'] = packages
        return redirect(url_for('pay', packages = packages))



@app.route('/pay', methods = ["GET","POST"])
def pay():
    packages = session['packages']
    if request.method == "GET":
        return render_template('pay.html', packages = packages)
    elif request.method == "POST":
        form = request.form
        for info in form.values():
            Customer.append(info)
        index = 1
        sheet.insert_row(Customer, index)
        # session.clear()
        return redirect(url_for('send_email'))
        # return redirect(url_for('send_email'))

# @app.route('/form_package', methods = ["GET","POST"])
# def form_package():
#     if request.method == "GET":
#         return render_template('pay/form_package.html')
#     elif request.method == "POST":
#         form = request.form
#         packages = []
#         for package in form.values():
#             packages.append(package)
#         session['packages'] = packages
#         return redirect(url_for('pay', package = package))
@app.route('/thankyou')
def send_email():
    # customer_id = Customer.objects().with_id(service_id)
    # packages = session['packages']
    content = open('templates/mail.html', encoding="utf8").read()
    gmail = GMail('thinhbahuong@gmail.com','123@123a')
    # msg = Message('Test Message',to = Customer[5], html = content)
    msg = Message("Test message", to = Customer[5], html = content)
    gmail.send(msg)
    return 'thank you'
if __name__ == '__main__':
  app.run(debug=True)
