var _ = {

   filter: function(arr, callback) { 
     var result = [];
     for(var i = 0; i < arr.length; i++ ){
      if (callback(arr[i])) {
         result.push(arr[i]);
      };
     }
     return result;
   },

   reduce: function(arr, callback, memo) { 
     var subtotal = memo
     for(var i = 0; i < arr.length; i++ ){
      subtotal = callback(subtotal, arr[i]);
     }
     return subtotal;
   },

   reject: function(arr, callback) { 
     var result = [];
     for(var i = 0; i < arr.length; i++ ){
      if (!callback(arr[i])) {
        result.push(arr[i]);
      };
     }
     return result;
   },

   map: function(list, callback) {
     var result = [];
     for(var i in list){
        result.push(callback(list[i])); 
     };
     return result;
   },

   find: function(list, callback) {   
     for (var i = 0; i < list.length; i++) {
        if (callback(list[i])) {
            return list[i];
        } 
     }
   }
 }

var find = _.find([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(find);
// 2

var map = _.map([1, 2, 3], function(num){ return num * 3; });
console.log(map)
// [3, 6, 9]

var map = _.map({one: 1, two: 2, three: 3}, function(num, key){ return num * 3; });
console.log(map);
// [3, 6, 9]

var reject = _.reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(reject);
// [1, 3, 5]

var filter = _.filter([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
console.log(filter); 
// [2, 4, 6]

var reduce = _.reduce([1, 2, 3], function(memo, num){ return memo + num; }, 0);
console.log(reduce);
// 6



