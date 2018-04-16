"""Netra Vision GCP Library

    Authors:
            Subhojeet Pramanik
            Prateek Singh
"""


import io
import os
from google.cloud import vision
from google.cloud.vision import types 


def detect_faces(img_file=None,Content=None):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()
    if(img_file!=None):
        with io.open(img_file, 'rb') as image_file:
            content = image_file.read()
    elif (Content != None):
        content = Content
    else:
        raise ValueError('Nothing specified in label_captions')
    image = types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    return faces


def detect_text(img_file=None,Content=None):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    if (img_file != None):
        with io.open(img_file, 'rb') as image_file:
            content = image_file.read()
    elif (Content != None):
        content = Content
    else:
        raise ValueError('Nothing specified in label_captions')

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts

def label_captions(img_file=None,Content=None):
    """

    """
    vision_client = vision.ImageAnnotatorClient() 
    if(img_file!=None):
        with io.open(img_file, 'rb') as image_file:
            content = image_file.read()
    elif(Content!=None):
        content=Content
    else:
        raise ValueError('Nothing specified in label_captions')

    # Use Vision to label the image based on content.
    image = vision.types.Image(content=content)
    response = vision_client.label_detection(image=image)
    return response


