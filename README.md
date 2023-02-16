
# MacWarder

![MacWarder logo](images/MacWarderLogo.png)

MacWarder is a Python3 program that allows you to spoof Mac addresses on Linux systems.

## Prerequisites

Before using MacWarder, you need to make sure that Python3 is installed on your system. You can check if Python3 is installed by opening a terminal window and typing:

`python3 --version` 

If Python3 is installed, the version number will be displayed. If Python3 is not installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/) or using the terminal.

For Ubuntu and Debian:

`sudo apt-get update`
`sudo apt-get install python3`


For Fedora and CentOS:

`sudo dnf install python3`


For Arch Linux:

`sudo pacman -S python`


For openSUSE:

`sudo zypper install python3`


For Gentoo:

`sudo emerge --ask dev-lang/python`

## Installation

To install MacWarder, you first need to clone this Git repository. You can do this by opening a terminal window and typing:
`git clone https://github.com/sastre0x0/MacWarder.git` 

## Usage

To use MacWarder, open a terminal window and navigate to the directory containing the MacWarder.py file. Then, execute the following command with the required arguments:

`python3 MacWarder.py -i [interface] -m [new_mac]`

Replace [interface] with the name of the network interface you want to use and [new_mac] with the new MAC address you want to set.

For example, if you want to change the MAC address of the eth0 interface to 00:11:22:33:44:55, you would run the following command:

`sudo python3 MacWarder.py -i eth0 -m 00:11:22:33:44:55`

If you don't provide the -i and -m arguments, the program will prompt you to enter the interface and new MAC address when it starts.

You can also use "r" or "random" to generate a random MAC address. For example:

`sudo python3 MacWarder.py -i eth0 -m random`

This will generate a random MAC address and assign it to the eth0 interface.

Please note that you need to run MacWarder as a superuser using sudo. This is necessary to be able to change the MAC address.

## Moving MacWarder to the PATH on Debian systems (OPTIONAL)

**Note:** If you move the MacWarder script to the PATH, you will only be able to use the program with the `-i` and `-m` flags to specify the interface and MAC address. You won't be able to select the interface and MAC address via input prompts. If you prefer to use the input prompts, you can continue to run the program directly from the MacWarder directory.

If you really want to move MacWarder to the PATH follow the next steps.

1. Open the terminal and navigate to the directory where MacWarder is located.

2. Check the current PATH by running the command echo $PATH.

3. Copy the MacWarder file to the /usr/local/bin directory with the command

`sudo cp MacWarder.py /usr/local/bin/MacWarder`

4. Make sure the MacWarder file is executable by running the command

`sudo chmod +x /usr/local/bin/MacWarder`

5. Check if the MacWarder is accessible by running 

`MacWarder -h`

If you want to remove MacWarder from the PATH, you can simply run the command

`sudo rm /usr/local/bin/MacWarder`

If the script runs without errors, you have successfully moved it to a directory in your PATH.

Please note that moving the script to a directory in your PATH is an optional step. You can still execute the script from the MacWarder directory without needing to move it.

## License

This program is released under the GNU GENERAL PUBLIC LICENSE Version 3. For more information, please see the `LICENSE` file at the top of this document.

## Images

The images folder contains the MacWarder logo used at the top of this document.
