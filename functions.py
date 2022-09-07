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
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)