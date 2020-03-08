#!/usr/bin/env python3
from flask import Flask, render_template, request,json
app = Flask(__name__, static_url_path='/static')



@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('create.html')



@app.route("/demo" , methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        return render_template('demo.html')
    else:
        return render_template('demo.html')



if __name__ == "__main__":
    app.run(port=5011)

