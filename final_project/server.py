import json
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.englishToFrench(textToTranslate) # Write your code here
    return "englishText"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.frenchToEnglish(textToTranslate) # Write your code here
    return "frenchText"

@app.route("/")
def renderIndexPage():
    return render_template("index.html") # the code to renders the default homepage

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
