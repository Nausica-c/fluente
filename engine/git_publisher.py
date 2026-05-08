import os

def publish():

    os.system("git add .")
    os.system('git commit -m "auto: generate articles batch"')
    os.system("git push origin main")

    print("🚀 Published to GitHub")
