@app.route("/")
def view_all_majors():
	
	con = lite.connect("majors.db")
	cur = con.cursor()
	cur.execute("select name, description, average_salary, expected_growth, no_of_students, no_of_offering_schools from majors")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/addmajorcareers", methods=["GET", "POST"])
def add_majors():

	if request.method == "GET":
		return render_template("addmajors.html", **locals())

	else:
		name = request.form["name"]
		description = request.form["description"]
		average_salary = request.form["average_salary"]
		expected_growth = request.form["expected_growth"]
		no_of_students = request.form["no_of_students"]
		no_of_offering_schools = request.form["no_of_offering_schools"]

		con = lite.connect("majors.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into Majors (name, description, average_salary, expected_growth, no_of_students, no_of_offering_schools) values ('{}', '{}')".format(name, description, average_salary, expected_growth, no_of_students, no_of_offering_schools))

		return redirect("/")


@app.route("/majors/<int:id>")
def get_majors(id):

	con = lite.connect("majors.db")
	cur = con.cursor()
	cur.execute("select id name, description, average_salary, expected_growth, no_of_students, no_of_offering_schools from majors where id = " + str(id))
	rows = cur.fetchall()

	return render_template("viewmajors.html", **locals())