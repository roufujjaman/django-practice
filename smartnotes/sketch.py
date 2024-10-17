fname = ["roufujjaman", "atif", "arman", "kabir"]
lname = ["rahat", "aslam", "khan", "khan"]


for n in zip(fname, lname):
    print((n[0] + " " + n[1]).title())

print(zip(fname, lname))