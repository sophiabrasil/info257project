""" Table Name: universities
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'name', 'TEXT', 0, None, 0)
(2, 'ug_admissions_rate', 'TEXT', 0, None, 0)
(3, 'size', 'TEXT', 0, None, 0)
(4, 'in_state_tuition', 'TEXT', 0, None, 0)
(5, 'out_state_tuition', 'TEXT', 0, None, 0)
(6, 'state', 'TEXT', 0, None, 0)
(7, 'city', 'TEXT', 0, None, 0)


Table Name: majors
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'name', 'TEXT', 0, None, 0)
(2, 'description', 'TEXT', 0, None, 0)
(3, 'average_salary', 'TEXT', 0, None, 0)
(4, 'expected_growth', 'TEXT', 0, None, 0)
(5, 'no_of_students', 'TEXT', 0, None, 0)
(6, 'no_of_offering_schools', 'TEXT', 0, None, 0)


Table Name: cities
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'state', 'TEXT', 0, None, 0)
(2, 'city', 'TEXT', 0, None, 0)
(3, 'summer_temperature', 'TEXT', 0, None, 0)
(4, 'winter_temperature', 'TEXT', 0, None, 0)


Table Name: careers
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'name', 'TEXT', 0, None, 0)
(2, 'salary', 'TEXT', 0, None, 0)
(3, 'growth', 'TEXT', 0, None, 0)
(4, 'employment', 'TEXT', 0, None, 0)


Table Name: majorcareers
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'major', 'TEXT', 0, None, 0)
(2, 'career', 'TEXT', 0, None, 0)


Table Name: universitymajors
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'university', 'TEXT', 0, None, 0)
(2, 'major', 'TEXT', 0, None, 0)


Table Name: applications
(0, 'index', 'INTEGER', 0, None, 0)
(1, 'university', 'TEXT', 0, None, 0)
(2, 'major', 'TEXT', 0, None, 0)
(3, 'degree', 'TEXT', 0, None, 0)
(4, 'decision', 'TEXT', 0, None, 0)
(5, 'decision_method', 'TEXT', 0, None, 0)
(6, 'ug_gpa', 'REAL', 0, None, 0)
(7, 'gre_verbal', 'REAL', 0, None, 0)
(8, 'gre_quant', 'REAL', 0, None, 0)
(9, 'gre_writing', 'REAL', 0, None, 0) """

from flask import Flask
from flask import render_template
import os
import sqlite3 as lite
import sys
from os import path
app = Flask(__name__)

@app.route('/')
def view_all_books():
	
	con = lite.connect("info257app.db")
	cur = con.cursor()
	cur.execute("select * from cities")
	rows = cur.fetchall()
	print(rows)
	return render_template("home.html")
# def home():
#     return render_template("home.html")

@app.route('/majors/<int:id>')
def get_major(id):
    return render_template("major.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

extra_dirs = ['static',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)
app.run(extra_files=extra_files)
