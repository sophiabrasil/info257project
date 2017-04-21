@app.route("/")
def view_all_universities():
	
	con = lite.connect("info257app.db")
	cur = con.cursor()
	cur.execute("select name, ug_admissions_rate, size, in_state_tuition, out_state_tuition, state, city from universities")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/adduniversities", methods=["GET", "POST"])
def add_universities():

	if request.method == "GET":
		return render_template("adduniversities.html", **locals())

	else:
		name = request.form["name"]
		ug_admissions_rate = request.form["ug_admissions_rate"]
		size = request.form["size"]
		in_state_tuition = request.form["in_state_tuition"]
		out_state_tuition = request.form["out_state_tuition"]
		city = request.form["city"]
		state = request.form["state"]

		con = lite.connect("info257app.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into universities (name, ug_admissions_rate, size, in_state_tuition, out_state_tuition, state, city) values ('{}', '{}')".format(name, ug_admissions_rate, size, in_state_tuition, out_state_tuition, state, city))

		return redirect("/")


@app.route("/universities/<int:id>")
def get_universities(id):

	con = lite.connect("info257app.db")
	cur = con.cursor()
	cur.execute("select name, ug_admissions_rate, size, in_state_tuition, out_state_tuition, state, city from universities where id = " + str(id))
	rows = cur.fetchall()

	return render_template("viewuniversities.html", **locals())
