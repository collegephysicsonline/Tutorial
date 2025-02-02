import subprocess
import sys

def install_packages():
    with open('requirements.txt', 'r') as file:
        packages = file.readlines()
    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package.strip()])

if __name__ == '__main__':
    install_packages()
    
# Run the script in the terminal
# python requirements.py    