# website-blocker
Python script to block certain websites during specific times of the day. This simple python scripts modifies the hosts file on the host computer depending on the time of day. Any website in the website list are redirected to the local host ip address 127.0.0.1 during the specified time of day

The list of websites are assigned to the variable "website_list"
time_at_8_am and time_at_4_pm are the variables that are assigned work hours and off work hours.

For the script to run as a window process, it needs to be renamed to use the .pyw extension.
This program can be packaged as a wondows.exe file using python "pyinstaller".
To generate a .exe file run do the following:
pip install pyinstaller
Navigate to the directory where your .pyw script is and then run the following 
pyinstaller --onefile --windowed <scriptname>
  Finally this can then be scheduled using windows task scheduler. Ensure to tick the option to "run with highest privileges". This is needed because admin right is required to modify the etc\hosts file on the host pc.
