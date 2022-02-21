function getAllUsers(){
    fetch('http://10.0.0.17:8000/users')
    .then(response=>response.json())
    .then(data=>{
        let html="<table>";
        data.forEach(element => {
            html+=`<tr><td>${element.id}</td>
            <td>${element.name}</td>
            <td>${element.email}</td></tr>`           
        });
        html+="</table>";
        document.getElementById("user").innerHTML=html;
    })
}

var i = 1;                  //  set your counter to 1

function loopRequest() {         //  create a loop function
  setTimeout(function() {   //  call a 3s setTimeout when the loop is called
       //  your code here
        getHumidityAndTemperature();               //  increment the counter
    if (i < 2) {           //  if the counter < 10, call the loop function
      loopRequest();             //  ..  again which will trigger another 
    }                       //  ..  setTimeout()
  }, 3000)
}

    


function getHumidityAndTemperature(){

    fetch('http://10.0.0.17:8000/temphum')
    .then(response=>response.json())
    .then(data=>{
        document.getElementById("tftemperature").innerHTML=data.temp;
        document.getElementById("tfhumidity").innerHTML=data.humidity;
        document.getElementById("tftemperaturePlant").innerHTML=data.temp;
        document.getElementById("tfhumidityPlant").innerHTML=data.humidity;
    })
}