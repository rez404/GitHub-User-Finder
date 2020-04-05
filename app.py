from flask import Flask, render_template,request
import requests

app = Flask(__name__)
url= "https://api.github.com/users/"

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=="POST":
        username=request.form.get("username")
        data=requests.get(url+username)
        djson=data.json()

        return render_template('index.html',djson=djson)
    else:
        return render_template('index.html',djson="Not Found")

if __name__ == '__main__':
  app.run(debug=True)
 