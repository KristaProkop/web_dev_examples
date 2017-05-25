var express = require('express');

var path = require('path');

var app = express();

var bodyParser = require('body-parser');


app.use(bodyParser.urlencoded({ extended: true}));

app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));

app.set('view engine', 'ejs');

app.get('/', function(request, response) {
    response.render('index');
})

app.post('/result', function (req, res) {
    var survey_result = {
        name: req.body['Name'], 
        location: req.body['location'],
        language: req.body['language'],
        comment: req.body['comment'],
    };
    res.render('results', {result: survey_result});
});


app.listen(8000, function() {
    console.log('listening on port 8000');
}); 