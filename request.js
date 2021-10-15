const express = require('express')
const { spawn } = require('child_process');
const {PythonShell} =require('python-shell');
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World!'))
var bodyParser = require('body-parser'); 
var jsonParser = bodyParser.json();
var urlencodedParser = bodyParser.urlencoded({ extended: false }); 
app.use(express.static('public'));  
app.use(bodyParser());

 
app.post('/run', jsonParser, function (req, res) {  
	y = req.body.year;
	m = req.body.month;
	input = y*100 + m;
	pred = 0

	let options = {
        mode: 'text',
        pythonOptions: ['-u'],
        args: [input]
    };

	PythonShell.run('forecasting_script.py', options, function (err, result){
		if (err) throw err;

		var output = {
			"prediction" : parseInt(result[0])
		}
		res.send(output);
	});

})  

app.listen(port, () => console.log(`Sever running at http://localhost:3000/`))