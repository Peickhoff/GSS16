class Semaphore():
    def __init__(self):
        self.W = 1 # Lock can be acquired
        self.NumberOfActiveReaders = 0 # No Active Readers
        self.Mutex = 1 # Changing NumberOfActiveReaders allowed

    @synchronized
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

    @synchronized        
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
    # Static Variable semaphore
    semaphore = []

    def __init__(self, s):
        self.semaphore = s

    def processReader(self):
        # Try to acquire Lock
        if self.semaphore.P(self):
            self.readData()
            self.semaphore.V(self)
        else:
        # Retry to acquire Lock
            self.processReader()

    def readData(self):
        # Insert Read Data


class Writer():
    # Static Variable semaphore
    semaphore = []

    def __init__(self, s):
        self.semaphore = s

    def processWriter(self):
        # Try to acquire Lock
        if self.semaphore.P(self):
            self.writeData()
            self.semaphore.V(self)
        else:
        # Retry to acquire Lock
            self.processWriter();

    def readData(self):
        # Insert Write Data
