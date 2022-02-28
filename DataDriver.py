#! /usr/bin/python3


'''
DataDriver.py defines a Simulator class that simulates satellite telemetry
'''

import asyncio
import json
from pathlib import Path
import websockets
import base64


SPACECRAFTID = ''
APID = ''
ORGNAME = ''
PACKETTYPE = ''
DATAURL = ''
websocket = websockets.connect(DATAURL,extra_headers={'Content-Type': 'application/json'})

def send_telemetry_packets(tlm_bytes):
    tag = f'{SPACECRAFTID}.{PACKETTYPE}'

    message = {
        'label': SPACECRAFTID,
        'apid': APID,
        'tlm': base64.b64encode(tlm_bytes).decode('ascii'),
        'tenant': f'{ORGNAME}Data'
    }



    asyncio.get_event_loop().run_until_complete(send_bytes_ws(tag, message))

    
    
async def send_bytes_ws(tag, record):
    async with websocket as ws:
        data = json.dumps(record)

        await ws.send(data)


#############################################
# ADD CODE HERE TO SEND PACKETS TO send_telemetry_packets
############################################
#tlm_bytes = receive_packet_function()

#send_telemetry_packets(tlm_bytes)
