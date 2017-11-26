from queue import Queue
from threading import Thread
data="communcationData"
# Object that signals shutdown
_sentinel = object()
# A thread that produces data
def producer(out_q):
    while out_q.running:
    # Produce some data
        out_q.put(data)
 # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)


# A thread that consumes data
def consumer(in_q):
    while True:
    # Get some data
        data = in_q.get()
    # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
        break
    # Process the data