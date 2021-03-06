function loadLineChart(){

  var humidity=new Array;
  var temperature=new Array;
  var preassure=new Array;
  
  
    fetch('http://192.168.137.206:8000/testData')
    .then(response=>response.json())
    .then(data=>{
      data.temp.forEach(e=>{
      temperature.push(e);
    })
    data.hum.forEach(e=>{
      humidity.push(e);
    })
    data.prsr.forEach(e=>{
      preassure.push(e);
    })
  
  })
  
  


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
      type: 'logarithmic',
      title: {
        display: true,
        text: 'y - Axis',
      },
    }
  };


  const zoomOptions = {
    limits: {
        x: {min: 0, max: 2000, minRange: 50},
        y: {min: 0, max: 2000, minRange: 50}
      },
    pan: {
      enabled: true,
      mode: 'xy',
      modifierKey: 'ctrl',
    },
    zoom: {
      drag: {
        enabled: true
      },
      wheel: {
        enabled: true,
      },
      mode: 'xy',
    },
  };


  const data = {
    labels: labels,
    datasets: [{
      label: 'Temperature : C°',
      backgroundColor: 'rgb(231, 158, 79)',
      borderColor: 'rgb(160, 83, 68)',
      data: temperature,
    },{
      label: 'Humidity : %',
      backgroundColor: 'rgb(188, 111, 241)',
      borderColor: 'rgb(137, 44, 220)',
      data: humidity,
    },{
        label: 'Air Preassure : hPa',
        backgroundColor: 'rgb(173, 29, 69)',
        borderColor: 'rgb(249, 210, 118)',
        data: preassure,
      }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {
        scales:scales,
        plugins: {
            zoom: zoomOptions
        },
    },
    plugins: [background]
  };


  const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
  }