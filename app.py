from flask import Flask,render_template,request
import os

app = Flask(__name__)

import openai

openai.api_key = os.getenv('OPENAI_API_KEY’)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        response = openai.Image.create(prompt=t,n=1)
        image_url = response['data'][0]['url']
        print(image_url)
        return(render_template("index.html",result=image_url))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()
