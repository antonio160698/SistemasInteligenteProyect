from flask import render_template
from app import app
import io
import os
import cv2
#from google.cloud import vision_vlp3betal as vision_vlp3betal
from datetime import datetime

@app.route('/example')
def example():
    URL = 'https://api.openweathermap.org/data/2.5/'
    key = 'b1ffe3330b6cdb03e70a9e5842a7f0b1'
    return render_template('example.html', API_URL=URL, API_KEY=key)