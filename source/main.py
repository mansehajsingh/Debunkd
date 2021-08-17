from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route("/verify", methods=['GET'])
def verifypage():
    return render_template('verify.html')

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()