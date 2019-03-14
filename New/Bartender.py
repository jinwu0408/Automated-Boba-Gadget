# Initialize adaFruit
execfile('confAda.py')
width = disp.width-1
height = disp.height-1

from drinks import drink_list
from pumpconfig import pump
import RPi.GPIO as GPIO


# Button Pins
# Can be changed to any IO pin
button1 = 5 #pin29
button2 = 6 #pin31
pump1 = 18 #pin12
pump2 = 17 #pin11
current_selection = 0
drink1_name = drink_list[0]["name"]
drink2_name = drink_list[1]["name"]
drink_disp_list = [drink1_name,drink2_name]
drink1_ingredient = drink_list[0]["ingredients"]
drink2_ingredient = drink_list[1]["ingredients"]

def initial():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for key, value in pump.items():
        GPIO.setup(value, GPIO.OUT)


def next_item(current_selection):
    if current_selection == 0:
        current_selection =+ 1
        #print(current_selection)
        updateDisplay(drink_disp_list[current_selection])
        return current_selection
    else:
        current_selection = 0
        updateDisplay(drink_disp_list[current_selection])
        return current_selection

def updateDisplay(string):
    # Draw a black filled box to clear the image.
    # Pixel count origin at upper left corner
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    #draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
    #draw.text((x, top+8),     str(CPU), font=font, fill=255)
    #draw.text((x, top+16),    str(MemUsage),  font=font, fill=255)
    #draw.text((x, top+25),    str(Disk),  font=font, fill=255)
    #draw.text((x, top),     "PUT SOME TEXT RIGHT HERE", font=font, fill=255)
    
    draw.text((x,top+8),    string, font=font, fill=255)
    print (string)
    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)

def dispense(drinks):#0 or 1
    #Turn on the pump for t
    #Then turn off
    pump_name = []
    pump_time = []
    drink_ingredient = drink_list[drinks]["ingredients"]
    for key, value in drink1_ingredient:
        pump_name.append(pump.get(key))
        time = 3*value
        pump_time.append(time)
    num_pump = len(pump_name)
    
    for i in range(num_pump):
        GPIO.output(pump_name[i], GPIO.HIGH)#turn on
    
    
    
    
    
    
    GPIO.output(pump, GPIO.HIGH)#turn on
    time.sleep(t)
    GPIO.output(pump, GPIO.LOW)#turn off
    
    if(drinkType):
        output-strawberry=1
        output-milktea=1
        wait25
        output-milktea=0
        wait50
        output-milk
        

initial()

while False:
    try:
        # Button1 pressed
        # Dispense drink
        button1_state = GPIO.input(button1)
        button2_state = GPIO.input(button2)
        if(button_state1 == GPIO.HIGH):
            print('btn 1 pressed')
            dispense(current_selection)

         
        # Button2 pressed
        # Go to next menu item
        # call next_item()
        if(button_state2 == GPIO.HIGH):
            current_selection = next_item(current_selection)
            print('btn 2 pressed')
            time.sleep(1)
    except:
        GPIO.cleanup()
