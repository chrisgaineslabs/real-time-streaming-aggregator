import signal

def processdata(event):
	eventTime = event['event']['time']
	eventUrl = event['event']['event_url']
	eventCountry = event['group']['group_country']
	return eventTime, eventUrl, eventCountry


# count the following

## the count of each group country during the time period

# the data should be in the following format

## total,future_date,future_url,co_1,co_1_count,co_2,co_2_count,co_3,co_3_count

