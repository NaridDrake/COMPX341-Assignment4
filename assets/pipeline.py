import os

commit_msg = input("Please enter a commit message: ")

#test that the app builds successfully
if (os.system("npm run build") != 0):
    exit(1)

#run the static test to ensure comments are added to all .ts files
if (os.system("python static_test.py") != 0):
    exit(1)

#git commands
os.system("cd ..")
os.system("git add .")
os.system("git commit -m \"%s\"" % commit_msg)
os.system("git push origin master")
