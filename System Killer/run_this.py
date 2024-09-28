import subprocess
if input("Warning: Once run, this program cannot be stopped.\n\nTo continue, press enter.\nTo exit, type 'exit'.\n").lower() == "exit":
    exit()
else:
    if input("Are you SURE you want to run this program?\nPress enter to continue or type 'exit' to exit.\n").lower() == "exit":
        exit()
    else:
        subprocess.run(f'start cmd /k python "{__file__.replace("run_this.py", "crasher.py")}"', shell=True)
