# Some random code to print an ACSII pyramid

pyramid_base = 5
sym = "*"
white_space = " - "

for i in range(pyramid_base):
    line = ""
    for j in range(i+1):
        line += sym
    for k in range(pyramid_base - (i+1)):
        line += white_space
    print(line)

print("It's supposed to be a pyramid")

