'use strict';

const express = require('express');
var app = express();
var bodyParser = require('body-parser');

// Constants
const PORT = 8089;
const HOST = '0.0.0.0';

// Create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false })



app.use(express.static('public'));


app.get('/index.htm', function (req, res) {
  console.log("__dirname>");
  console.log(__dirname);
  res.sendFile( __dirname + "/" + "index.htm" );
})

// App
//const app = express();
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`---------------------------------------------------`);
console.log(`Running on http://${HOST}:${PORT}`);
console.log(`---------------------------------------------------`);