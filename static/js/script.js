function searchEmployee() {
    const ssn = document.getElementById('searchBar').value;
    fetch(`/employees/${ssn}`)
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById('results');
            resultDiv.innerHTML = '';

            if (data.message) {
                resultDiv.innerHTML = `<p>${data.message}</p>`;
            } else {
                let employeeInfo = `
                    <p>SSN: ${data.ssn}</p>
                    <p>Name: ${data.Fname} ${data.Minit} ${data.Lname}</p>
                    <p>Birth Date: ${data.Bdate}</p>
                    <p>Address: ${data.Address}</p>
                    <p>Sex: ${data.Sex}</p>
                    <p>Salary: ${data.Salary}</p>
                    <p>Supervisor SSN: ${data.Super_ssn}</p>
                    <p>DL ID: ${data.DL_id}</p>
                `;
                resultDiv.innerHTML = employeeInfo;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('results').innerHTML = '<p>An error occurred while fetching employee data.</p>';
        });
}
