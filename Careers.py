from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import sqlite3 as lite
import sys
 
@app.route("/")
def view_all_careers():
	
	con = lite.connect("careers.db")
	cur = con.cursor()
	cur.execute("select name, salary, growth, employment from careers")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/addcareers", methods=["GET", "POST"])
def add_careers():

	if request.method == "GET":
		return render_template("addcareers.html", **locals())

	else:
		name = request.form["name"]
		salary = request.form["salary"]
		growth = request.form["growth"]
		employment = request.form["employment"]

		con = lite.connect("careers.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into careers (name, salary, growth, employment) values ('{}', '{}')".format(name, salary, growth, employment))

		return redirect("/")


@app.route("/careers/<int:id>")
def get_careers(id):

	con = lite.connect("careers.db")
	cur = con.cursor()
	cur.execute("select name, salary, growth, employment from careers where id = " + str(id))
	rows = cur.fetchall()

	return render_template("viewcareers.html", **locals())

if __name__ == "__main__":
    app.run()
