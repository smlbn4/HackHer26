
import time
class stopwatch:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.running = False
        self.elasped_time = 0

    def start(self): #return nothing
        self.start_time = time.time()
        self.running = True

    def stop(self): #return nothing
        self.running = False
        self.stop_time = time.time()

    def elapsedTime(self): #return time elapsed
        return (self.stop_time - self.start_time)/360

    def reset(self): #return nothing
        self.start_time = 0
        self.running = False


if __name__ == "__main__":
    print("hello")
    s = stopwatch()
    s.start()
    s.stop()
    print(s.elapsedTime())
    s.reset()

