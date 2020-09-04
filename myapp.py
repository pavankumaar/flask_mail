from flask import Flask, render_template, redirect,request
import smtplib, ssl

application = app = Flask(__name__)

def send_mail(sender,password,receiver,message):
	smtp_server = 'smtp.gmail.com'
	port = 587
	context = ssl.create_default_context()
	# with smtplib.SMTP_SSL(smtp_server,port,context = context) as server:
	# 	server.login(sender,password)
	# 	server.sendmail(sender,receiver,message)
	server = smtplib.SMTP(smtp_server, port)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(sender,password)
	server.sendmail(sender,receiver,message)
	server.close()
	return True

@app.route('/')
@app.route('/' ,methods=['GET','POST'])
def index():
	# if request.method == 'POST':
	# 	sender = request.form['sender']
	# 	password = request.form['password']
	# 	receiver = request.form['receiver']
	# 	message = request.form['message']

	# 	if sender != None:
	# 		result = send_mail(sender,password,receiver,message)
	# 		# if result == 'success':
	# 		# 	return render_template('mail.html',success = result)
	# 		# else:
	# 		# 	return render_template('mail.html',error = result)

	# 		return render_template('mail.html')
			
	return render_template('mail.html')

if __name__ == '__main__':
	app.run(debug=True)