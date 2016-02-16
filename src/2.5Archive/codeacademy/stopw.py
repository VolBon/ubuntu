import time as tm
class Watch:
    count = 0
    description = "Stopwatch class object (default description)"
    author = "Author not yet set"
    name = "not defined"
    instances = []
    def __init__(self,name="not defined"):
        self.name = name
        self.elapsed = 0.
        self.mode = 'init'
        self.starttime = 0.
        self.created = tm.strftime("%Y-%m-%d %H:%M:%S", tm.gmtime())
        Watch.count += 1

    def __call__(self):
        if self.mode == 'running':
            return tm.time() - self.starttime
        elif self.mode == 'stopped':
            return self.elapsed
        else:
            return 0.

    def display(self):
        if self.mode == 'running':
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.elapsed = 0.
        elif self.mode == 'stopped':
            pass
        else:
            pass
        print "Name:       ", self.name
        print "Address:    ", self
        print "Created:    ", self.created
        print "Start-time: ", self.starttime
        print "Mode:       ", self.mode
        print "Elapsed:    ", self.elapsed
        print "Description:", self.description
        print "Author:     ", self.author

    def start(self):
        if self.mode == 'running':
            self.starttime = tm.time()
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.starttime = tm.time()
            self.mode = 'running'
            self.elapsed = 0.
        elif self.mode == 'stopped':
            self.mode = 'running'
            #self.elapsed = self.elapsed + tm.time() - self.starttime
            self.starttime = tm.time() - self.elapsed
        else:
            pass
        return

    def stop(self):
        if self.mode == 'running':
            self.mode = 'stopped'
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.mode = 'stopped'
            self.elapsed = 0.
        elif self.mode == 'stopped':
            pass
        else:
            pass
        return self.elapsed

    def lap(self):
        if self.mode == 'running':
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.elapsed = 0.
        elif self.mode == 'stopped':
            pass
        else:
            pass
        return self.elapsed

    def reset(self):
        self.starttime=0.
        self.elapsed=0.
        self.mode='init'
        return self.elapsed

def WatchList():
    return [i for i,j in zip(globals().keys(),globals().values()) if '__main__.Watch instance' in str(j)]