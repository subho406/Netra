"""Responsible for producing audio output for detected labels


"""

import pyttsx3
import numpy as np
import os


def say(text):
    text_cmd='pico2wave -w .temp.wav "'+text+'" && aplay .temp.wav' 
    os.system(text_cmd)

def speak_face(annotations):
    faces_count=len(annotations)
    if(faces_count>0):
        output_text='Detected '+str(faces_count)+' faces.'
        say(output_text)
    i=1
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    for f in annotations:
        if(likelihood_name[f.joy_likelihood]!='VERY_UNLIKELY'):
            output_text='The face '+ str(i)+' seems Happy!'
            say(output_text)
        else:
            output_text='Face '+str(i)+' has no identifiable expressions.'
            say(output_text)
        i=i+1

def speak_text(annotations):
    Output_text='The Visible text is '

    if (len(annotations)>0):
        say(Output_text)
        i=1
        for t in annotations:
            say('Text '+str(i))
            print(t.description)
            say(t.description)
            i=i+1



def speak_vision_labels(annotations, cuttoff_prob=0.8):
    """
    Speak Labels Detected by the vision api

    :param annotations:
    :param cuttoff_prob:
    :return:
    """
    descriptions = []
    probs = []
    for l in annotations:
        descriptions.append(l.description)
        probs.append(l.score)
    # Say the labels which have high probability
    descriptions = np.array(descriptions)
    probs = np.array(probs)
    to_say_desc = descriptions[probs > 0.8]
    if(to_say_desc.shape[0]>0):
        output_strs=''
        for w in to_say_desc:
            output_strs=output_strs+', '+w
        final_text='Detected, '+output_strs+'.'
        say(final_text)
