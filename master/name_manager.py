class Renamer():
    def __init__(self, name):
        self.extension = name.split('.')[-1]
        self.name = name[:-len(self.extension)-1]
        self.filename = self.name
        self.bashName = name.replace("\'","\'\\\'\'")
    def rename(self):
        import os
        i = 1
        if os.path.exists(self.filename+'.'+self.extension):
            while os.path.exists(self.filename+'.'+self.extension):
                self.filename = '{} ({})'.format(self.name,i)
                i += 1
        return self.filename+'.'+self.extension
