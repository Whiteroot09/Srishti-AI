import time
from os import startfile
from keyboard import write
from pynput.keyboard import Key, Controller
from time import sleep
def programfile(code, name, exten):
    if 'python' in exten:
        exten = 'py'
    elif 'java' in exten:
        if 'public class' in code:
            code = code.replace('public class', 'class')
        exten = 'java'
    elif 'c' in exten:
        exten = 'c'
    else:
        exten = 'txt'
    file = open(f'C:\\Users\\arnab\\OneDrive\\Documents\\SRISHTI MAKE CODE\\{name}.{exten}', 'w')
    file.write(code)
    print(f'The path where the program save -> C:\\Users\\arnab\\OneDrive\\Documents\\SRISHTI MAKE CODE\\{name}.{exten}')

# keyboard = Controller()
# time.sleep(2)
# write('d:')
# sleep(2)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
# programfile('abcd')
# programfile('Hi', 'text', 'C')
