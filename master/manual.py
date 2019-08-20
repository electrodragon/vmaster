class manual_msg():
    def __init__(self):
        self.s  = "\n   Video Master ( vmaster )\n"
        self.s += "\n:: Usage:\n   vmaster [options] <files...>\n"
        self.s += "\n:: Options:\n"
        self.s += "   --help       | Shows This Help Screen\n"
        self.s += "   --ea         | Extracts Audio From Video\n"
        self.s += "   --ra         | Removes Audio From Video\n"
        self.s += "   --jav        | Joins Audio Video\n"
        self.s += "   --cat        | Concats Audio or Video Tracks\n"
        self.s += "   --cut        | Cuts Video at Provided Durations\n"
        self.s += "   --rec        | Records Video While Streaming\n"
        self.s += "\n:: Examples: \n"
        self.s += "   $ vmaster --ea \'videofile.mp4\'\n"
        self.s += "   $ vmaster --jav \'videofile.mp4\' \'audioFile.aac\'\n"
        self.s += "   $ vmaster --cat \'v1.mp4\' \'v2.mp4\' \'vN.mp4\'\n"
    def __str__(self):
        return self.s
    
