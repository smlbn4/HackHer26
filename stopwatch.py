import time

class Stopwatch:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        #self.running = False
        self.elasped_time = 0

    def start(self): #return nothing
        self.start_time = time.time()
        print(self.start_time)

    def stop(self): #return nothing
        self.stop_time = time.time()
        print(self.stop_time)

    def elapsedTime(self): #return time elapsed
        self.elapsed_time = self.start_time - self.stop_time 
        return self.elapsed_time

    def reset(self): #return nothing
        self.elapsed_time = 0

if __name__ == "__main__":
    stopwatch = Stopwatch()

