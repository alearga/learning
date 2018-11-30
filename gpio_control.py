from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)


if button.wait_for_press():
    led.on()
    print('You pushed me')
else:
    print("you suck at coding")
sleep(2)
if button.wait_for_press():
   led.off()
   print("You did it again...")
else:
    print("you suck at coding")
#button.wait_for_press()
#print('You pushed me')
#led.on()
#sleep(2)
#led.off()