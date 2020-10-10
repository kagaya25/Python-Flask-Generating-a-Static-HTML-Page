from flask import Flask

from flask import render_template


app = Flask(__name__)
@app.route('/')
def hello_world():
   return render_template('blog/blog.html')
   
if __name__ == "__main__":
    with app.app_context():
        rendered = render_template('blog.html', \
            title = "My Generated Page", \
            people = [{"name": "kagaya"}, {"name": "john"}])
        lines = []

        with open('templates/blog/blog.html', 'w') as f:
        	f.write(rendered)
    app.run(debug = True,port=4000)
	
		


		