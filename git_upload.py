from os import popen, system
from datetime import datetime

def main():
    msg = input("커밋 메시지를 입력해주세요. ")

    if msg == 0 or msg == ".":
        print("\n파일 입력 모드 진입.\n")
        system("git status")
        file = input("\n파일명을 입력하여주세요. ")
        system(f'git add {file}')
        main()

    elif msg == "first_git":
        first_git()

    else:
        popen("git add .")
        github_upload(msg)
        
def first_git():
    print("\033[91m**주의**\033[0m\n본 프로그램은 깃허브 업로드를 도와줄뿐, 값 검증을 하지 않습니다. 정확한 값을 적어주세요.")
    username = input("깃허브 계정의 이름을 적어주세요. ")
    useremail = input("깃허브 계정의 이메일을 적어주세요. ")
    git_url = input("연결을 원하는 깃허브 url을 적어주세요. ")
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

    print("기본 설정이 종료되었습니다.")
    exit()

def github_upload(msg=str):
    list_command = [
    'git status',
    f'git commit -m "[{datetime.now().strftime("%Y-%m-%d/%H:%M:%S")}] {msg}"',
    'git push origin +main'
    ]

    for i in list_command:
        print(f">>> {i}")
        system(i)

    print("깃헙 업로드 완료.")

if __name__ == "__main__":
    main()