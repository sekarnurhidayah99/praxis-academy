@app.route('/hi/<name>')
def say_hi(name):
    return 'Hello, %s!' % (name)

@app.route('/age/<int:age>')
def show_age(age):
    return 'Age is %d!' % (age)