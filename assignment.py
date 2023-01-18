# 1
def max_num(n1, n2, n3):
    return max(n1, n2, n3)

print('Test max_num():')
print(max_num(1, 2, 3))
print(max_num(3, 55, 2))

# 2
def mult_list(list):
    i = 0
    n = 1
    while i < len(list):
        n *= list[i]
        i += 1
    return n

print('Test mult_list():')
print(mult_list([4, 6, 9]))

# 3
def rev_string(str):
    # base case
    if len(str) == 1 or len(str) == 0:
        return str
    # recursive case
    return str[-1] + rev_string(str[1:-1]) + str[0]

print('Test rev_string():')
print(rev_string('alex'))

# 4
def num_within(n, beg, end):
    return n >= beg and n <= end

print('Test num_within():')
print(num_within(5, 3, 10))
print(num_within(1, 3, 10))

# 5
def pascal(n):
    # error case
    if n < 1:
        print(f'{n} is an invalid number of rows')
    # set current row to 1 and calculate each row until n
    current_row = 1
    while current_row <= n:
        # row always starts with 1
        row = [1]
        # find each element of current row
        for i in range(1, current_row):
            # formula finds element of pascals triangle 
            # given the row and position in row
            element = (row[i - 1] * (current_row - i)) / i
            row.append(int(element))
        print(row)
        current_row += 1

print('Test pascal():')
pascal(4)
pascal(1)
pascal(-9)
pascal(10)
