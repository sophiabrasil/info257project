from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import sqlite3 as lite
import sys
 
@app.route("/")
def view_all_applications():
	
	con = lite.connect("applications.db")
	cur = con.cursor()
	cur.execute("select university, major, degree, decision, decision_method, ug_gpa, gre_verbal, gre_quant, gre_writing from applications")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/addapplications", methods=["GET", "POST"])
def add_applications():

	if request.method == "GET":
		return render_template("addapplications.html", **locals())

	else:
		university = request.form["university"]
		major = request.form["major"]
		degree = request.form["degree"]
		decision = request.form["decision"]
		decision_method = request.form["decision_method"]
		ug_gpa = request.form["ug_gpa"]
		gre_verbal = request.form["gre_verbal"]
		gre_quant = request.form["gre_quant"]
		gre_writing = request.form["gre_writing"]

		con = lite.connect("applications.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into applications (university, major, degree, decision, decision_method, ug_gpa, gre_verbal, gre_quant, gre_writing) values ('{}', '{}')".format(university, major, degree, decision, decision_method, ug_gpa, gre_verbal, gre_quant, gre_writing))

		return redirect("/")


@app.route("/applications/<int:id>")
def get_applications(id):

	con = lite.connect("applications.db")
	cur = con.cursor()
	cur.execute("select university, major, degree, decision, decision_method, ug_gpa, gre_verbal, gre_quant, gre_writing from applications where id = " + str(id))
	rows = cur.fetchall()

	return render_template("viewapplications.html", **locals())

if __name__ == "__main__":
    app.run()
