var mongoose = require('mongoose');
var Person = mongoose.model('Person');

module.exports = {

    showAll: function(req, res) {
        Person.find({}, function(err, people) {
            if(err) {
                console.log("None found")
                res.json({err: "no people found"})
            } else {
                res.json(people);
            }
        })
    },

    showOne: function(req, res) {
        Person.find({name: req.params.name}, function(err, person) {
            if(err) {
                res.redirect('/');
            } else {
                res.json(person);
            }
        })
    },

    create: function(req, res) {
        person = new Person( {name: req.params.name});
        person.save(function(err) {
            if(err) {
                console.log(err);
            }
        })
        res.redirect('/');
    },

    destroy: function(req, res) {
        Person.remove( { name: req.params.name }, function(err, person) {
            if (err) {
                console.log("couldn't delete " + req.params.name);
            }
        })
        res.redirect('/');
    }

}
