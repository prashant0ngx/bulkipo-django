var data = JSON.parse(localStorage.getItem('formData')) || [];
            var nodata = document.getElementsByClassName('no-data');
            var table = document.getElementById('tbody');
            // if data is empty
            if (data.length == 0 || data == null || data == undefined) {
                table.innerHTML = `<tr>
                <td colspan="4" align="center">No data found. Please add the Data</td>
            </tr>`;

            }

            // if data is not empty

            for (var i = 0; i < data.length; i++) {
  
                var row = `<tr>
                <td >${i}</td>
                <td>${data[i].name}</td>
                <td>${data[i].capital}</td>
                <td>${data[i].username}</td>
                <td>
                    <button type="button"  class="btn btn-danger"><i class="bx bx-trash-alt"></i></button></td>
             
            </tr>`;
                table.innerHTML += row;
            }
            try {
                //delete the particular row when btn is clicked
                var deleteBtn = document.getElementsByClassName('btn-danger');
                var deletesuccessmessage = " Data deleted successfully";
                for (var i = 0; i < deleteBtn.length; i++) {
                    deleteBtn[i].addEventListener('click', function () {
                        var row = this.parentElement.parentElement;
                        var id = row.children[0].innerHTML;
                        data.splice(id - 1, 1);
                        localStorage.setItem('formData', JSON.stringify(data));
                        row.remove();
                        alert(deletesuccessmessage);

                    });
                }
            }
            catch (error) {
                alert(error);
            }

            //delete all data
            var deleteAllBtn = document.getElementById('deleteAll');
            var deletesuccessmessage = "All Data deleted successfully";
            deleteAllBtn.addEventListener('click', function () {
                localStorage.clear();
                table.innerHTML = `<tr>
                <td colspan="4" align="center">No data found. Please add the Data</td>
            </tr>`;
                alert(deletesuccessmessage);
            });

