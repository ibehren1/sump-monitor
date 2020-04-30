#!/usr/bin/env python3
import boto3
import datetime
import RPi.GPIO as GPIO
import time


class Accumulator:
    # Define the init function to setup private attributes
    def __init__(self, value):
        self.__value = value

    def reset(self):
        self.__value = 0

    def accumulate(self, value):
        self.__value += value

    def getValue(self):
        return self.__value


# Setup Boto Client
client = boto3.client('cloudwatch', 'us-east-2')

# GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    if GPIO.input(channel):
        accumObj.accumulate(1)
    else:
        accumObj.accumulate(1)


def logToCloudwatch(rate):
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
                'Value': rate,
                'Unit': 'Count',
                'StorageResolution': 1
            },
        ]
    )


# let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel, callback)


# Open file for logging
with open("/home/ibehr/sump_data.csv", 'a', encoding='utf-8') as f:

    accumObj = Accumulator(0)

    # infinite loop
    while True:
        # Reset the accumulator
        accumObj.reset()

        # Sleep 1 minute while accumulating montion
        time.sleep(60)

        # Log accumulated motions to Cloudwatch and write to file
        logToCloudwatch(accumObj.getValue())

        line = str(datetime.datetime.now()) + "," + \
            str(accumObj.getValue()) + "\n"
        f.write(line)

        f.flush()
