from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

import datetime

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/on')
def on():
    print('successful')
    
    led = 17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    GPIO.output(led, GPIO.HIGH)

    return render_template('on.html')

@app.route('/off')
def off():
    print('successful')
    
    led = 17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

    GPIO.output(led, GPIO.LOW)

    return render_template('off.html')

@app.route('/auto')
def auto():
    print('auto activated')

    sensor = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor, GPIO.IN)

    while True:
        isDry = GPIO.input(sensor)
        print(GPIO.input(sensor))
        time.sleep(0.5)

        led = 17

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led, GPIO.OUT)
        

        if isDry:
            GPIO.output(led, GPIO.HIGH)
        else:
            GPIO.output(led, GPIO.LOW)

    
    return render_template('on.html')
@app.route('/get-status')
def getStatus():
    sensor = 21
    led = 17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(sensor, GPIO.IN)

    while True:
        isDry = GPIO.input(sensor)
        if isDry:
            print('DRY')
            GPIO.output(led, GPIO.LOW)
        else:
            print('WET')
            GPIO.output(led, GPIO.HIGH)
        time.sleep(0.5)

@app.route('/plant-web')
def plantWeb():
    return render_template('plant_web.html')