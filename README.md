
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

## Moving MacWarder to the path

Moving the MacWarder.py script to a directory in your system's PATH environment variable is an optional step that allows you to execute the script from any directory without needing to specify the full path to the script.

To move the script to a directory in your PATH, follow these steps:

1. Find a directory that is already in your PATH. You can view the directories in your PATH by typing the following command in a terminal window:

`echo $PATH`

2. Copy the MacWarder.py script to the directory you found in step 1. You can do this by typing the following command in the terminal window:

`sudo cp /path/to/MacWarder/MacWarder.py /path/to/destination/directory`

Replace /path/to/MacWarder with the actual path to the MacWarder directory and /path/to/destination/directory with the actual path to the destination directory.

3. Make the script executable by typing the following command in the terminal window:

`sudo chmod +x /path/to/destination/directory/MacWarder.py`

Verify that the script can be executed from any directory by typing the following command in the terminal window:

`MacWarder.py`

If the script runs without errors, you have successfully moved it to a directory in your PATH.

Please note that moving the script to a directory in your PATH is an optional step. You can still execute the script from the MacWarder directory without needing to move it.

## License

This program is released under the GNU GENERAL PUBLIC LICENSE Version 3. For more information, please see the `LICENSE` file at the top of this document.

## Images

The images folder contains the MacWarder logo used at the top of this document.
