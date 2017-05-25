var mongoose = require('mongoose');
var Animal = mongoose.model('Animal');

module.exports = {
    showAll: function(req, res) {
        Animal.find( {}, function(err, animals) {
            if(err) {
                console.log("No animals found");
                res.redirect('/animals/new');
            } else {
                res.render('index', {animals: animals});
            }
        })
    },

    create: function(req, res) {
        var animal = new Animal({ name: req.body.name, family: req.body.family, color: req.body.color, lifespanYears: req.body.lifespanYears});
        animal.save(function(err) {
            if (err) {
                console.log(err);
            } 
        res.redirect('/');
        })
    },

    showOne: function(req, res) {
        Animal.find({ _id: req.params.id}, function(err, animal) {
            if(err){
                console.log('error retrieving animal');
                res.redirect('/');
            } else {
                res.render('showAnimal', {animal: animal});
            }
        })
    },

    edit: function(req, res) {
        Animal.find({_id: req.params.id}, function(err, animal) {
            if(err) {
                console.log('error retrieving animal');
                res.redirect('/');
            } else {
                res.render('editAnimal', {animal: animal});
            }
        })
    },

    update: function(req, res) {
        Animal.update({_id: req.params.id}, {$set: {name: req.body.name, family: req.body.family, color: req.body.color, lifespanYears: req.body.lifespanYears} }, function(err) {
            if(err){
               console.log("error updating animal");
               
            } 
            res.redirect('/animals/'+req.params.id);
        })
    },

    destroy: function(req, res) {
        Animal.remove( { _id: req.params.id }, function(err, animal) {
            if (err) {
                console.log('error retrieving animal');
                res.redirect('/animals/'+req.params.id)
            } 
            res.redirect('/');
        })
    }


}