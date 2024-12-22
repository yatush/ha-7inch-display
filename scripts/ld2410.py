from LD2410 import *
from requests import post
from datetime import datetime
import logging
import time
import keyboard
import threading
import subprocess

ha_url = "ADD_YOUR_HOMEASSISTANT_URL"
sensor = "sensor.GIVE_A_NAME"

# Get a token, see https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159/4 for instructions
token = "REPLACE_THIS_WITH_THE_TOKEN"

url = ha_url + "/api/states/" + sensor
headers = {"Authorization": "Bearer " + token }

# Change this to change the distance from screen the it wakes up from.
wakeup_dist = 150 # In c"m

def request_task(url, data, headers):
  post(url, json=data, headers=headers)

def fire_and_forget(url, data, headers):
  threading.Thread(target=request_task, args=(url, data, headers)).start()

def main():
  radar=LD2410("/dev/ttyS5", PARAM_BAUD_256000, verbosity=logging.INFO)
  fw_ver = radar.read_firmware_version()
  print(fw_ver)
  radar.edit_detection_params(8, 8, 1)
  radar.edit_gate_sensitivity(3, 50, 40)
  detection_params = radar.read_detection_params()
  print(detection_params)

  radar.start()

  last_movement = False
  last_distance = 1000
  last_time = datetime.now()
  move_10 = False
  dist_10 = 10000

  while True:
    data = radar.get_data();
    movement = data[0][0] % 2 == 1
    distance = data[0][1]
    now = datetime.now()
    move_10 = move_10 or movement
    dist_10 = min(dist_10, distance)

    if (now - last_time).total_seconds() > 10:
      temp = 0
      try:
        temp = int(int(subprocess.check_output(['cat', '/sys/class/thermal/thermal_zone0/temp']))/100)/10
      except Exception as e:
        temp = -1
      fire_and_forget(url + "_distance", headers=headers, data= {
        "state": dist_10 if move_10 else "unknown",
        "attributes": {
          "unit_of_measurement": "cm",
          "device_class": "distance",
          "state_class": "measurement"
        }
      })
      fire_and_forget(url + "_movement", headers=headers, data= {
         "state": "on" if move_10 else "off",
         "attributes": {
           "device_class": "motion"
         }
      })
      fire_and_forget(url + "_temp", headers=headers, data= {
        "state": temp,
        "attributes": {
          "unit_of_measurement": "°C",
          "device_class": "temperature",
          "state_class": "measurement"
        }
      })
      last_time = now
      move_10 = False
      dist_10 = 10000
      radar.ser.reset_input_buffer()
    if movement and distance < wakeup_dist:
      keyboard.send('alt')
    time.sleep(0.25)
  radar.stop()

if __name__ == "__main__":
  main()
