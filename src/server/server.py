#
# THESE ARE COMMENTS
# 
# Variables:
# x = 4
# y = True
# random_var = "yes"
# x = True
# x + 4 + y # NONONONO
# 
# tp = 3, True, "no"
# tp = 1, 4, False
# tp[0] += 1 # WRONG - tuples are immutable (can't change)
# test = tp[1] # = 4
#
# arr = [1, 2, 3, True, (False, 4), "ha"]
# arr[0] = arr[1] + 2 # [4, 2, 3...
# arr[4][0] # False
# arr[4][1] += 1 # NO - tuples can't change
# # arr.append, arr.remove, etc.
#
# "s" + "a" # "sa"
# "s" == "s" # True
# # lots of functions like arrays
#
#
# Flow: # Booleans
# if x == "s": # if x is "s" then set x to 5
#   x = 5
# elif (not a) and (y == 2): # if a is False and y is 2
#   x = 2
# else:
#   x = 0
#
# # or, !=, <, >, <=, etc.
#
# while b != 3:
#   b += 1
# 
# for i in [0, 1, 2, 3, 4]:
#   b += i
# # b = 3 + 10 = 13
#
# range(4) # [0, 1, 2, 3]
# range(0) # []
# range(3, 7) # [3, 4, 5, 6]
# range(3, 10, 2) # [3, 5, 7, 9]
#
# sum = 0 
#
# for i in range (3, 10, 2):
#   sum += i
# # sum = 24
# 
# for (i, j) in [(1, 2), (2, 4)]:
#   pass
#
