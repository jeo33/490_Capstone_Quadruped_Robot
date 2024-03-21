import time
import board
import busio
import adafruit_bno055

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor instance
sensor = adafruit_bno055.BNO055_I2C(i2c)

# Main loop to read orientation data
while True:
    # Read orientation data
    heading, roll, pitch = sensor.euler

    # Print orientation data
    print("Heading:", heading)
    print("Roll:", roll)
    print("Pitch:", pitch)

    # Delay for a short period
    time.sleep(0.1)
