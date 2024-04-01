Startup guide for the WannaBe 8-Key Macropad:

First off, thank you for purchasing this PCB, and I hope it works out great for you. I am no expert-coder, so the instructions and code I’ll be providing are pretty basic. 

Things you’ll need:
- The latest version of circuit python for the RP2040-zero (https://circuitpython.org/board/waveshare_rp2040_zero/)
- The latest and greatest KMK firmware (http://kmkfw.io/Getting_Started/)
- Lastly, the ‘code.py’ file, available in this repository. 

Recommended:
- Download the IDE Thonny. It’s super basic and easy to use while programming microcontrollers (https://thonny.org/). This would be useful for customizing your macropad layout, as well as debugging. 

Lets begin 🤘
1. After you've assembled your PCB and are ready to start with the firmware, hold down the 'BOOT' button on the RP2040-Zero while plugging it into your computer via USB.
2. Open up your file explorer, on the left you should see a device mounted called something like “RPI-RP2”. Once you verify it’s there, take the .UF2 file you
  got from circuitpython.org, and drag it onto that drive. If done correctly, the drive will dismount, then remount under the new name “CIRCUITPY”.
3. Next, take the code.py file and drag it into the main directory of your CIRCUITPY drive.
4. Similar to the last step, we now need to drag the KMK folder into the main directory. Start by unzipping the folder “kmk_firmware-master”.
  Once unzipped, from kmk_firmware-master, look for the folder called “kmk”. Take that folder and drag it into the main directory of the CIRCUITPY drive,
  same as you did with the .UF2 file. 
5. At this point, you should be able to reset the macropad by using the reset button (opposite the boot button). Give it a few seconds, then pull up your notepad and give it a try.
  From left to right, top to bottom, the provided code will assign numbers 1-8. 

Great, hopefully, that worked smoothly. Now you’re ready to use the macropad as is, or to customize the layout to your needs. You can find all the resources you need on the KMK website,
but I’ll specifically link to the key overview page (http://kmkfw.io/keycodes/).

Please provide me with any and all feedback if you feel the urge to. I’d like for these instructions to be clear and accurate, and make for a good experience.
You can contact me through the Etsy shop, or by the email provided below.

Thanks again,
Alex
alex@wannab.shop

