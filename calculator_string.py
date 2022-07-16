import re

def adddtion_of_string_values(numbers: str):
  if numbers == '':
    return 0

  del_ = None
  if numbers[:2] == '//':
    numbers = numbers[2:]
    del_, numbers = re.split('\n', numbers, 1)

  pattern = ',|\n'
  if del_ is not None:
    pattern = f',|\n|\{del_}'

  nums = [ int(_) for _ in re.split(pattern, numbers) ]

  # check for negatives
  for num in nums:
    if num < 0:
      raise ValueError(f'negatives numbers are  not allowed. found {num}')
  return sum(nums) 
