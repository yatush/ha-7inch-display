#!/usr/bin/env bash

export URL="YOUR_HOMEASSISTANT_URL"

sleep 3

sudo pkill -f ld2410
sudo pkill -f chromium

sudo /bin/python /home/orangepi/ld2410.py &
sudo unclutter-xfixes --hide-on-touch &

chromium \
  --kiosk \
  --force_device_scale_factor=1.25 \
  --no-sandbox \
  --start-maximized \
  --noerrdialogs \
  --disable-infobars \
  --enable-features=OverlayScrollbar \
  $URL
