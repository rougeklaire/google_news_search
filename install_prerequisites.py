import subprocess

def install_prerequisites():
    prerequisites = ["selenium", "tkinter", "customtkinter"]
    try:
        for i in prerequisites:
            subprocess.call(f"pip install {i}")
            print(f"installing package: {i}")

    except:
        print("exception occurred")