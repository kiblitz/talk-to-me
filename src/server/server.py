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
# def function_name(a, b, c):
#   a = a + b
#   return a + b + c # a + b + c + b

import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
uid = 0

# create database.db file with appropriate tables and columns
def create_database():
  c.execute("CREATE TABLE users (user_id PRIMARY KEY, first_name, last_name, email, username, password, entry_count)")
  c.execute("CREATE TABLE entries (entry_id PRIMARY KEY, timestamp, user_id, version)")

# add a user to the user table of database.db
def add_user(first, last, email, username, password):
    global uid
    uid += 1
    info = (uid, first, last, email, username, password, 0)
    c.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?)', info)
# testing function
# add_user("sal", "vulcano", "sal@gmail.com", "fatsal", "jokers123")

# returns true if password matches password with login matching either username or email; else false
def confirm_login(login, password):
    t = (login, login)
    c.execute("SELECT * FROM users WHERE username=? OR email=?", t)
    result = c.fetchone()
    print(result)
    try:
        if login == result[3] or login == result[4]:
            if password == result[5]:
                print("loading...")
                return True
            else:
                print("incorrect password")
                return False
    except:
        print("incorrect login")
        return False
# testing function
# confirm_login("fatsal", "jokers123")


# dont do yet
#def add_entry(user_id, entry_audio, 

conn.commit()
conn.close()
