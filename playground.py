from os import times
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/')  # I can have multiple routes stacked on top of each other.
@app.route('/play/<int:times>')
@app.route('/play/<int:times>/<string:color>')
def play(times=3,color='blue'):
    return render_template('index.html', times=times, color=color) 

if __name__=="__main__":
    app.run(debug=True)
