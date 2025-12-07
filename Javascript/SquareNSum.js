// Complete the square sum function so that it squares each number 
// passed into it and then sums the results together.

// For example, for [1, 2, 2] it should return 9.

function squareSum(numbers){
  let total_sum = 0
  
  for(i=0;i<numbers.length;i++) {
    let x = numbers[i];
    let squared_number = x ** 2
    total_sum += squared_number
  }
  return total_sum
}