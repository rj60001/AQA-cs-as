'''Command list definition. Dictionary definition used.'''

import time

commandList = {
    'help' : "Here is the list of commands possible: 'time' - Check the time. 'project - set' - Set your current project. 'project - get' - Get your current project. 'reminder' - Set a reminder. 'play - audio' - Play a nested audio file. 'play - video' - Play a nested video file(INVALID - DO NOT USE). 'file - write': Write to a new file. 'file - read': Read from a file and print it's contents. 'file - edit': Edit a currently existing file." ,
    'time' : 'The time is: '+str(time.asctime(time.localtime(time.time())))
}