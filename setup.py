import os,platform
dire=str(os.path.dirname(os.path.abspath(__name__)))
requirements=open("requirements.txt","r",encoding="UTF-8")
libd = [libd.rstrip() for libd in requirements]
if platform.system() =='Linux':
    os.system('python3 -m venv menadger')
    os.chdir('menadger')
    os.system('python.exe -m pip install --upgrade pip')
    os.system('source bin/activate')
    os.chdir(dire)
    for i in range(0,len(libd)):
        print(f'install lib >> {libd[i]}')
        os.system(f'pip install {libd[i]}')
if platform.system() =='Windows':
    os.system('python -m venv menadger')
    os.chdir('menadger')
    os.system('python.exe -m pip install --upgrade pip')
    os.chdir('Scripts')
    os.system('start activate.bat')
    os.chdir(dire)
    for i in range(0,len(libd)):
        print(f'install lib >> {libd[i]}')
        os.system(f'pip install {libd[i]}')
else:
    print('error you OS Not supported')       
    
    