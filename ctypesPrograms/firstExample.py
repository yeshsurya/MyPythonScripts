from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello world\n"
msvcrt.printf(message_string)