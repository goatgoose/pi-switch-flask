from flask import Flask
from RPi import GPIO

app = Flask(__name__)


# Define pins (Red, Yellow)
LED_PIN = 21

# GPIO configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)


@app.route("/light_on")
def light_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return "ok"


@app.route("/light_off")
def light_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return "ok"


if __name__ == '__main__':
    app.run()
