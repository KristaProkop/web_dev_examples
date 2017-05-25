var mongoose = require('mongoose');
var fs = require('fs');
var path = require('path');

mongoose.connect('mongodb://localhost/animals');

var models_path = path.join(__dirname, './../models');

fs.readdirSync(models_path).forEach(function(file) {
    if(file.indexOf('.js') >= 0) {
        require(models_path + '/' + file);
    }
})

var AnimalSchema = new mongoose.Schema({
    name: {type: String, required: true},
    family: {type: String, required: true},
    color: {type: String, required: true},
    lifespanYears: {type: String, required: true}
}, {timestamps: true});

var Animal = mongoose.model('Animal', AnimalSchema);