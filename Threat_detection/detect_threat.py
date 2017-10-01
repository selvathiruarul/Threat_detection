import io
import os
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
from flask import Flask, render_template, request
import urllib, cStringIO
import urllib
import boto3
from PIL import Image
import requests

app = Flask(__name__)
s3 = boto3.client('s3')

def lambda_handler():
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = 'hackuta-image-recognition'
    key = 'Data/fnb.jpg'
    try:
        response = s3.get_object(Bucket=bucket, Key=key)

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def image_analysis(file_name):
    file_name='https://s3.amazonaws.com/hackuta-image-recognition/Data/fnb.jpg'
    image = types.Image()
    image.source.image_uri = file_name
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    for label in labels:
        print(label)


if __name__ == '__main__':
    file_name = os.path.join(
        os.path.dirname(__file__),
        'download.jpg')
    image_analysis(file_name)
    # lambda_handler()