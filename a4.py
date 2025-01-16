import os

shutdown=input("do you wsh to shutdown your computer? (yes or no):")

if shutdown =='no':
    exit()
else:
    os.system("shutdown/s /t 1")