import os, time

# shows how to set up a pipe between two python scripts

# run with
#   python pipe-background.py &
# and then run
#   python pipe-foreground.py
#
# ctrl-c to exit foreground
#
# ps -aux | grep pipe
#   lists pid
# sudo kill <pid>


pipe_name = "/tmp/mypipe"

pipe = open(pipe_name, 'w', 1)
pipe.write("opening pipep\n")

i = 0
while True:
    time.sleep(1)

    pipe.write("sending message " + str(i) + "\n")
    i += 1
