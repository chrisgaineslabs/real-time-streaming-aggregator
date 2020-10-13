import operator
import itertools

def processData(event, total, eventTime, eventUrl, countries_dict):
	if event['event']['time'] > eventTime:
		eventTime = event['event']['time']
		eventUrl = event['event']['event_url']
	eventCountry = event['group']['group_country']
	if eventCountry in countries_dict:
		countries_dict[eventCountry] += 1
	else:
		countries_dict[eventCountry] = 1
	sorted_d = sorted(countries_dict.items(), key=operator.itemgetter(1),reverse=True)[:3]
	flatten = list(itertools.chain(*sorted_d))
	if len(flatten) == 2:
		co_1, co_1_count = flatten
		return total, eventTime, eventUrl, co_1, co_1_count
	if len(flatten) == 4:
		co_1, co_1_count, co_2, co_2_count = flatten
		return total, eventTime, eventUrl, co_1, co_1_count, co_2, co_2_count
	if len(list(flatten)) == 6:
		co_1, co_1_count, co_2, co_2_count, co_3, co_3_count = flatten
		return total, eventTime, eventUrl, co_1, co_1_count, co_2, co_2_count, co_3, co_3_count