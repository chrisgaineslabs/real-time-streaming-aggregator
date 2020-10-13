from ingest import ingest
import signal

# def processdata():
# 	ingest.ingest()

class TimeoutException(Exception):   # Custom exception class
	pass

def timeout_handler(signum, frame):   # Custom signal handler
	raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

signal.alarm(60)    
	# This try/except loop ensures that 
	#   you'll catch TimeoutException when it's sent.
try:
	print(ingest())
except TimeoutException:
	sdfghj
else:
	# Reset the alarm
	signal.alarm(0)