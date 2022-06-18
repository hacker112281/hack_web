from time import sleep
from colorama import Fore, init
import platform as pf
import os
import pyfiglet

print('[ 1 ] ddos                    [ 2 ] XXS                         [ 3 ] SQL                       [ 4 ] admin panel                             [ 5 ] port scan') 


if select == '1':
    os.system('python ddos.py') 
    
if select == '2':
    os.system('python3 XXS.py') 
     
if select == '3':
    os.system('python3 SQL.py') 
    
if select == '4':
    os.system('python3 admin_panel.py') 
      
if select == '5': 
    os.system('python3 port_scan.py') 
