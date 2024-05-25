function createEmployee() {
    const employee = {
        ssn: document.getElementById('ssn').value,
        Fname: document.getElementById('fname').value,
        Minit: document.getElementById('minit').value,
        Lname: document.getElementById('lname').value,
        Bdate: document.getElementById('bdate').value,
        Address: document.getElementById('address').value,
        Sex: document.getElementById('sex').value,
        Salary: document.getElementById('salary').value,
        Super_ssn: document.getElementById('super_ssn').value,
        DL_id: document.getElementById('dl_id').value
    };

    fetch('/employees', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(employee)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadEmployees();
    });
}

function updateEmployee() {
    const ssn = document.getElementById('ssn').value;
    const employee = {
        Fname: document.getElementById('fname').value,
        Minit: document.getElementById('minit').value,
        Lname: document.getElementById('lname').value,
        Bdate: document.getElementById('bdate').value,
        Address: document.getElementById('address').value,
        Sex: document.getElementById('sex').value,
        Salary: document.getElementById('salary').value,
        Super_ssn: document.getElementById('super_ssn').value,
        DL_id: document.getElementById('dl_id').value
    };

    fetch(`/employees/${ssn}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(employee)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadEmployees();
    });
}

function deleteEmployee(ssn) {
    fetch(`/employees/${ssn}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadEmployees();
    });
}

function searchEmployee() {
    const ssn = document.getElementById('search').value;
    fetch(`/employees`)
    .then(response => response.json())
    .then(data => {
        const filteredEmployees = data.filter(employee => employee.ssn.includes(ssn));
        displayEmployees(filteredEmployees);
    });
}

function loadEmployees() {
    fetch('/employees')
    .then(response => response.json())
    .then(data => {
        displayEmployees(data);
    });
}

function displayEmployees(employees) {
    const employeesList = document.getElementById('employeesList');
    employeesList.innerHTML = '';
    employees.forEach(employee => {
        const employeeDiv = document.createElement('div');
        employeeDiv.className = 'employee';
        employeeDiv.innerHTML = `
            <p>${employee.Fname} ${employee.Lname} (SSN: ${employee.ssn})</p>
            <button onclick="deleteEmployee(${employee.ssn})">Delete</button>
        `;
        employeesList.appendChild(employeeDiv);
    });
}

window.onload = loadEmployees;
