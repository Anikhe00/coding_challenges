def solution(number):
  if number < 0:
    return 0
  result = 0
  for num in range(number):
      if num % 3 == 0 or num % 5 == 0:
        result += num
  return result

print(solution(10))