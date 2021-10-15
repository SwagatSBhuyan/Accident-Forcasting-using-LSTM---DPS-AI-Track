const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World!'))
var bodyParser = require('body-parser'); 
var jsonParser = bodyParser.json();
var urlencodedParser = bodyParser.urlencoded({ extended: false }); 
app.use(express.static('public'));  
app.use(bodyParser());

 
app.post('/run', jsonParser, function (req, res) {  
	console.log(JSON.stringify(req.body));
	y = toString(req.body.year);
	// m = toString(req.body.month);
	// var value = toString(year) + toString(month);

	var output = {
		"prediction" : y
	}
	res.send(output);  
})  

app.listen(port, () => console.log(`Sever running at http://localhost:3000/`))