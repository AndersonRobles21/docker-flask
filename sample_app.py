from flask import Flask, request, render_template

sample = Flask(__name__)

@sample.route("/")
def home():
    return "Aplicación funcionando", 200

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=False)