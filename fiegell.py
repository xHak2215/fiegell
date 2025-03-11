import os,sys,time
import keyboard 
#import subprocess

files=os.listdir()
style="\033[4m\033[37m\033[44m{}"
cursor=0

while True:
    cours=''
    file_list=[]
    index=0
    out=''
    files=os.listdir()
    for i in range(0,len(files)):
        otstup='                         '[len(files[i])+len(str(index)):]
        ves=os.path.getsize(files[i])
        if cursor==i:
            cours=">"
        else:
            cours=''
        out+=f"{cours}{index} {files[i]}{otstup} bite {ves}\n"
        file_list.append(files[i])
        index=index+1
    if cursor>index:
        cursor=0
    if cursor>=len(file_list):
        cursor=len(file_list)
#This part of the code is creating a command-line interface within the Python script. When the 'Esc'
#key is pressed, the program enters a loop where it continuously waits for user input. The user can
#enter various commands such as changing directories ('cd'), deleting files or directories ('rm' or 'del'), searching for files by number (':','file'), or printing the current working directory ('pwb').
    if keyboard.is_pressed('down'):
        cursor=cursor+1
    if keyboard.is_pressed('up'):
        cursor=cursor-1
    if cursor<0:
        cursor=0
    if keyboard.is_pressed('enter'):
        if os.path.isdir(files[cursor]):    
            os.chdir(files[cursor])
        if os.path.isfile(files[cursor]):
            file=open(files[cursor],"rb")
            print(file.read())
            file.close()
    if keyboard.is_pressed('left'):
        os.chdir('..')
            
    if keyboard.is_pressed('Esc'):
        while True:
            command=input('>>')
            if keyboard.is_pressed('Esc') or command=='e':#выход
                break
            elif command=='exit':
                exit('bue')
            elif command.startswith("cd"):#переход по директориям
                try:
                    directory_name = command.split(" ")[1]
                    os.chdir(directory_name)
                except FileNotFoundError:
                    print("error file 1")
            elif command.startswith("rm") or command.startswith("del"):#удоление файла/директории
                try:
                    directory_name = command.split(" ")[1]
                    os.rmdir(directory_name)
                except FileNotFoundError:
                    print("error file 1")
            elif command.startswith(":") or command.startswith("file"):#поиск файлов по номеру
                try:
                    numner_file=command.split(':')[1]
                    print(file_list[int(numner_file)])
                except IndexError :
                    print("error no file number")
            elif command.startswith('pwb') or command.startswith('dir'):
                print(os.getcwd())
            else:
                print('error no command')
        else:
            exit('exit')
            
    #time.sleep(0.6)
    os.system('clear')
    print(style.format(out))