from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "ADMIN"
app.config["MYSQL_DB"] = "company"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/employees", methods=["GET"])
def get_employees():
    data = data_fetch("""select * from employee""")
    return make_response(jsonify(data), 200)


@app.route("/employees", methods=["POST"])
def add_employees():
    cur = mysql.connection.cursor()
    info = request.get_json()
    ssn = info["ssn"]
    Fname = info["Fname"]
    Minit = info["Minit"]
    Lname = info["Lname"]
    Bdate = info["Bdate"]
    Address = info["Address"]
    Sex = info["Sex"]
    Salary = info["Salary"]
    Super_ssn = info["Super_ssn"]
    DL_id = info["DL_id"]
    cur.execute(
        """ INSERT INTO employee (ssn, Fname, Minit, Lname, Bdate, Address, Sex, Salary, Super_ssn, DL_id) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (ssn, Fname, Minit, Lname, Bdate, Address, Sex, Salary, Super_ssn, DL_id),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor added successfully", "rows_affected": rows_affected}
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
