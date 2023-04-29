import requests
import datetime

calendar_api_url = 'https://your_calendar_api_url.com'
maintenance_days = []

# Get the events from the calendar API
response = requests.get(calendar_api_url)
events = response.json().get('events', [])

# Filter the events to only include maintenance days
for event in events:
    if event['type'] == 'maintenance':
        date_str = event['date']
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        maintenance_days.append(date)

# Print the maintenance days
for day in maintenance_days:
    print(day)
