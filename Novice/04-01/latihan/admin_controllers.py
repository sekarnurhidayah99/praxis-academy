from flask import Flask, Response, render_template, redirect, request, url_for, flash

from wtforms import Form, CreateAuthorForm, db
admin = Flask(__name__, template_folder='templates')

@admin.route('/author/create', methods = ['GET', 'POST'])
def create_author():
    form = CreateAuthorForm(request.form)
    if request.method == 'POST' and form.validate():
        author = Author(form.names.data)
        db.session.add(author)
        db.session.commit()
        flash('Author successfully created.')

        return redirect(url_for('main.display_authors'))

    return render_template('create_author.htm', form=form)
if __name__ == '__main__':
    admin.run(debug=True)
    