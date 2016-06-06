class Semaphore():
    def __init__(self):
        self.W = 1
        self.NumberOfActiveReaders = 0
        self.Mutex = 1

    def P(self, caller):
        type = caller.__class__.__name__
        if type == "Reader":
            if self.Mutex > 0
                if self.NumberOfActiveReaders == 0:
                    self.W = 0
                self.Mutex = 0
                self.NumberOfActiveReaders+=1
                self.Mutex = 1
                return true
            else:
                return False
        elif type == "Writer":
            if self.W > 0:
                self.W = 0
                return True
            else:
                return False
        else:
            return False

    def V(self, caller):
        type = caller.__class__.__name__
        if type == "Reader":
            if self.Mutex > 0
                self.Mutex = 0
                self.NumberOfActiveReaders-=1
                if self.NumberOfActiveReaders == 0:
                    self.W = 1
                self.Mutex = 1
                return true
            else:
                return False
        elif type == "Writer":
            self.W = 0
        else:
            return False


class Reader():
    semaphore = []

    def __init__(self, s):
        self.semaphore = s

    def processReader(self):
        if self.semaphore.P(self):
            self.readData()
            self.semaphore.V(self)
        else:
            self.processReader()

    def readData(self):
        # Insert Read Data


class Writer():
    semaphore = []

    def __init__(self, s):
        self.semaphore = s

    def processWriter(self):
        if self.semaphore.P(self):
            self.writeData()
            self.semaphore.V(self)
        else:
            self.processWriter();

    def readData(self):
        # Insert Write Data
