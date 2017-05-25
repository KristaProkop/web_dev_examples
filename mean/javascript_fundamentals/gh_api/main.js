// JS Promise:
$(document).ready(function(){
    $('button').click(displayName);
});


function displayName() {
    var promise = new Promise(function(resolve, reject) {
        var request = new XMLHttpRequest();

        request.open('GET', 'https://api.github.com/users/kristaprokop');
        request.onload = function() {
            if (request.status == 200) {
                resolve(request.response); 
            } else {
                reject(Error(request.statusText));  
            }
        };

        request.onerror = function() {
            reject(Error('Error fetching data.')); 
        };
        
        request.send(); 
    });

    promise.then(function(data) {
        var name = JSON.parse(data).login;
        $('h2').html(name);
    }, 

    function(error) {
        console.log(error.message);
    });
}


// JQUERY:
// $(document).ready(function(){
//     $('button').click(function(){
//         $.get("https://api.github.com/users/kristaprokop", displayName);
//     });
// });

// // function displayName(data) {
// //       $('h2').html(data['login']);
// //     }