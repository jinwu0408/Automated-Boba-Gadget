# Initialize adaFruit
#execfile('confAda.py')
execfile("/home/pi/Desktop/AutomatedBobaGadget/image.py")
execfile("/home/pi/Desktop/AutomatedBobaGadget/confAda.py")

disp.clear()
disp.display()

width = disp.width-1
height = disp.height-1

from drinks import drink_list
from pumpconfig import pump
import RPi.GPIO as GPIO


# Button Pins
# Can be changed to any IO pin
button1 = 5 #pin29
button2 = 6 #pin31
bobaLever = 21 #pin40
pump1 = 18 #pin12
pump2 = 17 #pin11
current_selection = 0
drink1_name = drink_list[0]["name"]
drink2_name = drink_list[1]["name"]
drink_disp_list = [drink1_name,drink2_name]
drink1_ingredient = drink_list[0]["ingredients"]
drink2_ingredient = drink_list[1]["ingredients"]

def initial():
    #setup GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(bobaLever, GPIO.OUT)
    for key, value in pump.items():
        GPIO.setup(value, GPIO.OUT)

def next_item(current_selection):
    #update current selection and display
    if current_selection == 0:
        current_selection =+ 1
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

def dispense(drinks):#input0 or 1
    
    GPIO.output(bobaLever, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(bobaLever, GPIO.HIGH)
    
    updateDisplay("Dispensing Boba")
    time.sleep(7)
    
    pump_name = []
    pump_time = []
    drink_ingredient = drink_list[drinks]["ingredients"]
    updateDisplay("Dispensing Drink")
    time.sleep(0.5)
    for key, value in drink_ingredient.items():
        pump_name.append(pump.get(key))
        dispense_time = value
        pump_time.append(dispense_time)
    num_pump = len(pump_name)
    max_time = max(pump_time)
    
    #Turn pumps on
    for i in range(num_pump):
        GPIO.output(pump_name[i], GPIO.LOW)#turn on
        print (pump_name[i], " on")
    
    temp_time=0
    temp_pump=0
    sec = 0
    
    for dispense_time in pump_time:
        #print("dispense time: {}".format(dispense_time))
        #print("temptime: {}".format(temp_time))
        actual_time = dispense_time-temp_time
        #print("actual time: {}".format(actual_time))
        
        for i in range(actual_time):
            updateDisplay(str(max_time - sec) + "s left")
            sec = sec + 1
            time.sleep(1)
            
        GPIO.output(pump_name[temp_pump], GPIO.HIGH)#turn off
        print(pump_name[temp_pump],"Turned off")
        temp_pump = temp_pump + 1
        temp_time=dispense_time
        
    updateDisplay("Finished dispensing")
    time.sleep(.5)

initial()
GPIO.output(pump1, GPIO.HIGH)
GPIO.output(pump2, GPIO.HIGH)
GPIO.output(bobaLever, GPIO.HIGH)

#dispense(0)
updateDisplay(str(drink_disp_list[current_selection]))

while True:
    button1_state = GPIO.input(button1)
    button2_state = GPIO.input(button2)

    try:
        # Button1 pressed
        # Dispense drink
        if(button1_state == GPIO.HIGH):
            print('btn 1 pressed')
            dispense(current_selection)
            updateDisplay(str(drink_disp_list[current_selection]))

        # Button2 pressed
        # Go to next menu item
        if(button2_state == GPIO.HIGH):
            current_selection = next_item(current_selection)
            print('btn 2 pressed')
            time.sleep(1)
    except:
        GPIO.cleanup()
