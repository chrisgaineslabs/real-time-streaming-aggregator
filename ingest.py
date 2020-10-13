from processdata import processData
import requests
import signal
import json

time_to_run_program = 60 # in secs

def ingest():
	total = 0
	countries_dict = {}
	r = requests.get('http://stream.meetup.com/2/rsvps', stream=True)
	for line in r.iter_lines():
		total += 1
		decoded_line = line.decode('utf-8')
		jsondict = json.loads(decoded_line)
		print(processData(jsondict, total, countries_dict))


class TimeoutException(Exception): #code from https://stackoverflow.com/questions/25027122/break-the-function-after-certain-time
	pass

def timeout_handler(signum, frame):
	raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(time_to_run_program)    
try:
	ingest()
except TimeoutException:
	sdfghj
else:
	signal.alarm(0)