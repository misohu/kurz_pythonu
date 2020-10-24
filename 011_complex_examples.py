# Video https://youtu.be/PY_sfXfCLOU
# Priklad 1
# Napiste kod ktory na zaklade 2 premennych vyska a sirka vypise mriezku vyplnenu hviezdickami
# rows = 3
# columns = 2
# **
# **
# **
rows = 5 
columns = 10
for row in range(0, rows):
    for column in range(0, columns):
        print("*", end="")
    print("")

# Priklad 2
# rows = 3
# *
# **
# ***
# **
# *
rows=3
for row in range(1, rows + 1):
    for columns in range(0, row):
        print("*", end="")
    print("")
for row in range(rows - 1, 0, -1):
    for columns in range(0, row):
        print("*", end="")
    print("")

# Priklad 3
# rows=3
# 1
# 1 2 
# 1 2 3
# 1 2 
# 1
rows = 5
for row in range(1, rows + 1):
    temp = ""
    for column in range(1, row + 1):
        temp += str(column)
        temp += " "
    print(temp)
for row in range(rows - 1, 0, -1):
    temp = ""
    for column in range(1, row + 1):
        temp += str(column)
        temp += " "
    print(temp)



