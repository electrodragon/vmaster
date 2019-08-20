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
    pass

class RecordingCore():
    pass
