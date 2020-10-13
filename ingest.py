import requests
import json

def ingest(period=60):
	r = requests.get('http://stream.meetup.com/2/rsvps', stream=True)
	for line in r.iter_lines():
		decoded_line = line.decode('utf-8')
		print(json.loads(decoded_line))

ingest()