var temperature = []
var humidity = []

function getLast24h(){
    fetch('http://192.168.137.206:8000/readings/last24')
    .then(response=>response.json())
    .then(data=>{
		console.log(data)
        data.forEach(d=>{
            console.log(d.temp)
            temperature.push(d.temp)
			console.log(d.hum)
            humidity.push(d.hum)
        })  
    }
	)

	console.log(temperature)
	console.log(humidity)
	

}




function loadTempChart(){

	const labels = [
		'00:00',
		'01:00',
		'02:00',
		'03:00',
		'04:00',
		'05:00',
		'06:00',
		'07:00',
		'08:00',
		'09:00',
		'10:00',
		'11:00',
		'12:00',
		'13:00',
		'14:00',
		'15:00',
		'16:00',
		'17:00',
		'18:00',
		'19:00',
		'20:00',
		'21:00',
		'23:00',
		'24:00',
	  ];

	  const background = {
		id: 'custom_canvas_background_color',
		beforeDraw: (chart) => {
		  const ctx = chart.canvas.getContext('2d');
		  ctx.save();
		  ctx.globalCompositeOperation = 'destination-over';
		  ctx.fillStyle = 'rgb(50, 31, 40)';
		  ctx.fillRect(0, 0, chart.width, chart.height);
		  ctx.restore();
		}
	  };

	  const scales = {
		y: {
		  title: {
			display: true,
			text: 'Values',
		  },
		}
	  };

	  const data = {
		labels: labels,
		datasets: [{
		  label: 'Temperature C°',
		  backgroundColor: 'rgb(231, 158, 79)',
		  borderColor: 'rgb(160, 83, 68)',
		  data: temperature,
		},
		{
			label: 'Humidity %',
			backgroundColor: 'rgb(0,0,205)',
			borderColor: 'rgb(0,191,255)',
			data: humidity,
		  }
	]
	};

	const config = {
		type: 'line',
		data: data,
		options: {
			scales:scales,
		},
		plugins: [background]
	  };

	  const myChart2 = new Chart(
		document.getElementById('myChart2'),
		config
	  );

	  function update(){
		getLast24h();
		myChart2.data.datasets[0].data=temperature;
		
	}
	
	

}




