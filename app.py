#!/usr/bin/env python3
from flask import Flask, render_template, request,json
app = Flask(__name__, static_url_path='/static')



@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')



@app.route("/demo_input" , methods=['GET', 'POST'])
def demo_input():
    if request.method == 'POST':
        return render_template('demo_audio.html')
    else:
        return render_template('demo_input.html')
        #return "Nhan"



if __name__ == "__main__":
    app.run(port=5011)

