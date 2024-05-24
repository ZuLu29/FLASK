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


if __name__ == "__main__":
    app.run(debug=True)
