function getAllUsers(){
    fetch('http://127.0.0.1:8000/users')
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