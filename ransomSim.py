import os
import socket 
import time 
import sys 
from cryptography.fernet import Fernet

def check_safety():

    current_hostname=socket.gethostname()

    try:
        print("it will start in 10 seconds you have 10 seconds to save your files break with ctrl+c")
        for i in range (10,0,-1):
            print(f"{i} seconds remaining")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit()



def generate_and_save_key():
    encrypted_key=Fernet.generate_key()
    with open("encrypted_key.key","wb") as key_file:
        key_file.write(encrypted_key)

    return encrypted_key
















def main():
    check_safety()
    generate_and_save_key()

if __name__ == "__main__":
    main()
