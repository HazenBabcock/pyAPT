pyAPT
=====

Python interface to Thorlab's APT motion controllers. 

The motion controller can be accessed in two ways:

1. Using `libftdi1` and `pylibftdi`. Under Linux the easiest way to get these is 
to install `libftdi1` using the package management system, and then install 
`pylibftdi` into a virtual environment or equivalent.

2. Serial communication using [pySerial](http://pyserial.sourceforge.net/) and 
virtual com ports. You can use these in Windows by going to the device manager, 
selecting "Universal Serial Bus controllers", right clicking on the desired 
"APT USB Device" and selecting "properties". Under the Advanced tab check the 
box labeled "Load VCP". Virtual com port drivers are described here: 
[FTDI Chip](http://www.ftdichip.com/Drivers/VCP.htm).

Note on stage limits
====================

The stage limits (maximum acceleration, velocity, etc) as quoted on the
Thorlabs website, or in their user manuals, often don't agree with reality. The
best way to get these limits is to install the APT User software, which seems
to have built-in limits for the various stages. These correspond much better to
the actual performance of stages.
