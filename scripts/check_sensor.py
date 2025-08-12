import sys
import time
import serial.tools.list_ports
from LD2410 import LD2410, PARAM_BAUD_256000

def find_ld2410_port():
    """Scans serial ports and returns the device path for an LD2410 sensor."""
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("❌ No serial ports found on this system.")
        return None

    print("🔎 Searching for LD2410 sensor...")
    for port in ports:
        try:
            radar = LD2410(port.device, PARAM_BAUD_256000, verbosity=0)
            if radar.read_firmware_version():
                print(f"✅ Found LD2410 at: {port.device}")
                radar.stop()
                return port.device
        except Exception:
            continue
    print("❌ LD2410 sensor not found.")
    return None

def monitor_radar():
    """Finds the radar and prints its live data until stopped."""
    port = find_ld2410_port()
    if not port:
        sys.exit(1)

    radar = None
    try:
        radar = LD2410(port, PARAM_BAUD_256000, verbosity=0)
        
        # Using some basic default parameters for good performance
        radar.edit_detection_params(max_gate=8, max_moving_gate=8, max_static_gate=1)
        
        radar.start()
        print("\n--- Starting Live Radar Monitoring ---")
        print("Press Ctrl+C to stop.")

        while True:
            data = radar.get_data()
            
            # The get_data() method returns data only when a target is detected
            if data:
                # data[0][0] indicates the target type: 1 for moving, 2 for static
                is_moving = (data[0][0] == 1)
                distance = data[0][1]

                status_str = "Yes" if is_moving else "No "
                distance_str = f"{distance} cm"
            else:
                # No target detected within the configured gates
                status_str = "No "
                distance_str = "N/A"

            # The '\r' character moves the cursor to the beginning of the line,
            # allowing us to overwrite it for a "live" display.
            # Extra spaces at the end clear any previous, longer line.
            print(f"Movement Detected: {status_str} | Distance: {distance_str}      ", end='\r')
            sys.stdout.flush()
            
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n--- Stopping Radar ---")
    finally:
        if radar:
            radar.stop()
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_radar()
