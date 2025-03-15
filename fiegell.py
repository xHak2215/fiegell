import os,sys,time
import keyboard 
#import subprocess

files=os.listdir()
cursor=0

#setings
kast='>'
style="\033[4m\033[37m\033[44m{}"
open_file_is_bin=False

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
            cours=kast
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
#Cursor shift using the arrow (↑ ↓) transition or opening a file using the Enter key return to the last directory ←
#сдвиг курсора с помощью стрелочек ( ↑  ↓ ) переход или открытие файла с помощью клавиши Enter возврат в прошлую директорию ← 
    if keyboard.is_pressed('down'):
        cursor=cursor+1
    if keyboard.is_pressed('up'):
        cursor=cursor-1
    if cursor<0:
        cursor=0
    if keyboard.is_pressed('enter'):
        if os.path.isdir(os.getcwd()+'/'+files[cursor]):    
            os.chdir(os.getcwd()+'/'+files[cursor])
        if os.path.isfile(os.getcwd()+'/'+files[cursor]):
            file=open(os.getcwd()+'/'+files[cursor],"rb" if open_file_is_bin else 'r')
            while True:
                if keyboard.is_pressed('Esc'):
                    break
                print(file.read())
                
                os.system('clear')
            file.close()
            #print(os.access(os.getcwd()+'/'+files[cursor],os.X_OK))
    if keyboard.is_pressed('left'):
        os.chdir('..')
    if keyboard.is_pressed('Esc'):
        while True:
            command=input(kast)
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
            elif command.startswith("python"):#запуск пайтон програм 
                file = command.split(" ")[1]
                if os.path.isfile(file):
                    os.system(f'python {file}')
                else:
                    print("error file 1")
            elif command.startswith("rm") or command.startswith("del"):#удоление файла/директории
                try:
                    directory_name = command.split(" ")[1]
                    os.remove(directory_name)
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
            elif command.startswith("") or command.startswith(" "):
                break
            else:
                print('error no command')
        else:
            exit('exit')
            
    #time.sleep(0.6)
    os.system('clear')
    print(style.format(out))
