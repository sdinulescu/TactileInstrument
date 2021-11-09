# Tactile Instrument
A haptic bracelet for turning the hand into an instrument, performed via touch.

Stejara Dinulescu, Fall 2021. MAT240A.

## Abstract

The sense of touch is used to convey semantic and emotional information when interacting socially, with expressivity and nuance paralleled in speech and musical composition. We present a wrist-worn haptic device that can digitally encode tactile gestures (taps, slides, pinches, etc.) across the whole surface of the hand via remote and minimal acoustic sensing, leaving the hand free for manual interaction. By sonifying the captured mechanical signals generated by spatiotemporal wave propagation across the skin that occurs during touch contact, our wearable device transforms the hand into a musical instrument.

![Screen Shot 2021-11-07 at 10.20.38 AM](/Users/stejaraiulia/GitHub/TactileInstrument/Images/Screen Shot 2021-11-07 at 10.20.38 AM.png)

-----------------------

## Documentation

- *10/28*: Utilizing the current device setup (4 3-axis analog accelerometers connected to 2 Adafruit Feather M0 Wifi boards, depicted in image above), read serial input via Max's serial object. See *SerialAccelerometerInput.maxpat* and *SerialAccelerometerIn* + *Accelerometer.h* Arduino files, located in the *SerialAccelerometerIn* folder.
  
  - Following the *Communications Tutorial 2: Serial Communication* Max tutorial, I created a max patch utilizing the serial object utilizing the port that the adafruit device was on
  - I was successful reading in numbers, but the string that I was sending serially via Arduino was not being parsed properly on the other end. I looked into the itoa and fromsymbol object, where I found itoa do what I need to pending proper parameter setting via the serial object (i.e. the "chunk" parameter, specificying how many numbers I was expecting to be communicated via serial port). 
  - However, halfway through my creation/exploration of this patch, my devices stopped registering in the ports list of Arduino. Both Feather M0 boards were not being listed on either my Macbook or my Windows 10 office computer, despite manually resetting the board. Stack overflow or adafruit forums were not fruitful. 
    - --> Updating my Macbook fixed this issue (still using the Teensy moving forward)
  - In the meantime, I ordered a Teensy board to attempt to utilize it as a midi input. Arrives on 11/01.
  
- Utilize Teensy to transmit accelerometer data to Max (11/01-11/03). Setup pictured below with 2 accelerometers.
  
  ![IMG_8200](/Users/stejaraiulia/GitHub/TactileInstrument/Images/IMG_8200.jpg)
  
  - Get Teensy registered by computer (works now on Mac and Windows) as a midi or HI device, and/or via serial port in Arduino
    - A macOS update (to the new Monterey OS) fixed the problem I was having with the teensy not being recognized (or any microcontroller device) via USB port
  - Receive messages in Max
  - Display raw accelerometer data (x, y, z data per accelerometers --> 2 accelerometers --> 6 floats per read sample) in Max
    - Issue --> Sample drops due to needing to bang the serial object to read from serial port. Move back to old Python script for reading serial input, and send OSC data to Max.
  - OSC messaging from python script to max works (11/03 -11/04) --> I am filling a buffer with the samples read in via OSC; however, I am still experiencing sample drops. This causes the buffer to look like discrete signals (i.e. measuring periods of touch on the accelerometer, or no touch).![Screen Shot 2021-11-07 at 10.25.07 AM](/Users/stejaraiulia/GitHub/TactileInstrument/Images/Screen Shot 2021-11-07 at 10.25.07 AM.png)
  - 11/06 --> I just needed to change some parameters of the buffer object to visualize the signal better. Now, you can clearly see when each accelerometer is tapped, as well as the resulting mechanical reverberations. ![Screen Shot 2021-11-07 at 10.45.26 AM](/Users/stejaraiulia/GitHub/TactileInstrument/Images/Screen Shot 2021-11-07 at 10.45.26 AM.png)This can now be sonified! 
  
- Sonifying signals

  - Using line~ and mc.play~, I am able to playback all three channels of signal from each buffer (11/07)
  - How can these signals drive/shape audio output? First, I tried with a simple sine oscillator, varying pitch with signal change


----------------

## To Dos

- *Next:* Extend Max patch to process data (compress axes to one-dimensional signal, normalize, whiten), visualize these signals (*scope~*, *number~*)
- *Next:* Control synthesis processes





