import RPi.GPIO as GPIO 
import time



class buzzer():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.p = GPIO.PWM(self.pin, 50)
        self.p.start(100)

    def play(self, sound, reps=1):
        if sound == "police_siren":
            i = 1000
            p = GPIO.PWM(self.pin, 50)
            GPIO.output(self.pin, True)
            p.start(100)
            p.ChangeDutyCycle(90)
            for n in range(reps):
                while i <= 10000:
                    p.ChangeFrequency(i)
                    i += 1
                    time.sleep(0.0001)
                while i >= 1000:
                    p.ChangeFrequency(i)
                    i -= 1
                    time.sleep(0.0001)
            p.stop()  
        if sound == "gameshow":
            self.p.ChangeFrequency(2000)
            for n in range(reps):
                self.p.ChangeDutyCycle(90)
                time.sleep(0.2)
                self.p.ChangeDutyCycle(100)
                time.sleep(0.3)
            self.p.stop()
