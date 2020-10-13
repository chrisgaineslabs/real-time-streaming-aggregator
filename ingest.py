import requests
import signal
import json

def ingest(period=60):
	initlist = []
	r = requests.get('http://stream.meetup.com/2/rsvps', stream=True)
	for line in r.iter_lines():
		decoded_line = line.decode('utf-8')
		jsondict = json.loads(decoded_line)
		print(jsondict)
		# publish(jsondict)

class TimeoutException(Exception):
	pass

def timeout_handler(signum, frame):
	raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(60)    
try:
	ingest()
except TimeoutException:
	sdfghj
else:
	signal.alarm(0)