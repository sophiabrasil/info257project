@app.route("/")
def view_all_majorcareers():
	
	con = lite.connect("majorcareers.db")
	cur = con.cursor()
	cur.execute("select major, career from majorcareers")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/addmajorcareers", methods=["GET", "POST"])
def add_majorcareers():

	if request.method == "GET":
		return render_template("addmajorcareers.html", **locals())

	else:
		major = request.form["major"]
		career = request.form["career"]

		con = lite.connect("majorcareers.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into majorcareers (major, career) values ('{}', '{}')".format(major, career))

		return redirect("/")


@app.route("/majorcareers/<int:id>")
def get_majorcareers(id):

	con = lite.connect("majorcareers.db")
	cur = con.cursor()
	cur.execute("select id major, career from majorcareers where id = " + str(id))
	rows = cur.fetchall()

	return render_template("viewmajorcareers.html", **locals())