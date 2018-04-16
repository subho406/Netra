#!/usr/bin/env python
"""
Netra Daemon Script.

This script is required to be run on Raspberry Pi device connected to a camera. 
Please note that describe mode requires a Netra_Vision server accessible on a particular IP address. Change the IP address by modifying the global IP variable

"""

import os
import time
import argparse
import requests
import json
from libs.cloud import vision_api
from libs.see import  camera_pi
from libs.nlp import speak
from sys import getsizeof


IP='192.168.43.118:5000'

def face_mode():
    while True:
        start_time = time.time()
        frame = pi_cam.get_frame()
        end = time.time() - start_time
        print('Time taken to capture %fs' % end)
        start_time = time.time()
        label_response = vision_api.detect_faces(Content=frame)
        end = time.time() - start_time
        print('Time taken to inference %fs' % end)
        print(label_response)
        speak.speak_face(label_response)


def describe_mode():
    addr = IP
    test_url = addr + '/describe_image'

    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}
    while True:
        start_time = time.time()
        frame = pi_cam.get_frame()
        end = time.time() - start_time
        print('Time taken to capture %fs' % end)
        start_time = time.time()
        response = requests.post(test_url, data=frame, headers=headers)
        end = time.time() - start_time
        print('Time taken to inference %fs' % end)
        response_data=json.loads(response.text)
        prediction=response_data['data'][0]
        if(prediction['prob']>0.001):
            print(prediction['sentence']+': '+str(prediction['prob']))
            speak.say(prediction['sentence'])


def raw_mode():
    while True:
        start_time = time.time()
        frame = pi_cam.get_frame()
        end = time.time() - start_time
        print('Time taken to capture %fs' % end)
        print('Image size : %d bytes' % getsizeof(frame))
        start_time = time.time()
        label_response = vision_api.label_captions(Content=frame)
        end = time.time() - start_time
        print('Time taken to inference %fs' % end)
        # Gather useful information from the response
        annotations = label_response.label_annotations
        speak.speak_vision_labels(annotations)


def text_mode():
    while True:
        start_time = time.time()
        frame = pi_cam.get_frame()
        end = time.time() - start_time
        print('Time taken to capture %fs' % end)
        print('Image size : %d bytes' % getsizeof(frame))
        start_time = time.time()
        label_response = vision_api.detect_text(Content=frame)
        end = time.time() - start_time
        print('Time taken to inference %fs' % end)
        # Gather useful information from the response
        annotations = label_response
        print(annotations)
        speak.speak_text(annotations)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Start Netra Daemon')
    parser.add_argument('mode',type=str,help='Available modes: raw, face, text, describe')
    args = parser.parse_args()
    mode=args.mode

    print('Starting Netra Daemon')
    print('Initializing Camera')
    speak.say('Initializing Netra Daemon. Please wait!')
    if (mode=='describe'):
       pi_cam=camera_pi.Camera((1280,720))
    else:
       pi_cam=camera_pi.Camera((512,512))
    speak.say('Netra Daemon started! Welcome user!')
    if(mode=='raw'):
        raw_mode()
    elif(mode=='face'):
        face_mode()
    elif(mode=='text'):
        text_mode()
    elif(mode=='describe'):
        describe_mode()


            #print(label_response)

