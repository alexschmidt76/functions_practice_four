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
