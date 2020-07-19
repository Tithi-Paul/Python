def sum_positive_numbers(n):
  result = 0;
  for i in range(n):
    result= result+n
    n=n-1;
  return result
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
