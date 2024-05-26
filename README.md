Employee Management System
This project is a simple web application built using Flask for managing employee records in a company. It provides functionalities to view, add, update, and delete employee information stored in a MySQL database.

Features
View all employees
Search for employees by first or last name
Add a new employee
Update an existing employee's details
Delete an employee record

Usage
Viewing All Employees
To view all employees, navigate to:
GET /employees
Searching for Employees
To search for employees by first or last name, use:
GET /search_employees?query=<name>
Adding a New Employee
To add a new employee, send a POST request to:
POST /employees
Updating an Employee
To update an existing employee's details, send a PUT request to:
PUT /employees/<ssn>
Deleting an Employee
To delete an employee, send a DELETE request to:
DELETE /employees/<ssn>

API Endpoints
GET /employees - Get all employees
GET /search_employees - Search employees by first or last name
POST /employees - Add a new employee
PUT /employees/<ssn> - Update an employee's details
DELETE /employees/<ssn> - Delete an employee

Error Handling
Validation errors are returned with a status code 400 and a JSON response containing the error details.

Templates
The project includes a basic HTML template for searching employees, located in the templates directory.

Built With
Flask - The web framework used
MySQL - Database
Flask-MySQLdb - Flask extension for MySQL
Marshmallow - Object serialization/deserialization library
