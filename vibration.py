#!/usr/bin/env python3
import boto3
import datetime
import RPi.GPIO as GPIO
import time

# Setup Boto Client
client = boto3.client('cloudwatch', 'us-east-2')

# GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    if GPIO.input(channel):
        line = str(datetime.datetime.now()) + ",Movement Detected!\n"
        f.write(line)
        response = client.put_metric_data(
            Namespace='Sump',
            MetricData=[
                {
                    'MetricName': 'Sump',
                    'Dimensions': [
                        {
                            'Name': 'PumpMotion',
                            'Value': '1'
                        },
                    ],
                    'Value': 2,
                    'Unit': 'Count',
                    'StorageResolution': 1
                },
            ])
        response = client.put_metric_data(
            Namespace='Sump',
            MetricData=[
                {
                    'MetricName': 'Sump',
                    'Dimensions': [
                        {
                            'Name': 'PumpMotion',
                            'Value': '1'
                        },
                    ],
                    'Value': 0,
                    'Unit': 'Count',
                    'StorageResolution': 1
                },
            ])
    else:
        line = str(datetime.datetime.now()) + ",Movement Detected!\n"
        f.write(line)
        response = client.put_metric_data(
            Namespace='Sump',
            MetricData=[
                {
                    'MetricName': 'Sump',
                    'Dimensions': [
                        {
                            'Name': 'PumpMotion',
                            'Value': '1'
                        },
                    ],
                    'Value': 2,
                    'Unit': 'Count',
                    'StorageResolution': 1
                },
            ])
        response = client.put_metric_data(
            Namespace='Sump',
            MetricData=[
                {
                    'MetricName': 'Sump',
                    'Dimensions': [
                        {
                            'Name': 'PumpMotion',
                            'Value': '1'
                        },
                    ],
                    'Value': 0,
                    'Unit': 'Count',
                    'StorageResolution': 1
                },
            ])


# let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel, callback)


# Open file for logging
with open("/home/ibehr/sump_data.csv", 'a', encoding='utf-8') as f:

    # infinite loop
    while True:
        time.sleep(5)
        f.flush()
