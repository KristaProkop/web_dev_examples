// Your are given a string. You must replace the word(s) coverage with covfefe, however, if you don't find the word coverage in the string, you must add it at the end of the string with a leading space.



var string = 'This is a test'
console.log(covfefe('coverage')) //"covfefe"
console.log(covfefe("coverage coverage")) //"covfefe covfefe"
console.log(covfefe("nothing")) //"nothing covfefe"
console.log(covfefe("double space ")) //"double space  covfefe"
console.log(covfefe("covfefe")) //"covfefe covfefe"

// with regex:
function covfefe(string) {
    var word = 'coverage'
    if(string.includes(word)) {
        var re = new RegExp(word, 'g');
        string = string.replace(re, "covfefe"); 
    } else {
        string = string.concat(' covfefe');
    }
    return string;
}

// with array and map:
// function covfefe(word) {
//     var arr = word.split(' ');
//     if(arr.includes('coverage')) {
//         arr = arr.map(function(item) { 
//             return item == 'coverage' ? 'covfefe' : item; 
//         });
//     } else {
//         arr.push('covfefe');
//     } 
//     return arr.join(' ');
// }


