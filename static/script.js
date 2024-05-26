document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const query = document.getElementById('searchInput').value;
    fetch(`/search_employees?query=${query}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            if (data.length > 0) {
                data.forEach(employee => {
                    const employeeDiv = document.createElement('div');
                    employeeDiv.className = 'employee';
                    employeeDiv.innerHTML = `
                        <p>Name: ${employee.Fname} ${employee.Lname}</p>
                        <p>SSN: ${employee.ssn}</p>
                        <p>Address: ${employee.Address}</p>
                        <p>Salary: ${employee.Salary}</p>
                    `;
                    resultsDiv.appendChild(employeeDiv);
                });
            } else {
                resultsDiv.innerHTML = '<p>No employees found</p>';
            }
        });
});
