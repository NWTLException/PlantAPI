function Sleep(milliseconds) {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
   }

function execute(){
    setInterval(function(){
        getReadings();
    }, 1000)
    
}




function getReadings(){
    fetch('http://192.168.137.206:8000/readings/all')
	.then(response=>response.json())
	.then(data=>{
		console.log(data)
        document.getElementById('tempOut').innerHTML=`<b>${data.temp} °C</b>`;
        document.getElementById('humOut').innerHTML=`<b>${data.hum} %</b>`;
        document.getElementById('prsrOut').innerHTML=`<b>${data.prsr} hPa</b>`;
        document.getElementById('airquOut').innerHTML=`<b>${data.airqu} Ω</b>`;
    })    
}







