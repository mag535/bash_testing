# This is just to print info on the Python_Files branch

print("In the \'Python_Files\' branch, only python files should be saved.")
print("There will be other branches for creating, editing, and adding/commiting other file types.")

sym1 = "^"
sym2 = "@"
sym3 = " : "
loop = 47

for i in range(loop):
    line = ""
    if i%3 == 0:
        line += sym1
    if i%5 == 0:
        line += sym2
    else:
        line += sym3
    print(line)

print("Just some random pyramid.")

