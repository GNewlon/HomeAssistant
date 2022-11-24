# Home Assistant Configuration

Here are all of my Config files from Home Assistant

_Companion Component to [Node-RED](https://github.com/GNewlon/Node-RED) to integrate Node-RED with Home Assistant._

## Integrations
  * ESPHome
  * JS-Z-Wave 700
  * MQTT Broker
  * Node-RED Companion
  * Tasmota
  * Zigbee 3.0 
  
## Devices  
  * Bond-RF Hub
  * Ecobee Wifi Thermostat
  * ESPHome
     * powermeter-18c
  * HVAC Heat Exchanger: Waste Heat= Heats Pool Water
  * Inovelli
    *  Dimmers-(Zwave)
    *  Switches-(Zwave)
    *  Fan Switches-(Zwave)
  * iPhones
  * LG
    * Smart TV
	* SmartThinQ Dishwasher 
	* SmartThinQ Washer
	* SmartThinQ Dryer
	* SmartThinQ Oven
  * Rokus
  * Smartthings 
    * Multipurpose Sensor
  * Sonoff 
    * Zigbee 3.0 USB Dongle Plus
    * Pro R3
    * TH16
  * Sonos
     * Playbar
	 * Sub
	 * Play-3s
	 * Play-1s
  * Tesla
	 * Wall Connector
	 * Custom Integration-MY
  * UDMPRO
     * UniFi Protect
     * UniFi Network	 
  * Xiaomi Miot Auto
     * Roborock
  * Zemismart
     * Z-Wave smart curtains

## Features
* Create and update binary sensors, buttons, sensors, and switches from Node-RED
* Disable and enable Node-RED flows from Home Assistant UI
* Create Home Assistant webhooks and handle them in Node-RED
* Use Device triggers and action from Node-RED

## Minimum Requirements

* [node-red-contrib-home-assistant-websocket](https://github.com/zachowj/node-red-contrib-home-assistant-websocket) v0.20+
* [Home Assistant](https://github.com/home-assistant/core) 2021.12.0

## Installation

### HACS

Install via [HACS](https://hacs.xyz) (Home Assistant Community Store)

1. Go to HACS -> Integrations -> "+ Explore & Download Repos"
1. Find "Node-RED Companion".
1. Open the search result and click "Download this Repository with HACS".
1. Refresh your browser window (bug in HA where it doesn't update the integration list after a reboot)
1. In the Home Assistant UI go to "Configuration" -> "Integrations" click "+" and search for "Node-RED" [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=nodered)

### Manual

1. Using your tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `nodered`.
1. Download _all_ the files from the `custom_components/nodered/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. Refresh your browser window (bug in HA where it doesn't update the integration list after a reboot)
1. In the Home Assistant UI go to "Configuration" -> "Integrations" click "+" and search for "Node-RED" [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=nodered)


    Using your HA configuration directory (folder) as a starting point you should have this:

    ```text
    custom_components/nodered/translations/en.json
    custom_components/nodered/__init__.py
    custom_components/nodered/binary_sensor.py
    custom_components/nodered/config_flow.py
    custom_components/nodered/const.py
    custom_components/nodered/discovery.py
    custom_components/nodered/manifest.json
    custom_components/nodered/sensor.py
    custom_components/nodered/services.yaml
    custom_components/nodered/switch.py
    custom_components/nodered/websocket.py
    ```


