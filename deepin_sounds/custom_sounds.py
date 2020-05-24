import os
from os import listdir
from os.path import isfile, join

def getSoundFiles():
    onlyFiles=[f for f in listdir('./') if isfile(join('./',f))]
    soundFiles=[]
    for f in onlyFiles:
        if(f.endswith('.wav')):
            soundFiles.append(f)
    return soundFiles

def backupSounds(soundFiles,location):
    for f in soundFiles:
        os.system('sudo mv '+join(location,f)+' '+join(location,f)+'.bak')
    return

def addNewSound(soundFiles,location):
    for f in soundFiles:
        os.system('sudo cp '+join('./',f)+' '+join(location,f))
    return

def main():
    location='/usr/share/sounds/deepin/stereo/'
    soundFiles=getSoundFiles()
    backupSounds(soundFiles,location)
    addNewSound(soundFiles,location)
    return

if __name__=='__main__':
    main()
