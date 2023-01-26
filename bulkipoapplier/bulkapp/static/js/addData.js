
try {
document.getElementById('my-form').addEventListener('submit', function (event) {
event.preventDefault();
var name = document.getElementById('name').value;
var capital = document.getElementById('capital').value;
var username = document.getElementById('username').value;
var password = document.getElementById('password').value;
var crn = document.getElementById('crn').value;
var pin = document.getElementById('pin').value;
//generate serial number for each data
// Create an object to store the data
var data = {
name: name,
capital: capital,
username: username,
password: password,
crn: crn,
pin: pin
};

// Get the existing data from local storage, if any
var existingData = JSON.parse(localStorage.getItem('formData')) || [];

// Add the new data to the array
existingData.push(data);
// Save the updated array to local storage
localStorage.setItem('formData', JSON.stringify(existingData));
// reload to form
window.location.reload();
alert('Data Saved Successfully');

});

} catch (error) {
alert(error);
}


