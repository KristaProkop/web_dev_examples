function fib() {
  var arr = [];

  function nacci() {
    var nextNum;
    var currNum = arr[arr.length-1];
    var prevNum = arr[arr.length-2];

    if (arr.length <= 1 ){
      nextNum = 1;
    } else {
      nextNum = currNum + prevNum;
    }

    arr.push(nextNum);
    console.log(nextNum);
  }

  return nacci;

}


var fibCounter = fib();
fibCounter() // should console.log "1"
fibCounter() // should console.log "1"
fibCounter() // should console.log "2"
fibCounter() // should console.log "3"
fibCounter() // should console.log "5"
fibCounter() // should console.log "8"
fibCounter() // should console.log "13"

