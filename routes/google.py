from flask import render_template
from app import app
import io
import os
import cv2
#from google.cloud import vision_vlp3betal as vision_vlp3betal
from datetime import datetime

@app.route('/example')
def example():
    return render_template('example.html')