import serial.tools.list_ports
from LD2410 import LD2410, PARAM_BAUD_256000
import sys

def find_ld2410_port():
    """
    Scans all available serial ports and tries to connect to an LD2410 sensor.

    Returns:
        The device path (e.g., '/dev/ttyACM0') if a sensor is found, otherwise None.
    """
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("❌ No serial ports found on this system.")
        return None

    print("🔎 Searching for LD2410 sensor on available ports...")

    for port in ports:
        print(f"   -> Checking port: {port.device}")
        try:
            # Attempt to initialize the radar on the current port.
            # We set verbosity to 0 to keep the output clean during the scan.
            radar = LD2410(port.device, PARAM_BAUD_256000, verbosity=0)
            
            # A good way to check is to ask for the firmware version.
            # If this succeeds, we've found the right device.
            firmware_version = radar.read_firmware_version()

            if firmware_version:
                print(f"✅ Success! Found LD2410 Sensor at: {port.device}")
                print(f"   Firmware Version: {firmware_version}")
                radar.stop() # Cleanly close the connection
                return port.device

        except Exception as e:
            # This will catch errors from connecting to the wrong device type
            # or permissions issues. We can safely ignore them and continue scanning.
            # print(f"      Could not connect or not an LD2410: {e}")
            pass

    print("❌ LD2410 sensor not found on any port.")
    return None

if __name__ == "__main__":
    find_ld2410_port()
