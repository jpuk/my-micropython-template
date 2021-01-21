# configuration templates for various micropython controllers

'''
# TTGO T-Beam v1.1 with sx1262 and neo-6, 4Mb flash, 8Mb PSRAM, AXP192 power management ic
available_pins = {"ADC": [0, 2, 4, 13, 14, 15, 25, 32, 33, 35, 36, 39],
                  "INOUT": [],
                  "OUT": [],
                  "IN": [],
                  "Serial": {"tx": 1, "rx": 3},
                  "Touch": [4, 0, 2, 15, 13, 14, 33, 32],
                  "5v": [],
                  "3v3": [],
                  "GND": []}
lora_gpio = {
    "miso": 19,
    "mosi": 27,
    "cs": 18,
    "sclk": 5,
    "dio_0": 26,
    "reset": 23,
    "led": 2
}

wire_gpio = {"sda": 21, "scl": 22}

neo_gpio = {
    "tx": 34,
    "rx": 12
}

'''

# Heltec WIFI LoRa 32 8Mb flash with sx1262 and 128x64 oled display#

# all touch pins "Touch": [4, 0, 2, 15, 13, 12, 14, 27, 33, 32],
# only list pins that are usable
available_pins = {"ADC": [],
                  "INOUT": [],
                  "OUT": [],
                  "IN": [],
                  "Serial": {"tx": 1, "rx": 3},
                  "Touch": [2, 13, 12, 33, 32],
                  "5v": [],
                  "3v3": [],
                  "GND": [],
                  "xtal": [32, 33],
                  "led": 25,
                  "vext_control": 21,
                  "prg_button": 0,
                  }


lora_gpio = {
    "miso": 19,
    "mosi": 27,
    "cs": 18,
    "sclk": 5,
    "dio_1": 35,
    "dio_2": 34,
    "reset": 14,
    "led": 25,
}

oled_gpio = {
    "scl": 15,
    "sda": 4,
    "rst": 16
}


# generic esp32 wroom


# Generic esp8266