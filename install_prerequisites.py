import subprocess

prerequisites = ["selenium", "tkinter", "customtkinter"]
try:
    for i in prerequisites:
        subprocess.call(f"pip install {i}")
        print(f"installing package: {i}")

except Exception as ex:
    print(ex)
