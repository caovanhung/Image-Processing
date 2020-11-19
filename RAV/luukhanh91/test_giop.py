import RPi.GPIO as GPIO
import time

# Pin Definitions
#output_pin = 27  # BOARD pin 12, BCM pin 18
output_pin =22
output_pin1 =27
output_pin2 =17
def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BCM)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(output_pin1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(output_pin2, GPIO.OUT, initial=GPIO.HIGH)    
    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.LOW

    GPIO.output(output_pin, curr_value)
    GPIO.output(output_pin1, curr_value)
    GPIO.output(output_pin2, curr_value)

if __name__ == '__main__':
    
     main()
