from flask import Flask, make_response, jsonify, request, render_template
from flask_mysqldb import MySQL
from marshmallow import Schema, fields, ValidationError, EXCLUDE

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "ADMIN"
app.config["MYSQL_DB"] = "company"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


class EmployeeSchema(Schema):
    ssn = fields.String(required=True)
    Fname = fields.String(required=True)
    Minit = fields.String(required=True, validate=lambda x: len(x) == 1)
    Lname = fields.String(required=True)
    Bdate = fields.Date(required=True)
    Address = fields.String(required=True)
    Sex = fields.String(required=True, validate=lambda x: x in ["M", "F"])
    Salary = fields.Float(required=True)
    Super_ssn = fields.String(required=True)
    DL_id = fields.String(required=True)


employee_schema = EmployeeSchema()


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return make_response(jsonify(e.messages), 400)


@app.route("/search", methods=["GET"])
def search_page():
    return render_template("index.html")


@app.route("/search_employees", methods=["GET"])
def search_employees():
    search_query = request.args.get("query", "")
    if search_query:
        data = data_fetch(
            f"SELECT * FROM employee WHERE Fname LIKE '%{search_query}%' OR Lname LIKE '%{search_query}%'"
        )
    else:
        data = data_fetch("SELECT * FROM employee")
    return make_response(jsonify(data), 200)


@app.route("/employees", methods=["GET"])
def get_employees():
    data = data_fetch("""select * from employee""")
    return make_response(jsonify(data), 200)


@app.route("/employees", methods=["POST"])
def add_employees():
    cur = mysql.connection.cursor()
    try:
        info = employee_schema.load(request.get_json())
    except ValidationError as err:
        return make_response(jsonify(err.messages), 400)

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
            {"message": "employee added successfully", "rows_affected": rows_affected}
        ),
        201,
    )


@app.route("/employees/<int:ssn>", methods=["GET"])
def get_employee(ssn):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee WHERE ssn = %s", (ssn,))
    data = cur.fetchone()
    cur.close()
    print(data)  # Add this line
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response(jsonify({"message": "Employee not found"}), 404)


class EmployeeUpdateSchema(Schema):
    Fname = fields.String(required=True)
    Minit = fields.String(required=True, validate=lambda x: len(x) == 1)
    Lname = fields.String(required=True)
    Bdate = fields.Date(required=True)
    Address = fields.String(required=True)
    Sex = fields.String(required=True, validate=lambda x: x in ["M", "F"])
    Salary = fields.Float(required=True)
    Super_ssn = fields.String(required=True)
    DL_id = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE  # Ignore unknown fields in the request payload


employee_update_schema = EmployeeUpdateSchema()


@app.route("/employees/<int:ssn>", methods=["PUT"])
def update_employees(ssn):
    cur = mysql.connection.cursor()
    try:
        info = employee_update_schema.load(request.get_json())
    except ValidationError as err:
        return make_response(jsonify(err.messages), 400)

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
        """ UPDATE employee SET Fname = %s, Minit = %s, Lname = %s, Bdate = %s, Address = %s, Sex = %s, Salary = %s, Super_ssn = %s, DL_id = %s WHERE ssn = %s """,
        (Fname, Minit, Lname, Bdate, Address, Sex, Salary, Super_ssn, DL_id, ssn),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "employee updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/employees/<int:ssn>", methods=["DELETE"])
def delete_employees(ssn):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM employee where ssn = %s """, (ssn,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify({"message": " deleted successfully", "rows_affected": rows_affected}),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
