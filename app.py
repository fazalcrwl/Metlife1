from flask import Flask, request, render_template, redirect, url_for, send_file

from src.save_image import Store_img
st=Store_img('artifacts/data')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' has the form


def 

if __name__ == '__main__':
    app.run(debug=True)