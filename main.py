from flask import Flask, render_template, request  
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

import bitcoin as byc
@app.route('/create')
def do_create():
    return byc.random_key()

@app.route('/doGet')
def do_get():
    prik = request.args['prik']
    cmd = request.args['cmd']
    if cmd == 'toPrikComp':
        return prik + '01'
    elif cmd == 'toPubk':
        return byc.privkey_to_pubkey(prik)
## Hw2: Implements the rests of 'cmd'.
#--------------------------------------------------

if __name__ == '__main__':
    app.run(port=8080, debug=True)


