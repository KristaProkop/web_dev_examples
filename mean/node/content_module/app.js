

var http = require('http');
// the file below is the file you need to create for this assignment.
var static_contents = require('./module.js');

server = http.createServer(function (request, response){

  static_contents(request, response);  

});

server.listen(8000);
console.log("Running in localhost at port 8000");



