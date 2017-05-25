var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

app.use(bodyParser.json()); 

mongoose.Promise = global.Promise;
require('./server/config/mongoose.js');

var route_setter = require('./server/config/routes.js');
route_setter(app);


app.listen(8000, function() {
    console.log('listening on port 8000');
})