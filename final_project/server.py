import json
from machinetranslation import translator
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.englishToFrench(textToTranslate)   # calling the english to french translation function
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.frenchToEnglish(textToTranslate) # calling the french  to english translation function
    return englishText

@app.route("/")
def renderIndexPage():
   return render_template("index.html") # the code to render the default dislay page        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
