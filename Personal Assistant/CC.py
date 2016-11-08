import CL
import datetime
import os
import winsound
global reminder
global remindersTime
reminders = []
remindersTime = []
global project
project = 'NULL'
now = datetime.datetime.now()   

def commandCentre():
    command = input("Hey, I am Eliza! What can I help you with? All commands must be prefixed with a ']' If you need help, please type: 'help'.")
    #Reminders.
    for i in range(0, len(reminders)):
        if now.minute == remindersTime[i]:
            if i == len(reminders)-1:
                print(reminders[i]+'.')
            else:
                print(reminders[i]+', ')
            reminders.remove(i)
            remindersTime.remove(i)
    #Main loop.
    while True:
        while command[0:1] != ']':
            command = input("All commands must be prefixed with a ']'.")
        commandLen = len(command)
        command = command[1:commandLen].lower()

        if command[0:7] == 'project':
            if command[8:14] == "- set":
                project = input('Project name: ')
            elif command[8:14] == "- get":
                print(project)
        elif command == 'reminder':
            reminder = input('What is the reminder?')
            reminders.append(reminder)
            reminderTime = input('How many minutes in advance should you be reminded for?')
            remindersTime.append(int(reminderTime)+now.minute)
            print('Reminder set!')
        elif command[0:4] == "play":
            if command[5:13] == "- audio":
                file = input('Which file would you like to play?')
                winsound.PlaySound(file, winsound.SND_FILENAME)
        elif command[0:4] == "file":
            if command[5:13] == "- write":
                filename = input('What is the file name? ')
                while filename[0] == ']':
                    filename = input('Enter a valid file name (no command prefix required): ')
                file = open(filename+'.txt', 'w')
                text = input('Please type in the relevant text: ')
                file.write(text)
                file.close()
                print('Success!')
            elif command[5:13] == "- read":
                filename = input('Please specify the file name: ')
                while filename[0] == ']':
                    filename = input('Enter a valid file name (no command prefix required): ')
                file = open(filename+'.txt', 'r')
                print(file.read())
                file.close()
                print('Success!')
            elif command[5:13] == "- edit":
                filename = input('Please specify the file name: ')
                while filename[0] == ']':
                    filename = input('Enter a valid file name (no command prefix required): ')
                file = open(filename+'.txt', 'r+')
                print(file.read())
                text = input('New text (WARNING! This will add text the file): ')
                file.write(text)
                file.close()
                print('Success!')
            elif command[5:15] == "- delete":
                filename = input('Please specify the file name: ')
                while filename[0] == ']':
                    filename = input('Enter a valid file name (no command prefix required): ')
                os.remove(filename+'.txt')
                print('Success!')
        elif command[0:28] == "what is the meaning of life?":
            print('42')
        else:
            for cmd in CL.commandList:
                if cmd == command:
                    print(CL.commandList[command])
