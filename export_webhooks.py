from datetime import datetime, timedelta
import requests
import time
import csv
import json

# API Key
credentials = ['_rRnSAig[REDACTED]']

page_size = 25
start_record = 1

def get_webhooks(credentials, page_size, start_record):
    print("[{timestamp}] Getting webhooks at {start_record}".format(timestamp=datetime.now(), start_record=start_record))
    url = 'https://rally1.rallydev.com/apps/pigeon/api/v2/webhook?pagesize={page_size}&start={start_record}'.format(page_size=page_size, start_record=start_record)
    cookies = {
        'ZSESSIONID': credentials[0]
    }
    response = requests.get(url, cookies=cookies).json()
    return response

webhook_file = open('webhooks.csv', 'w')
csv_writer = csv.writer(webhook_file)
x = 0

response = get_webhooks(credentials, page_size, start_record)
webhooks = response['Results']
total_result_count = response['TotalResultCount']

for webhook in webhooks:
    if x == 0:
        header = webhook.keys()
        csv_writer.writerow(header)
        x += 1
    csv_writer.writerow(webhook.values())

while start_record + page_size < total_result_count:
    start_record = start_record + page_size
    response = get_webhooks(credentials, page_size, start_record)
    webhooks = response['Results']

    for webhook in webhooks:
        csv_writer.writerow(webhook.values())
