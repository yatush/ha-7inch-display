ha-7inch-display
================
**Wall mounted 7 inch touch display for HA, based on OrangePi Zero 3, with motion detector.**

# Background
A project to create a HA display to mount on walls. Featuring:
* 7 inch touch display.
* Fully functional unix working running on [OrangePi Zero 3](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero-3.html).
* Power supply and OrangePi fits into outlet box (deep version of it).
* Motion sensor to wake up on pre-defined distance movement.

<img src="/images/7inch-1.png" height="300" /> <img src="/images/7inch-2.png" height="300" />

# Hardware

## Touch screen - 7 Inch Touch Screen IPS 1024x600 HD LCD HDMI-compatible

<img src="/images/screen-front.png" width="200" /> <img src="/images/screen-back.png" width="200" />

* 1024x600 IPS resolution
* [Aliexpress link](https://www.aliexpress.com/item/1005001485174459.html)
* Please make sure you choose the one with the back looking like this - HDMI connector and four round "legs" on the corners.
* Price: ~36 USD.

## Power supply - AC-DC to DC Step-Down Power Supply Module AC85-220V to DC 5V 2A

<img src="/images/power-supply.png" width="200" />

* 110V/220V -> 5V2A converter that fits in the wall box.
* [Aliexpress link](https://www.aliexpress.com/item/1005005142108650.html)
* Price: ~6 USD.

## SBC - Orange pi zero 3 (2GB Ram version)

<img src="/images/orange-pi.png" width="200" />

* Small factor SBC
* I've tried running this with Raspberry pi 4 - it's both more expensive, heats up more, and needs more power.  The Orange Pi Zero 3 is perfect for this usage.
* [Aliexpress link](https://www.aliexpress.com/item/1005006170910291.html)
* Price: ~26 USD.

## Passive cooling case for the Orange Pi

<img src="/images/housing.png" width="200" />

* Also protects from physical damage.
* [Aliexpress link](https://www.aliexpress.com/item/1005005886279442.html)
* Price: ~4 USD

## SD card for the SBC

<img src="/images/card.png" width="200" />

* Any 32 GB micro SD card will do the work.
* [Aliexpress link](https://www.aliexpress.com/item/1005007897862434.html)
* An SDCard reader is also needed, to burn the image to the SD Card.
* Price: ~3 USD.

## HDMI cable to connect the Orange Pi to the screen

<img src="/images/a3.png" width="200" /> <img src="/images/d2.png" width="200" /> <img src="/images/ribbon.png" width="200" />

* Built out of three parts - two connectors and the ribbon:
  * The first connector - model A3.
  * The second connector - model D2.
  * the connecting ribbon - length of 10 c"m.
* [Aliexpress link](https://www.aliexpress.com/item/1005006426262787.html) (choose the three parts separately).
* Price: ~7 USD for all three parts.

## USB cable to connect the Orange Pi to the screen

<img src="/images/usb.png" width="200" />

* Pay attention to the connectors (AMDO V8UP)
* Length of 10cm.
* [Aliexpress link](https://www.aliexpress.com/item/1005005979020420.html)
* Price: ~5 USD.

## USB-C Power plug

<img src="/images/usb-power.png" width="200" />

* Any other compact USB-C plug should do the work.
* [Aliexpress link](https://www.aliexpress.com/item/1005005419728912.html)
* Price: ~3 USD (for a pack of 10, only 1 is needed)

## Motion sensor - LD2410b

<img src="/images/ld2410b.png" width="200" />

* Choose a model where there are welded pins.
* [Aliexpress link](https://www.aliexpress.com/item/1005005242873516.html)
* Price: ~3 USD

## Motion sensor cable

<img src="/images/ld2410b-cable.png" width="200" />

* [Aliexpress link](https://www.aliexpress.com/item/1005007055937689.html)
* Price: ~1 USD

## Outlet box

<img src="/images/box.png" width="400" />

* This is the outlet box I'm using.
* Important measurements:
  * Length: 121mm
  * Width: 67mm
  * Depth: 74mm
  * Distance between screws: 108.5mm
* For other between-screws-distance the 3d model should be modified, this should not be a problem.
* I think this is the minimum size for the outlet box, otherwise, all the electronics will not fit in.

## (Optional) Keyboard to control the display

<img src="/images/keyboard.png" width="200" /> <img src="/images/usb-female.png" width="200" />

* There's no need while the system is "running" to control it via keyboard.
* However, for initial setup, and in case things go wrong for some reason, this is really convenient.
* Because OPI03 has only one usb pory (used for the screen), we need to also add a pin-connected USB port.
* [Aliexpress link - keyboard](https://www.aliexpress.com/item/1005004085232177.html)
* [Aliexpress link - USB port](https://www.aliexpress.com/item/1005004492194988.html)
* Price: ~4 USD + ~3 USD = ~7 USD.

# On the wall wiring diagram

<img src="/images/wiring.png" />

# Installation process

## Download and burn the Orange Pi OS(Arch) to the micro SD card
* Download the Debian Bookworm desktop image from [this](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-Zero-3.html) site.
* Burn it to an micro SD card, following the instructions [here](http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_3#Method_of_burning_Linux_image_to_micro_SD_card_based_on_Windows_PC).

## Initial startup
* Connect according to the wiring diagram
* Once the linux image is up, connect to the internet (using the icon on the top left part of the screen).

## Add scripts content
* Add the content of /scripts/kiosk.sh to ```/home/orangepi/kiosk.sh```
* Add the content of /scripts/ld2410.py to ```/home/orangepi/ld2410.py```
* Change the parts that need to be configured in both these scripts
* Make sure the two files are executable
```
chmod 777 /home/orangepi/kiosk.sh
chmod 777 /home/orangepi/ld2410.py
```

## Install required components
Run all the following:
```
sudo apt-get install pip
```
```
sudo pip3 install keyboard --break-system-packages
```
```
sudo pip3 install git+https://github.com/vjsyong/LD2410.git --break-system-packages
```
```
sudo pip3 install requests --break-system-packages
```
```
sudo pip3 install pySerial --break-system-packages
```
```
sudo apt-get install unclutter-xfixes
```

## Set ```kiosk.sh``` to start on startup
* From the top right menu: Applications->Settings->Session and Startup -> Application and Autostart -> add ```/home/orangepi/kiosk.sh```

## Set timezone:
* See available timezones by:
```
timedatectl list-timezones
```
* Choose the right one and set it to the system by:
```
timedatectl set-timezone XXXX
```

## Remove sudo passwords for orangepi user
* Open a Terminal window and type:
```
sudo visudo
```
* In the bottom of the file, change to the following line:
```
orangepi ALL=(ALL) NOPASSWD: ALL
```

## Enable the UART5 for radar
* From the terminal, run
```
sudo orangepi-config
```
* System -> Hardware
* Go down to ```ph-uart5``` press space to toggle
* Save -> Back -> Reboot.

**After following the above process, the system should restart and HA should start**

# Changes to HA
## WallPanel
* I'm using the (WallPanel)[https://github.com/j-a-n/lovelace-wallpanel] for "screensaver" options. The python scripts omits "alt" every time it senses a movement in less than 150c"m from it, which triggers the wall panel to get out of the screensaver.
* The WallPanel configuration I'm using (for reference):
```
wallpanel:
  cards:
    - type: custom:digital-clock
      firstLineFormat: h:mm
      card_mod:
        style: |
          ha-card {
            background-color: transparent;
            box-shadow: none;
            border: none;
            font-size: 5vw;
            color: #aaa;
            font-family: 'Acme', sans-serif;
            display: inline-block;
          }
          ha-card .first-line {
            font-size: 20vw;
          }
          ha-card .second-line {
            font-size: 5vw;
          }
  enabled: false
  debug: false
  hide_toolbar: true
  hide_sidebar: true
  fullscreen: false
  idle_time: 15
  image_url: /
  image_animation_ken_burns: false
  image_order: random
  show_images: true
  show_progress_bar: false
  display_time: 120
  keep_screen_on_time: 0
  black_screen_after_time: 0
  control_reactivation_time: 1
  screensaver_entity: input_boolean.wallpanel_screensaver
  info_animation_duration_x: 300
  info_animation_duration_y: 180
  info_animation_timing_function_x: steps(10, end)
  info_animation_timing_function_y: steps(6, end)
  info_move_pattern: random
  info_move_interval: 0
  info_move_fade_duration: 2
  card_interaction: false
  style:
    wallpanel-screensaver-image-overlay:
      background: rgba(0,0,0,0.6)
    wallpanel-screensaver-info-box-content:
      background: '#00000000'
    wallpanel-screensaver-info-box:
      '--wp-card-width': 45vw
```
* The step function in ```info_animation_timing_function_x/y``` is used to reduce the CPU usage.
* I use dark images (so that while the screen is in screensaver mode, it doesn't emit a lot of light). A sample of backgrounds are available under the ```backgrounds``` directory.
* Once this is all done, in the URL of starting the HA (in the ```kiosk.sh``` script), add:

  https://HA_URL/DASHBOARD/0<b>?wp_enabled=true</b>

  to start the WallPanel on startup.

## Other HA changes
* I'm using the dark mode of HA - IMO makes it look much better.

# Things I've tried along the way
* The Orange Pi Zero 4 was chosen over Raspberry Pi 4 - It consumes less power, gets to lower temperature and is smaller (dimensions). Performance-wise, it's weaker, but good enough to run browser smoothly with the right tweaks.
* Temperature-wise - I've run this for over a month, and it runs ~70ºC. I never saw it goes above 77ºC.
* The specified monitor is a good balance between price and performace. Higher resolution monitors require more CPU resources, which means higher temperature and more power consumption.
