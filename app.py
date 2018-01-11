from flask import Flask, render_template
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
if __name__ == '__main__':
  app.run(debug=True)
