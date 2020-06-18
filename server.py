from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# updates for all html pages
@app.route('/<string:page_name>')
def page(page_name=None):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',mode='a',newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"] 
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('./thankyou.html')
		except:
			return 'It did not save to database'
	else:
		return 'somehing went wrong try again'


'''
# default server method for all pages

@app.route('/index.html')
def my_home_page():
    return render_template('index.html')

@app.route('/works.html')
def works_page():
    return render_template('works.html')

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/contact.html')
def contact_page():
	return render_template('contact.html')

# components is for html formats, do not display
@app.route('/components.html')
def components_page():
	return render_template('components.html')
'''

