// Get the data from local storage

var data1 = JSON.parse(localStorage.getItem('formData')) || [];

// Iterate over the object and create a card element for each item
for (var i = 0; i < data1.length; i++) {
    row = document.getElementById('row');
    var card = `
  
    <div class="card">
    
    <div class="card-body">
    <h5 class="card-title">${data1[i].name}</h5>
    <p class="card-text">${data1[i].capital}</p>
    <p class="card-text">${data1[i].username}</p>
    <a href="/applyshare/" style=" textDecoration: 'none' " />
    <button type="button" id="apply${+i}"   onclick=reply_click(${i}) class="btn btn-apply" value="apply"> Apply</button>
    </a>
    </div>
    
    </div>
    
    `;
    row.innerHTML += card;



}
//if data is empty
if (data1.length == 0 || data1 == null || data1 == undefined) {
    document.getElementById('row').innerHTML = `
    <div class="card-body">
        <h5 class="card-title">No data found. Please add the Data</h5>
    </div>
    `;

}

//return true if apply button is clicked
function reply_click(clicked_id) {
    var data = JSON.parse(localStorage.getItem('formData')) || [];
    var name = data[clicked_id].name;
    var capital = data[clicked_id].capital;
    var username = data[clicked_id].username;
    var password = data[clicked_id].password;
    var crn = data[clicked_id].crn;
    var pin = data[clicked_id].pin;
    var userdata = {
        name: name,
        capital: capital,
        username: username,
        password: password,
        crn: crn,
        pin: pin
    }  
    var data = localStorage.setItem('userdata', JSON.stringify(userdata));
    var capply = localStorage.getItem('userdata');
    //save gdata as cookie
    document.cookie = "capply=" + capply;
    //delete the cookie after 1 minute
    return true;
}

 //when applysubmit button is clicked get current card data  and send the data to the server
 try{
    function submitData() {
  
  var shareid = document.getElementById('shareid').value;
  var bankid = document.getElementById('bankid').value;
  var sharequantity = document.getElementById('sharequantity').value;  
  var userdata = JSON.parse(localStorage.getItem('userdata')) || [];
  var name = userdata.name;
  var capital = userdata.capital;
  var username = userdata.username;
  var password = userdata.password;
  var crn = userdata.crn;
  var pin = userdata.pin;

  var applydata = {
      shareid: shareid,
      bankid: bankid,
      sharequantity: sharequantity,
      name: name,
      capital: capital,
      username: username,
      password: password,
      crn: crn,
      pin: pin
  }

      // Get the existing data from local storage, if any
      var existingData = JSON.parse(localStorage.getItem('apply-form')) || [];

      // Add the new data to the array
      existingData.push(applydata);
      // Save the updated array to local storage
      localStorage.setItem('userdata', JSON.stringify(existingData));
      // reload to form
      window.location.reload();
      alert('Share Applied Successfully');
     //wait for 2 seconds
        setTimeout(function(){
            //when sucess destroy userdata
            localStorage.removeItem('userdata');
            //when sucess destroy applydata
            localStorage.removeItem('apply-form');
        },25000);
 

}

}
catch(err){
    alert(err);
}



