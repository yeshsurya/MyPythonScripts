try:
 import thread
except:
 """ We're running on a single-threaded OS (or the Python
interpreter has
 not been compiled to support threads), so return a
standard dictionary. """
 _tss = {}
 def get_thread_storage( ):
    return _tss
else:
 """ We do have threads; so, to work: """
 _tss = {}
 _tss_lock = thread.allocate_lock( )   #Return a new lock object  # Return a new lock object
 def get_thread_storage( ):
    """ Return a thread-specific storage dictionary. """
    thread_id = thread.get_ident( ) # Identify the calling thread # Return the ‘thread identifier’ of the current thread. Thread identifiers may be recycled when a thread exits and another thread is created.
    tss = _tss.get(thread_id)
    #if tss is None: # First time being called by this thread
    try: # Entering critical section
     _tss_lock.acquire( )   # this method acquires the lock unconditionally,
     _tss[thread_id] = tss = {} # Create threadspecific dictionary # this map holds the address of data allocated for each thread.
    finally:
        _tss_lock.release( )
        return tss