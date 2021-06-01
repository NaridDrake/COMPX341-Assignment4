import os

commit_msg = input("Please enter a commit message: ")

os.system("npm run build")

#git commands
os.system("cd ..")
os.system("git add .")
os.system("git commit -m \"%s\"" % commit_msg)
os.system("git push origin master")
