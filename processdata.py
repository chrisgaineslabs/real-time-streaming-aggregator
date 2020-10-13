from ingest import ingest
import signal

def processdata(event, context):
	print(ingest()[0])