# CAN Bus Program
In late 2019 I purchased a used Infiniti G37x with the fully upgraded infotainment package. 
Audio systems are very important to me, so when the head-unit was experiencing connectivity issues through it's bluetooth module I started researching replacement options.


## Project Background
Previous cars I've owned have a segregated audio system, which usually implies that directly swapping the head-unit with aftermarket alternatives is not only cheap, but quick. 
This version of the G37's head-unit is integrated as a CAN Bus module, and is used for critical communications on the upgrades features. These features include:
* Backup Camera
* Backup Sensors Information
* Wheel Angle Position
* AC Controls
* Steering Wheel Controls

Because of these beneficial systems, the head-unit cannot be directly replaced. What I could change was the controller interface that car used to control the existing Audio Video, Air Conditioning, and backup sensors. 

The beginning of the project involved gaining access to the car's bus network. Using the linux socketcan library, and a significant amount of troubleshooting, I started logging data sets from the car's main bus network. The main program used to record these datasets was savvycan.

The first attempts of decoding resulted in a small DBC file that linked the headlight switches, steering wheel position, and RPM to their corresponding signals. One issue continued, I couldn't find the signals for the AV Controller. After finding out that they ran on their own sub-network, I patched in and started analyzing the new data.

## Development Process

For the controller's data to be useful, it must be used with an interface that could replicate the existing controller, while not interrupting other signals on the sub-network. Python already contains a repository for linking with multiple system libraries that interface with bus networks, so this was the language I chose to develop in.

The controller needs to perform the following functions.
1. Perform initialization onto the network with the AV head-unit.
2. Send a periodic broadcast signal every half second, which hold priority over any other controller signals (after initialization.)
3. On button press, send a signal and wait for a response.
4. Read the response signal from the AV head-unit, and update the controller's send message clock.
5. If the button is still pressed, send another signal message after 100 milliseconds.
6. If the button is released, send a release message.
7. If a dial is turned, send the speed signal every 100 milliseconds.
8. There are no release messages for dials.

I have reached points where points 1-4, 6, and 8 are programmatically functional. Errors arise when I'm unable to continue I/O reads while updating GUI conditions. This has later been identified as an issue with understanding asynchronous functionality within the python language.

## Version Development
Version 1 of the program resulted in a working interface which performed MOST of the functions needed. I was unable to get any continuous sending functions on the virtual network. 

Versions 2-4 contain a variety of attempts to simplify my code, and create an asynchronous functionality before I knew it existed. I switched over to Qt based GUI development because it seemed to create better looking interfaces without significant design experience. 

Version 5 is the first version after I read up on asynchronous programming, and was unable to achieve progress. I created a working interface, but kept running into infinite loop errors. One of the three async loops would refuse to behave, regardless of which one was given priority.  

Version 6 is the current development of the controller. After studying "Dead Simple Python", I gained enough conceptual knowledge to tackle asynchronous programming, and am working on the first release of the new controller setup with functional asynchronous methods. 