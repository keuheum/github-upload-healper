from os import popen, system
from datetime import datetime

def main():
    msg = input("Please enter your commit message. ")

    if msg == 0 or msg == ".":
        print("\nEnter file input mode.\n")
        system("git status")
        file = input("\nPlease enter a file name. ")
        system(f'git add {file}')
        main()

    elif msg == "first_git":
        first_git()

    else:
        popen("git add .")
        github_upload(msg)
        
def first_git():
    print("\033[91m**Caution**\033[0m\nThis program only helps you upload to GitHub, but does not verify the value. Please write the exact value.")
    username = input("Please enter the name of your GitHub account. ")
    useremail = input("Please enter the email address of your GitHub account. ")
    git_url = input("Please enter the github url you want to connect to. ")
    if useremail == "." and username == ".":
        list_command = [
            'git init',
            'git config --global init.defaultBranch main',
            f'git remote add origin {git_url}',
            'git status'
        ]
        
    else:
        list_command = [
            'git init',
            'git config --global init.defaultBranch main',
            f'git config --global user.name "{username}"',
            f'git config --global user.email "{useremail}"',
            f'git remote add origin {git_url}',
            'git status'
        ]

    for i in list_command:
        print(f">>> {i}")
        system(i)

    print("The default setting is over.")
    exit()

def github_upload(msg=str):
    list_command = [
    f'git commit -m "[{datetime.now().strftime("%Y-%m-%d/%H:%M:%S")}] {msg}"',
    'git push origin +main',#Requires +main only at first (+ sign means push master permission)
    #'git status'#Use only those who need it
    ]

    for i in list_command:
        print(f">>> {i}")
        system(i)

    print("Github upload complete.")

if __name__ == "__main__":
    main() 