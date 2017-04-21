@app.route("/")
def view_all_cities():
	
	con = lite.connect("cities.db")
	cur = con.cursor()
	cur.execute("select state, city, summer_temperature, winter_temperature")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/addcities", methods=["GET", "POST"])
def add_cities():

	if request.method == "GET":
		return render_template("cities.html", **locals())

	else:
		state = request.form["city"]
		city = request.form["state"]
		summer_temperature = request.form["summer_temperature"]
		winter_temperature = request.form["winter_temperature"]

		con = lite.connect("cities.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into cities (state, city, summer_temperature, winter_temperature) values ('{}', '{}')".format(state, city, summer_temperature, winter_temperature)

		return redirect("/")


@app.route("/cities/<int:id>")
def get_cities(id):

	con = lite.connect("cities.db")
	cur = con.cursor()
	cur.execute("select state, city, summer_temperature, winter_temperature from cities where id = " + str(id))
	rows = cur.fetchall()

	return render_template("viewcities.html", **locals())