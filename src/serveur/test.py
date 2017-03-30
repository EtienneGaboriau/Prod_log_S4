from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=10078, debug=True)
