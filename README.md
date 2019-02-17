# USBControl

An OctoPrint plugin to allow USB ports to be programmatically turned OFF and ON from within the web interface.

## Overview
> **Raspberry Pi 3B**: A single-board computer made by the Raspberry Pi Foundation
> 
> **USB**: (abbreviation of Universal Serial Bus) is an industry standard that establishes specifications for cables, connectors and protocols for connection, communication and power supply between personal computers and their peripheral devices. 

* The USB specification was created originally when the Type-A side of a USB cable was the PC and the Type-B side was the device. It was assumed that the PC could always provide power to the device.
* For OctoPi, the Type-A side is the Raspberry Pi 3B with a 5V 2.5A power adapter. It can't be sinking power over to the printer controller board since that's now considered to be the one with beefier power needs. This is often the case when the printer board is powered off and the Raspberry is still powered on. This could lead to the printer's LCD remaining on under these circumstances.
* It is suggested that this sinking of power is causing undervoltage conditions in some cases.
* The typical USB connection has four pins: 5V, ground, transmit and receive. OctoPrint appears to be happy with just the last three of these (as suggested by some users). As they say, though, "*your mileage may vary*".
* Many people are applying a small strip of tape to the inside of their Type-A connectors to prevent 5V from being felt on the controller (Arduino) board.
* There are other configurations in which the user feels like they want to have programmatic control over providing power to downstream devices.

### The rationale for this plugin

Rather than rigging up inline switches, applying tape inside the tongue of a USB connector or purchasing specialized male/female adapters which omit the 5V line...

    ...I thought that I would provide this plugin as a simpler alternative.

![Settings](https://user-images.githubusercontent.com/15971213/52908070-d4ae9980-3222-11e9-925a-6bff7af7badb.png)

## Compatibility
This plugin was created to support only the following platforms:

* Raspberry Pi 3B
* Raspberry Pi 3B+
* Raspberry Pi 2B

It is NOT intended to support the following:

* Raspberry Pi 3A+
* Raspberry Pi Compute Modules
* Raspberry Pi 1B+
* Raspberry Pi 1A+
* Raspberry Pi Zero W
* Raspberry Pi Zero
* PCs, Macs, generic Linux workstations *or anything else*

Also, this plugin is NOT intended to support those of you who wish to plug more than one printer into your Raspberry Pi 3B.

## Primary use case
I expect that this plugin would be useful for anyone who needs to remove power which is being sinked over to their printer's LCD panel when their printer board is powered OFF.

## Complications

### Raspberry Pi 2B/3B can't individually control ports
The `uhubctl` author informs me that internally the Raspberry Pi 2B and 3B cannot individually toggle ports. At best, the gang of four ports can be toggled as a group.

In theory, the Raspberry Pi 3B+ can individually control the ports.

### This won't necessarily work while printing
I note that on my own test rig, the Robo 3D printer board includes a jumper to determine how the board is powered. If the jumper is set to "USB", this plugin works as expected to completely power ON/OFF all functions on the board over the USB port although this wouldn't technically work in a real printer given the power limitation. **If instead the jumper is set to "5V" then toggling the associated USB port to OFF from this plugin will result in a communication error after the timeout has been reached.** Therefore this is not compatible with the normal functioning of this board for the purpose of printing.

**It *would* be useful to stop sinking power to the board when it is powered OFF however.**

| Popup | Seen in State side panel |
|---|---|
| ![CommunicationsError](https://user-images.githubusercontent.com/15971213/52870077-e1849d80-30fb-11e9-8924-95b889d39797.png)| ![TooManyTimeouts](https://user-images.githubusercontent.com/15971213/52870118-f8c38b00-30fb-11e9-9fd5-0ee2938f7ba4.png) |

So in some cases, this simply won't work for printing. (A better alternative might be a USB adapter with an inline diode for the 5V line.)

### Which port?
There are five USB ports on the USB hub known as `1-1` in the Raspberry Pi 3B. USB port 1 is the micro USB connection we usually power the board with. The remaining ports 2 through 5 are represented in the interface.

The Raspbian operating system assigns these port numbers not by their physical location in the four-connector arrangement but by the ID of the device during bootup or when the cable is connected.

For this reason, I a not persistently storing your settings for every session because this could get confusing if you add/remove USB devices.

### Persistence
At the moment, this plugin does not save the power state for each USB port. Each restart of OctoPrint will basically forget how you last left these and assume that they're all ON.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OutsourcedGuru/OctoPrint-USBControl/archive/master.zip

## Configuration

When initially installed, the plugin still needs a script to be run once. The instructions for doing this may be found in the associated **Settings** page but is also included below.

1. Install the plugin (see **Setup** in the section above)
2. Visit the **Settings** page
3. Follow the instructions under the **Setup required** section there
   * For this, you are required to remote into the Raspberry Pi 3B using `ssh` or `PuTTY`
   * Copy/paste the install script into this remote session
   * Return back to the OctoPrint **Settings** page
   * Indicate that you have run the script
   * Select the **Save** button at the bottom of the **Settings** page
4. Restart OctoPrint
5. Return to the **Settings** page (you should see the control sliders now for each USB port)

## REST API
The plugin includes an API for programmatically toggling the ports ON/OFF in a way which is similar to OctoPrint's. You can find/copy your API key under **Settings** -> **API**.

### Controlling USB port 2 remotely
```
POST /api/plugin/usbcontrol HTTP/1.1
Host: example.com
Content-Type: application/json
X-Api-Key: abcdef...

{
  "command": "usb2",
  "arg2": "on"
}
```

For USB port 2, the `arg2` options are "on" and "off".

### Controlling USB ports 3 through 5 remotely
The API is similar for the remaining ports. Instead of "usb2" and "arg2", replace these with the appropriate number.

## Reporting bugs/issues
Please do not report a bug if you *can't* print with the USB power turned OFF. It is assumed that this is the case for most printer controllers. If this does work for you, feel lucky.

By the way, this means the same as "I've just gotten a **Communications Error** popup with the USB port toggled OFF". This is not meant to be a solution to this problem.

Please do not report a bug if you are plugging more than one printer into your Raspberry Pi 3B at the same time.

Please do not report a bug if you are using a platform that isn't listed in the **Compatibility** section above.