import os, time

pipe_name = "/tmp/mypipe"

print("starting foreground pipe")
no_pipe = True
while no_pipe:
    try:
        print("file exists")
        pipe = open(pipe_name, 'r')
        no_pipe = False
    except:
        sleep_time(1)
        pass

print("looping")
while True:

    received = pipe.readline()[:-1]
    if received != "":
        print("   msg = " + received)
