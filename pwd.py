import subprocess

# The text that will be copied to the clipboard if the secret code is valid, it can be a password for example.
pwd = "PUT_YOUR_TEXT_HERE"
pwd_input = int(input("Secret_Code:"))

# Replace 12 with your preferred code
if pwd_input == 12:
    subprocess.run("clip", universal_newlines=True, input=pwd)
    print("success: copied to clipboard")
else:
    print("Secret_Code is Invalid")
