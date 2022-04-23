function Sleep(milliseconds) {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
   }

function execute(){
    setInterval(function(){
        getCurrTemp();
    }, 3000)
    
}




function getCurrTemp(){
    fetch('http://192.168.10.249:8000/readings')
	.then(response=>response.json())
	.then(data=>{
        let reading;
		console.log(data)
		reading = data.temp;
        document.getElementById('tempOut').innerHTML=`<b>${reading}°C</b>`;
    })    
}