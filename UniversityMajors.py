@app.route("/")
def view_all_universitymajors():
	
	con = lite.connect("universitymajors.db")
	cur = con.cursor()
	cur.execute("select university, major from universitymajors")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/adduniversitymajors", methods=["GET", "POST"])
def add_universitymajors():

	if request.method == "GET":
		return render_template("adduniversitymajors.html", **locals())

	else:
		university = request.form["university"]
		major = request.form["major"]

		con = lite.connect("universitymajors.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into universitymajors (university, major) values ('{}', '{}')".format(university, major))

		return redirect("/")


@app.route("/universitymajors/<int:id>")
def get_universitymajors(id):

	con = lite.connect("universitymajors.db")
	cur = con.cursor()
	cur.execute("select id university, major from universitymajors where id = " + str(id))
	rows = cur.fetchall()

	return render_template("viewuniversitymajors.html", **locals())