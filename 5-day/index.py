# 5TH DAY
# Logical operators

# Logical operators make it possible to transform bool values. For example
# we need to check if one value is True and the second one is also True
# - we can use 'and' operator which returns True if both left- and right-side
# values are True. Otherwise it returns False.

# and operator
print('and')

# As I said before, and returns True if both values are True.

# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

result = True and True # Will be True - left- and right-side booleans are True
print('True and True -> ' + str(result))

result = False and True # Will be False - one of the values is False
print('False and True -> ' + str(result))

result = False and False # Will be False - both values are False
print('False and False -> ' + str(result))

# or operator
print('or')

# or returns True if at least one of the values is True.

# True and True -> True
# True and False -> True
# False and True -> True
# False and False -> False

result = True or True # Will be True - both values are True
print('True or True -> ' + str(result))

result = False or True # Will be True - one of the values is True
print('False or True -> ' + str(result))

result = False or False # Will be False - both values are False
print('False or False -> ' + str(result))

# not operator
print('not')

# not operator takes only one value (after the keyword) and returns True if
# value is False and vice versa.

# not True -> False
# not False -> True

result = not True # I think it doesn't require an explanation ;)
print('not True -> ' + str(result))

result = not False
print('not False -> ' + str(result))

# Comparison operators and logical operators
print('Comparison operators and logical operators')

# Now we'll do some exercises with both comparison and logical operators

# 1. We want to check whether a is equal b and c is less than or equal d

a = 5
b = 4
c = 20
d = 42

result = a == b and c <= d
print('a == b and c <= d -> ' + str(result))

# a == b -> 5 == 4 -> False
# c <= d -> 20 <= 42 -> True
# a == b and c <= d -> False and True -> False

# 2. We want to check whether a is greater than b or c is not equal d

a = 10
b = 0
c = 3
d = 3

result = a > b or c != d
print ('a > b or c != d -> ' + str(result))

# a > b -> 10 > 0 -> True
# c != d -> 3 != 3 -> False
# True or False -> True

# 3. We want to check whether a is not equal b

a = 15
b = 100

result = not a == b
print('not a == b -> ' + str(result))

# Wait, can't we just type a != b?! Yes, of course we can!
# We can use either 'not a == b' or 'a != b' to check the inequality

# a == b -> 15 == 100 -> False
# not False -> True

# 5th day complete!
