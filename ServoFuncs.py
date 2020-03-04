import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

def closeLids():
    gpioPins = [11,12,13,15]    # GPIO pin numbers
    
    GPIO.setmode(GPIO.BOARD)    # use the BOARD numbering system for pins
    GPIO.setup(gpioPins, GPIO.OUT)  # set each channel (pin) in list above to output

    for i in gpioPins:
        lid = GPIO.PWM(i,50)    # create PWM instance at channel i with frequency 50
        lid.start(0)    # start PWM at 0 duty cycle
        lid.ChangeDutyCycle(2.5)    # rotate servo to 0 degrees to make sure it's closed
        sleep(1)    # sleep for a second to allow servo to move
        lid.stop()  # stop PWM

    GPIO.cleanup()  # return all channels used back to inputs
    

def openLid(pinNum):
    gpioPins = [11,12,13,15]    # plastic, glass, paper, aluminum
    lidNum = gpioPins[pinNum]

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(lidNum, GPIO.OUT)

    lid = GPIO.PWM(lidNum,50)
    lid.start(7.5)

    
    lid.ChangeDutyCycle(7.5)    # 90 degrees
    sleep(5)
    lid.ChangeDutyCycle(2.5)
    sleep(1)

    lid.stop()
    GPIO.cleanup()

