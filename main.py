import machine
import time

# 1. Setup Potentiometer ADC (GP26 = ADC0)
pot = machine.ADC(26)

# 2. Setup Direction Pins
in1 = machine.Pin(14, machine.Pin.OUT)
in2 = machine.Pin(13, machine.Pin.OUT)

# 3. Setup PWM for Speed Control (ENA on GP15)
ena = machine.PWM(machine.Pin(15))
ena.freq(1000)  # 1 kHz PWM frequency

# Set motor rotation direction (Forward)
in1.value(1)
in2.value(0)

while True:
    # Read 16-bit ADC value (0 to 65535)
    pot_value = pot.read_u16()
    
    # Apply deadband to prevent motor buzzing at low voltages
    if pot_value < 3000:
        ena.duty_u16(0)
    else:
        # Write directly to PWM duty cycle (0 to 65535)
        ena.duty_u16(pot_value)
        
    time.sleep(0.02)