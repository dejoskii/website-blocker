import time
from datetime import datetime as dt

hosts_path_temp = r'C:\Users\user\OneDrive\Documents\hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect_ip = '127.0.0.1'
website_list = ['www.bbc.co.uk', 'bbc.co.uk', 'gmail.com', 'facebook.com', 'www.facebook.com']
time_at_8_am = dt(dt.now().year, dt.now().month, dt.now().day, 8)
time_at_4_pm = dt(dt.now().year, dt.now().month, dt.now().day, 16)

while True:
    if time_at_8_am < dt.now() < time_at_4_pm:
        with open(hosts_path_temp, 'r+') as my_hosts_file:
            content = my_hosts_file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    my_hosts_file.write(redirect_ip + '   ' + site + '\n')
        print('Working Hours....')
        time.sleep(5)
    else:
        with open(hosts_path_temp, 'r+') as my_hosts_file:
            content = my_hosts_file.readlines()
            my_hosts_file.seek(0) # Seek(0) is needed because after python reads a file,
            # the cursor is at the end of the file. Hence we need to move the cursor to the beginning of the file
            # Otherwise when you iterate through the variable content it will return empty since there is nothing
            # after the cursor
            for line in content:
                if not any(website in line for website in website_list):# write line only if the website is not in line
                    my_hosts_file.write(line)

            my_hosts_file.truncate()
            print("Fun hours...")
        time.sleep(5)



