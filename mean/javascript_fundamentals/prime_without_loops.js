// Without using loops, return true if n is prime and false if not;

// like:
//   isPrime(7) == true 
//   isPrime(-7) == true 
//   isPrime(6) == false 
//   isPrime(-6) == false 

function isPrime(n) {
  n = Math.abs(n);
  if (n === 2) { return true };
  if (n === 0 || n === 1) { return false };
  let arr = Array.from(Array(n).keys()).filter(item => item > 1);
  return arr.every(item => n % item !== 0);
};

isPrime(3)