function squareSum(numbers){
  let total_sum = 0
  
  for(i=0;i<numbers.length;i++) {
    let x = numbers[i];
    let squared_number = x ** 2
    total_sum += squared_number
  }
  return total_sum
}