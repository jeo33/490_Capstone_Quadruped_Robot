from evdev import InputDevice, categorize, ecodes
import threading
import time
from robot import robot
from servo_control import controller


quadruped_robot=robot()
controller=controller()
#joycon_path_L = '/dev/input/event4'
joycon_path_R = '/dev/input/event5'

# Create an InputDevice instance for the Joy-Con
#joycon_L = InputDevice(joycon_path_L)
joycon_R = InputDevice(joycon_path_R)
def function_turn_left():
    print("Function function_turn triggered")
    controller.set_walk_angle(quadruped_robot.turn_left())
    time.sleep(0.02)
def function_pull():
    print("Function function_pull triggered")
    controller.set_angle(12,130)
    time.sleep(0.02)
def function_stop_wench_off():
    print("Function function_stop_wench_off triggered")
    controller.set_winch_pwm_zero()
    time.sleep(0.02)
def function_push():
    print("Function function_push triggered")
    controller.set_angle(12,50)
    time.sleep(0.02)
def function_POWE_PWM():
    print("Function function_POWE_PWM triggered")
    #controller.set_walk_angle(quadruped_robot.turn_left())
    #time.sleep(0.02)
    controller.set_pwm_zero()
    time.sleep(0.02)
def function_pwm_one():
    print("Function function_pwm_one triggered")
    controller.set_pwm_one()
    #controller.set_walk_angle(quadruped_robot.turn_right())
    time.sleep(0.02)
def function_turn_right():
    controller.set_walk_angle(quadruped_robot.turn_right())
    time.sleep(0.02)
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

#added
def function_move():
	print("unsure")
	controller.set_target_degree(quadruped_robot.move())
	controller.set_all()
	time.sleep(0.02)

# Define a function to monitor a specific Joy-Con
def monitor_joycon(device, name):
    print(f"Monitoring {name}...")
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            # Check if a specific button is pressed
            if key_event.keystate == key_event.key_down:
                if 'BTN_EAST' in key_event.keycode:
                    function_forward()
                elif 'BTN_C' in key_event.keycode:
                    function_backward()
                elif 'BTN_NORTH' in key_event.keycode:
                    function_turn_left()
                elif 'BTN_SOUTH' in key_event.keycode:
                    function_turn_right()
                elif 'BTN_Z' in key_event.keycode:
                    function_push()
                elif 'BTN_WEST' in key_event.keycode:
                    function_pull()
                elif 'BTN_THUMBR' in key_event.keycode:
                    function_pwm_one()
                elif 'BTN_START' in key_event.keycode:
                    function_POWE_PWM()
                elif 'BTN_TR2' in key_event.keycode:
                    function_stop_wench_off()
                    
        if event.code == ecodes.ABS_HAT0X:
            if event.value==-1:
                function_sit()
            elif event.value>0:
                function_stand()
# Main control loop function
def main_control_loop():
    # Start monitoring both Joy-Cons in separate threads
    #thread_L = threading.Thread(target=monitor_joycon, args=(joycon_L, 'Joy-Con L'), daemon=True)
    thread_R = threading.Thread(target=monitor_joycon, args=(joycon_R, 'Joy-Con R'), daemon=True)

    #thread_L.start()
    thread_R.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Main control loop terminated by user.")

if __name__ == "__main__":
    main_control_loop()

