# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(10,20,30))
print(max_num(82,150,27))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
  if len(list) == 0:
    return 0
  prod = list[0]

  if len(list) > 1:
    for i in list[1:]:
      prod = prod * i
  
  return prod

print(mult_list([1,2,3]))
print(mult_list([2,2,2,2]))


# Write a Python function called rev_string() to reverse a string.
def rev_string(my_string):
  return my_string[::-1]

print(rev_string(''))
print(rev_string('apple'))
print(rev_string('mt '))


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

sample_pascal_triangle = '''
          [1]
        [1] [1]
      [1] [2] [1]
    [1] [3] [3] [1]
  [1] [4] [6] [4] [1]
'''
def pascal():