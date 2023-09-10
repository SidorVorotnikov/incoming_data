from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/query-example')
def query_example():   
  temp = request.args.get('t')
    #https://incomingdata.dbikkuzin.repl.co/query-example?language=Python
  hum = request.args.get('h')
    #jp;kim
  return '''<h1>The temperature top level value is: {}</h1>
            <h1>The temperature bottom level value is: {}</h1>'''.format(temp, hum)
@app.route('/form-example')
def form_example():
    return '''<h1>The language value is: {}</h1>
            <h1>The framework value is: {}</h1>'''.format(language, framework)

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=80)
