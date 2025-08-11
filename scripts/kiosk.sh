#!/usr/bin/env bash

# HA URL, ends with "/"
export HA_URL="YOUR_HA_URL"

# Replace the DASHBOARD_NAME with the one from your HA
export DASH_URL=$HA_URL"DASHBOARD_NAME/0?wp_enabled=true"

# This will be the prefix of the sensor that will output to your HA the distance/movement/temperature
export SENSOR_NAME="sensor.YOUR_MADE_UP_SENSOR_PREFIX"

# Get a token, see https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159/4 for instructions
export API_TOKEN="API_TOKEN"

# The distance in cm from which the screen "comes to life"
export WAKEUP_DIST_CM="150"

sleep 3

sudo pkill -f ld2410
sudo pkill -f chromium

sudo /bin/python /home/orangepi/ld2410.py $SENSOR_NAME $HA_URL $API_TOKEN $WAKEUP_DIST_CM &
sudo unclutter-xfixes --hide-on-touch &

chromium \
  --kiosk \
  --force_device_scale_factor=1.25 \
  --no-sandbox \
  --start-maximized \
  --noerrdialogs \
  --disable-infobars \
  --enable-features=OverlayScrollbar \
  $DASH_URL
