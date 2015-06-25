import os

while True:
    name = str(input("Hi, please type in the name of the file to record: "))
    name = name+".h264"
    os.system("raspivid -w 800 -h 600 -fps 90 -t 10000 -o "+name)
    os.system("omxplayer "+name)
