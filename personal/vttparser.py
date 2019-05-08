import webvtt
prevline = "HI I AM SHOUTING."
captions = []

from os import listdir
files = listdir("./subs/")

for vttFile in files:
    output = open("./subs/" + vttFile + ".txt", 'w')

    for caption in webvtt.read("./subs/"+vttFile):
        #print(caption.start)
        #print(caption.end)
        
        
        for line in caption.text.split("\n"):
            if line == " ":
                continue
            elif line != prevline:
                output.write(line)
                output.write('\n')
                prevline = line
    output.close()
    
    
"""
print(captions[0])
print("----")
print(captions[1].split('\n'))
print("----")
print(captions[2])
"""
