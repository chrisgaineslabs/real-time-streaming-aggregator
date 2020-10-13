import signal

def processdata(event):
	eventTime = event['event']['time']
	eventUrl = event['event']['event_url']
	eventCountry = event['group']['group_country']
	return eventTime, eventUrl, eventCountry


# each event we need the following info

## event['event']['time']

## event['event']['event_url']

## event['group']['group_country']

# count the following

## total number of rsvps in the time period

## the count of each group country during the time period

# the data should be in the following format

## total,future_date,future_url,co_1,co_1_count,co_2,co_2_count,co_3,co_3_count

