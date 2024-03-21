import evdev
from evdev import InputDevice, categorize, ecodes

# Find the Joy-Con event file (e.g., /dev/input/eventXX)
# You might need to adjust this according to your system
joycon_path = '/dev/input/event6'

# Create an InputDevice instance for the Joy-Con
joycon = InputDevice(joycon_path)

print(f"Found Joy-Con: {joycon.name}")

# Loop to handle button presses
for event in joycon.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
