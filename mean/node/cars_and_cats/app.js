var http = require('http');

var fs = require('fs');

var server = http.createServer( function(request, response) {

    console.log('client request URL: ', request.url);

    if (request.url === "/cars") {
         fs.readFile('views/cars.html', 'utf8', function (errors, contents){
             response.writeHead(200, {'Content-type': 'text/html'});
             response.write(contents); 
             response.end();
         });
    }

    else if (request.url === '/cats'){
        fs.readFile('views/cats.html', 'utf8', function (errors, contents) {
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents);
            response.end();
        });
    }

    else if (request.url === '/cars/new'){
        fs.readFile('views/cars-form.html', 'utf8', function (errors, contents) {
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents);
            response.end();
        });
    }

    else if(request.url === '/stylesheets/styles.css'){
        fs.readFile('stylesheets/styles.css', 'utf8', function(errors, contents){
         response.writeHead(200, {'Content-type': 'text/css'});
         response.write(contents);
         response.end();
        })
    }

    else if(request.url === '/images/mini.jpg'){
        fs.readFile('./images/mini.jpg', function(errors, contents){
            response.writeHead(200, {'Content-type': 'image/jpg'});
            response.write(contents);
            response.end();
        })
    }

    else if(request.url === '/images/mini1.jpg'){
        fs.readFile('./images/mini1.jpg', function(errors, contents){
            response.writeHead(200, {'Content-type': 'image/jpg'});
            response.write(contents);
            response.end();
        })
    }

    else if(request.url === '/images/cats.jpg'){
        fs.readFile('./images/cats.jpg', function(errors, contents){
            response.writeHead(200, {'Content-type': 'image/jpg'});
            response.write(contents);
            response.end();
        })
    }

    else if(request.url === '/images/cats1.jpg'){
        fs.readFile('./images/cats1.jpg', function(errors, contents){
            response.writeHead(200, {'Content-type': 'image/jpg'});
            response.write(contents);
            response.end();
        })
    }

    else {
        response.writeHead(404);
        response.end('File not found!!!');
    }

});

server.listen(6789);
// print to terminal window
console.log("Running in localhost at port 6789");