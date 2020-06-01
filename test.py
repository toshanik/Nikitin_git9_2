import time
import sys
import subprocess

#тест1
code = subprocess.run('python project.py 50', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);
if(code.returncode == 0):
    print('Тест 1 прошел успешно')
else:
    print('Тест 1 ошибка')
    sys.exit(1)

#тест2
code = subprocess.run('python project.py Карусель', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);
if(code.returncode == 0):
    print('Тест 2 прошел успешно')
else:
    print('Тест 2 ошибка')
    sys.exit(1)


# code = subprocess.run(['C:\python\python.exe', 'sub.py', '50'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

