from flask import Flask
from flask import render_template
from flask import request
from jinja2 import Template
import csv
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])

def hey_ya():
	if request.method == "GET":
		return render_template("index.html")
	elif request.method == "POST":
		para_one = request.form["ID"]
		para_two = request.form["id_value"]
		file = open('data.csv')
		data = csv.reader(file)
		rows = []
		possible = False
		for i in data:
			rows.append(i)
		file.close()
		if para_one=="Student ID":
			summ = sum(int(i[2]) for i in rows if i[0]==para_two)
			if summ != 0:
				possible = True
			avg,maxx = 0,0
		elif para_one=="Course ID":
			summ = 0
			marks = []
			for i in rows:
				if i[1].strip(" ") == para_two:
					marks.append(int(i[2].strip(" ")))
			if len(marks)!=0:
				avg = sum(marks)/len(marks)
				maxx = max(marks)
				'''plt.hist(marks)
				plt.xlabel("Marks")
				plt.ylabel("Frequency")
				plt.savefig("static/image.png")'''
				possible = True
			else:
				avg,maxx = 0,0
		else:
			summ,avg,maxx = 0,0,0
		
		return render_template("student.html",para_one = para_one, para_two = para_two, rows = rows, sum = summ, avg = avg, maxx = maxx, possible = possible)
	else:
		print("Error check")



if __name__ == "__main__":
	app.debug = True
	app.run()





