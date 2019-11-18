"""
In this pattern, objects are represented as observers that wait for an event to trigger.
 An observer attaches to the subject once the specified event occurs.
As the event occurs, the subject tells the observers that it has occurred.
"""
"""
    @date   : 11/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @import statement
try:
    import threading
    import time
    import pdb
except ImportError:
    print("module not found: ")


# Class Downloader for thread
class Downloader(threading.Thread):

    # @this is run method got downloading
    def run(self):
        print('downloading')
        for i in range(1, 5):
            self.i = i
            time.sleep(2)
            print('unfunf')
        return 'hello world'


# @class worker for therd
class Worker(threading.Thread):
    # @this is run method for worker
    def run(self):
        # @iterating till 4
        for i in range(1, 5):
            print('worker running: %i (%i)' % (i, t.i))
            # @sleep for 1 second
            time.sleep(1)
            t.join()

            print('done')


# @driver programs
# @creating object of Downloader
t = Downloader()
#  @calling start
t.start()

# @calling sleep for a while
time.sleep(1)

# @setting worker
t1 = Worker()

t1.start()

t2 = Worker()
t2.start()

t3 = Worker()
t3.start()
