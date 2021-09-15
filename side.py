import os
import time
import requests
import datetime

def ping():
    """
    ping the website
    """
    try:
        r = requests.get('https://texasrighttolife.com/')
        return r
    except:
        return False

def write_log(r):
    """
    write the details of the ping to a log file
    """
    with open('ping_log.txt', 'a') as f:
        f.write(str(r.status_code) + '\n')
        f.write(str(r.elapsed.total_seconds()) + '\n')
        f.write(str(datetime.datetime.now()) + '\n')
        f.write('\n')

def check_log():
    """
    check the log file to see if it has more than 250 lines
    """
    if os.stat('ping_log.txt').st_size > 250000:
        return True
    else:
        return False

def main():
    """
    main function
    """
    while True:
        r = ping()
        if r:
            print(r.status_code)
            print(r.elapsed.total_seconds())
            print(datetime.datetime.now())
            write_log(r)
            if check_log():
                with open('ping_log.txt', 'r') as f:
                    lines = f.readlines()
                with open('ping_log.txt', 'w') as f:
                    f.writelines(lines[3:])
        else:
            print('error')
        time.sleep(.5)

if __name__ == '__main__':
    main()