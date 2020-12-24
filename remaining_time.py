#!/usr/bin/env python3

from datetime import datetime

seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60


class days_hours_minutes_seconds:
	def __init__(self, days, hours, minutes, seconds):
		self.days = days
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
		
		
def get_dhms_from_seconds(secs):
	days = int(secs / seconds_in_day)
	secs -= days * seconds_in_day
	
	hours = int(secs / seconds_in_hour)
	secs -= hours * seconds_in_hour
	
	minutes = int(secs / seconds_in_minute)
	secs -= minutes * seconds_in_minute
	
	secs = int(secs)
	return days_hours_minutes_seconds(days, hours, minutes, secs)


def print_remaining_dhms(label, dhms):
	print(
		"{1:2} days, {2:2} hours, {3:2} minutes, {4:2} seconds until {0}".format(
			label, dhms.days, dhms.hours, dhms.minutes, dhms.seconds
		)
	)
	
	
right_now = datetime.now()
new_years_day = datetime(2021, 1, 1, 0, 0, 0)
inauguration_day = datetime(2021, 1, 20, 12, 0, 0)

diff = new_years_day - right_now
secs = diff.total_seconds()
time_remaining_until = get_dhms_from_seconds(secs)
print_remaining_dhms("suckass 2020 ends", time_remaining_until)

diff = inauguration_day - right_now
secs = diff.total_seconds()
time_remaining_until = get_dhms_from_seconds(secs)
print_remaining_dhms("that punk-ass bitch leaves the White House", time_remaining_until)
