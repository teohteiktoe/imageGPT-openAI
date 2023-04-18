from flask import Flask,render_template,request
import replicate,os

app = Flask(__name__)

import openai

openai.api_key = "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"

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
