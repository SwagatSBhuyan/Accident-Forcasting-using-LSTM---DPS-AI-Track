const { spawn } = require('child_process');
const express = require('express')
const app = express()
const port = 3000

// var input = 202101;
var input = parseInt(process.argv[2])

const childPython = spawn('python', ['forecasting_script.py', input]);

childPython.stdout.on('data', (data) => {
	console.log(`${data}`);
});

childPython.stderr.on('data', (data) => {
	console.log(`stderr: ${data}`);
});

// childPython.on('close', (code) => {
// 	console.log(`Child process exited with code ${code}`);
// });