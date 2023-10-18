# Flask Language Translator Web Application

This Flask web application utilizes the IBM Watson Language Translator service to provide language translation features. The application allows users to translate text from English to French and from French to English. Here's how to use it:

## Prerequisites

Before running the Flask application, make sure you have the following prerequisites:

- IBM Watson Language Translator API Key
- IBM Watson Language Translator Service URL
- Python 3.x
- Required Python packages (install with `pip`):
  - `ibm-watson`
  - `flask`
  - `python-dotenv`

You'll also need to create a `.env` file in the same directory as your Flask app with the following content:

```bash
apikey=YOUR_IBM_WATSON_API_KEY
url=YOUR_IBM_WATSON_SERVICE_URL
SECRET_KEY=YOUR_SECRET_KEY
```


Replace YOUR_IBM_WATSON_API_KEY and YOUR_IBM_WATSON_SERVICE_URL with your IBM Watson credentials, and YOUR_SECRET_KEY with a secure secret key for your Flask app.

## Installation and Usage


Clone or download this repository.

Install the required Python packages using pip:

```bash
pip install ibm-watson flask python-dotenv
```


Run the Flask app:
```bash
flask run
```
Access the web application in your web browser at http://localhost:5000.

## Features

English to French Translation
Enter English text in the input box.
Click the "Translate to French" button.
The translated text will be displayed.
French to English Translation
Enter French text in the input box.
Click the "Translate to English" button.
The translated text will be displayed.

## Support and Contributions
If you encounter any issues, have suggestions for improvements, or would like to contribute, please open an issue or create a pull request in this project's repository.





