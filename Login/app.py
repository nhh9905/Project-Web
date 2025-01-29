from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def home():
    return render_template("login.html")
    
@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/forgotpass.html')
def forgotpass():
    return render_template("forgotpass.html")

@app.route('/web.html')
def web():
    return render_template("web.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1234)