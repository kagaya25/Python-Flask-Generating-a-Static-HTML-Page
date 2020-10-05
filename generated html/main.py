from flask import render_template
import flask

app = flask.Flask('my app')

if __name__ == "__main__":
    with app.app_context():
        rendered = render_template('blog.html', \
            title = "My Generated Page", \
            people = [{"name": "kagaya"}, {"name": "john"}])
        print(rendered)