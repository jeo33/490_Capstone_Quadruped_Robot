from evdev import InputDevice, categorize, ecodes
import threading
import time
from robot import robot
from servo_control import controller


quadruped_robot=robot()
controller=controller()
joycon_path_L = '/dev/input/event5'
joycon_path_R = '/dev/input/event6'

joycon_L = InputDevice(joycon_path_L)
joycon_R = InputDevice(joycon_path_R)

def function_forward():
    print("Function A triggered")
    controller.set_walk_angle(quadruped_robot.walk())
    time.sleep(0.02)
def function_backward():
    print("Function B triggered")
    controller.set_walk_angle(quadruped_robot.walk_back())
    time.sleep(0.02)
def function_sit():
    print("Function B triggered")
    controller.set_target_degree(quadruped_robot.sit())
    controller.set_all()
    time.sleep(0.02)
def function_stand():
    print("Function B triggered")
    controller.set_target_degree(quadruped_robot.stand())
    controller.set_all()
    time.sleep(0.02)

def monitor_joycon(device, name):
    print(f"Monitoring {name}...")
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            # Check if a specific button is pressed
            if key_event.keystate == key_event.key_down:
                if 'BTN_EAST' in key_event.keycode:
                    function_stand()
                elif 'BTN_C' in key_event.keycode:
                    function_sit()
                if 'BTN_NORTH' in key_event.keycode:
                    function_forward()
                elif 'BTN_SOUTH' in key_event.keycode:
                    function_backward()

def main_control_loop():
    thread_L = threading.Thread(target=monitor_joycon, args=(joycon_L, 'Joy-Con L'), daemon=True)
    thread_R = threading.Thread(target=monitor_joycon, args=(joycon_R, 'Joy-Con R'), daemon=True)

    thread_L.start()
    thread_R.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Main control loop terminated by user.")

if __name__ == "__main__":
    main_control_loop()

