const API_URL = 'https://jsonplaceholder.typicode.com/users/';

        const xhr = new XMLHttpRequest();

        function onRequestHandler() {
            if (this.readyState == 4 && this.status == 200) {
                const data = JSON.parse(this.response);
                const tableBody = document.getElementById('users-table').querySelector('tbody');

                data.forEach(user => {
                    const row = document.createElement('tr');

                    row.innerHTML = `
                        <td>${user.id}</td>
                        <td>${user.name}</td>
                        <td>${user.username}</td>
                        <td>${user.email}</td>
                        <td>${user.address.street}, ${user.address.suite}, ${user.address.city}, ${user.address.zipcode}</td>
                        <td>${user.phone}</td>
                        <td>${user.website}</td>
                        <td>${user.company.name}</td>
                    `;

                    tableBody.appendChild(row);
                });
            }
        }

        xhr.addEventListener("load", onRequestHandler);
        xhr.open('GET', API_URL);
        xhr.send();