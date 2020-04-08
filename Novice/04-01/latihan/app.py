from flask import Flask, render_template, abort, request
from flask.views import View
from flask.views import MethodView
app = Flask(__name__, template_folder='templates')

class MyRequest(View):
    methods = ['POST']
  
    def dispatch_request(self):
        # request.method == 'POST'
        name = request.form.get('name', 'Damyan')
        return 'Hello, %s!' % name

app.add_url_rule(
    '/say-hi', view_func=MyRequest.as_view('my_request')
)



if __name__ == '__main__':
    app.run(debug=True)