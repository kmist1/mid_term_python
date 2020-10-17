import time

def time_take(func):
    def inner(*args):
        start = time.time()*1000
        s = func(*args)
        end = time.time()*1000
        with open("log.txt","a") as log_file:
            log_file.write("Time took: {}\n".format(end-start))
        return s
    return inner
