#!/usr/bin/env python3

import os
import sys
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

column, reps, limit = [int(x) for x in sys.argv[1:]]
head = sys.stdin.readline().split()[column]

count = 0
for i, line in enumerate(sys.stdin): 
    if int(line.split()[column]) > limit and i != 0: 
        count += 1 
    else: 
        count = 0 
    if count >= reps: 
        message = client.messages \
            .create( 
                body='check ' + head, 
                from_='+12057408930', 
                to='+14082508329' 
            )

print(message.sid)