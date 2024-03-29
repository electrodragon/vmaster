class MediaCore():
    import os, sys
    from master.colours import Terminal_color as color
    from master.name_manager import Renamer
    def __init__(self,name):
        self.name = name
    def extRemCombo(self):
        MediaCore.os.system('ffprobe -show_streams \'{}\' -loglevel quiet | grep codec_name'.format(MediaCore.Renamer(self.name).bashName))
        self.extOut = input("Output Extension: ")
        self.extRemOutName = MediaCore.Renamer(MediaCore.Renamer(self.name).name+'.'+self.extOut).rename()
    def extractAudio(self):
        MediaCore.extRemCombo(self)
        MediaCore.os.system('ffmpeg -i \'{}\' -vn -c:a copy \'{}\''.format(MediaCore.Renamer(self.name).bashName,MediaCore.Renamer(self.extRemOutName).bashName))
        print(MediaCore.color.GREEN+'Output File: '+self.extRemOutName+MediaCore.color.ENDC)
    def removeAudio(self):
        MediaCore.extRemCombo(self)
        MediaCore.os.system('ffmpeg -i \'{}\' -c copy -an \'{}\''.format(MediaCore.Renamer(self.name).bashName,MediaCore.Renamer(self.extRemOutName).bashName))
        print(MediaCore.color.GREEN+'Output File: '+self.extRemOutName+MediaCore.color.ENDC)

class CatCore():
    def __init__(self,names):
        self.name = names
    def joinAV(self):
        self.outExt = input("Output Extension: ")
        self.outName = MediaCore.Renamer(MediaCore.Renamer(self.name[0]).name+'.'+self.outExt).rename()
        self.name[0] = MediaCore.Renamer(self.name[0]).bashName
        self.name[1] = MediaCore.Renamer(self.name[1]).bashName
        MediaCore.os.system('ffmpeg -i \'{}\' -i \'{}\' -codec copy -shortest \'{}\''.format(self.name[0],self.name[1],MediaCore.Renamer(self.outName).bashName))
        print(MediaCore.color.GREEN+'Output File: '+self.outName+MediaCore.color.ENDC)
    def cat(self):
        extensionsSet = set()
        fname = '__vMcAtlIsT.txt'
        f = open(fname,'w+')
        for n in self.name:
            extensionsSet.add(MediaCore.Renamer(n).extension)
            f.write('file \''+n+'\'\n')
        f.close()
        if len(extensionsSet) == 1:
            self.outputFileName = MediaCore.Renamer('output.'+MediaCore.Renamer(self.name[0]).extension).rename()
            MediaCore.os.system('ffmpeg -f concat -i \'{}\' -c copy \'{}\''.format(fname,self.outputFileName))
        MediaCore.os.system('rm '+fname)
        if len(extensionsSet) > 1: MediaCore.sys.exit(MediaCore.color.FAIL+'\n :: Extensions Differ !\n'+MediaCore.color.ENDC)
        if MediaCore.os.path.exists(self.outputFileName): print(MediaCore.color.GREEN+'Output File: '+self.outputFileName+MediaCore.color.ENDC)
        else: MediaCore.sys.exit(MediaCore.color.FAIL+'Failed !'+MediaCore.color.ENDC)

class CutCore():
    def __init__(self,name):
        self.name = name
    def cutClip(self):
        self.startingPoint = input('Starting Point (00:00:00) :')
        self.endingPoint = input('Ending Point (00:00:00) :')
        self.cmd = 'ffmpeg -i \'{}\''.format(MediaCore.Renamer(self.name).bashName)
        if self.startingPoint != '': self.cmd += ' -ss '+self.startingPoint
        if self.endingPoint != '': self.cmd += ' -to '+self.endingPoint
        self.outputFileName = MediaCore.Renamer('cut.'+MediaCore.Renamer(self.name).extension).rename()
        self.cmd += ' -c copy \'{}\''.format(self.outputFileName)
        MediaCore.os.system(self.cmd)
        self.replaceOrignal = input(MediaCore.color.BLUE+':: Replace with Orignal? (y/N) : '+MediaCore.color.ENDC)
        if self.replaceOrignal == 'y' or self.replaceOrignal == 'Y':
            MediaCore.os.system('mv \'{}\' \'{}\''.format(self.outputFileName,MediaCore.Renamer(self.name).bashName))
            self.outputFileName = self.name
        print(MediaCore.color.GREEN+'Output File: '+self.outputFileName+MediaCore.color.ENDC)

class RecordingCore():
    def __init__(self,url):
        self.url = MediaCore.Renamer(url).bashName
    def record(self):
        import random, datetime
        self.date = str(datetime.datetime.utcnow().strftime("%a-%b-%d--%H-%M-%S--%Y-"+str(random.randint(50001,60001))))
        self.quality = input('\n :: Enter Quality ([best], worst, 144, 240, 360): ')
        if self.quality == '':
            print(MediaCore.color.BLUE+" :: No Quality Given, using default [best] !"+MediaCore.color.ENDC)
            self.quality = 'best'
        elif self.quality != 'worst':
            self.quality = '\'bestvideo[height<=?{}]+bestaudio/best\''.format(self.quality)
        self.seek = input('\n :: Start Seek at (00:00:00) : ')
        if self.seek == '':
            print(MediaCore.color.BLUE+" :: No Seek Given, Recording Will Start at 0"+MediaCore.color.ENDC)
            self.seek == ''
        else:
            self.seek = ' --start=\''+self.seek+'\''
        self.recFormat = input('\n :: Recording Extension (mkv): ')
        if self.recFormat == '':
            print(MediaCore.color.BLUE+" :: No Recording Format Given, Using Matroska as Default !"+MediaCore.color.ENDC)
            self.recFormat = 'mkv'
        self.filename = MediaCore.Renamer(self.date+'.'+self.recFormat).rename()
        print('\n{} :: Filename {}= {}{}{}'.format(MediaCore.color.HEADER,MediaCore.color.ENDC,MediaCore.color.GREEN,self.filename,MediaCore.color.ENDC))
        self.cmd = 'mpv --ytdl-format='+self.quality+' \''+self.url+'\''
        self.cmd += ' --no-border --record-file=\''+self.filename+'\''
        self.cmd += self.seek
        self.proceed = input(MediaCore.color.HEADER+"\n :: Proceed (Y/n) "+MediaCore.color.ENDC)
        if self.proceed.lower() == 'y' or self.proceed == '':
            print()
            MediaCore.os.system(self.cmd)
        else:
            MediaCore.sys.exit(MediaCore.color.GREEN+'\n :: GOOD BYE !\n'+MediaCore.color.ENDC)
