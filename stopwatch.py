
import time
class stopwatch:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.running = False
        self.elasped_time = 0

    def start(self): #return nothing
        self.start_time = time.time()
        print(self.start_time)
        self.running = True

    def stop(self): #return nothing
        self.stop_time = time.time()
        print(self.stop_time)
        self.running = False

    def elapsedTime(self): #return time elapsed
        self.elapsed_time = (self.stop_time - self.start_time)/360
        return self.elapsed_time

    def reset(self): #return nothing
        self.start_time = 0
        self.stop_time = 0
        self.elapsed_time = 0
        print(self.start_time, self.stop_time,self.elapsed_time)


if __name__ == "__main__":
    print("hello")
    s = stopwatch()
    s.start()
    s.stop()
    print(s.elapsedTime())
    s.reset()

