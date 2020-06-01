import sys
import subprocess

#тест1 аргумент 50
code = subprocess.run('python project.py 50', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);
if(code.returncode == 0):
    print('Test 1 proshel uspeshno')
else:
    print('Test 1 error')
    sys.exit(1)

#тест2 аргумент Карусель
code = subprocess.run('python project.py Карусель', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);
if(code.returncode == 0):
    print('Test 2 proshel uspeshno')
else:
    print('Test 2 error')
    sys.exit(1)

