

var fs = require('fs');
var url = require('url');
var path = require('path');


module.exports = function (request, response) {

    var pathName = url.parse(request.url)['path'];
    var ext = path.parse(pathName).ext;
    var mimeType = {
        '.ico': 'image/x-icon',
        '.html': 'text/html',
        '.js':'text/javascript',
        '.css': 'text/css',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
    }
    
    if (request.url === '/' ) {
          parsedPath = 'views/index.html';
    } else {
        parsedPath = pathName.replace('/','');
        if( ext == false ){
            parsedPath = `views/${parsedPath}.html`;
        } 
    }
    
    fs.exists(parsedPath, function (exist) {
        if(!exist) {
              response.statusCode = 404;
              response.end(`File ${pathName} not found!`);
              return;
        }
        
        fs.readFile(parsedPath, function(error, content) {
            if(error) {
                response.statusCode = 500;
                response.end(`Error getting the file: ${err}.`);
            } else {
                response.writeHead(200, 'Content-type', mimeType[ext] || 'text/plain'  );
                response.write(content);
                response.end();
            }
        });
    });
}



