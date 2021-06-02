import glob

for name in glob.glob('/COMPX341-Assignment4/assets/src/**/*.ts', recursive=True):
    # print(name)
    f = open(name, "r")

    commentLine1 = "//Narid Drake: 1363139\n"
    readLine1 = f.readline()
    if (commentLine1 != readLine1):
        print("Comment not found, exiting with 1")
        exit(1)
    
print("All comments found, exiting with 0")
exit(0)
