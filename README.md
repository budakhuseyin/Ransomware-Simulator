# RansomSim & Decrypter
Project Overview
This project is developed as a part of a larger personal cybersecurity initiative called RansomCatch, which focuses on behavioral-based ransomware detection and prevention systems. To test the detection capabilities of RansomCatch, I have developed this modular Ransomware Simulator (RansomSim) and its corresponding recovery tool (Decrypter). The project aims to simulate how modern ransomware operates by encrypting files with the AES-based Fernet algorithm and altering file extensions.

## Purpose of Development
The primary goal of this tool is to provide a controlled environment for:

Monitoring file system anomalies (I/O spikes, entropy changes).

Testing behavioral analysis algorithms against encryption patterns.

Validating the effectiveness of "honey-pot" (decoy) file triggers.

Enhancing my understanding of cryptographic implementations in Python.

## Usage & Warnings
DISCLAIMER: This tool is strictly for educational and ethical security research purposes.

Lab Environment Only: This script should only be executed within a dedicated, isolated laboratory environment or a virtual machine (VM).

User Responsibility: The use of this software is at the user's own discretion and risk. The developer assumes no liability for any unintended data loss or damage caused by misuse.

Safety First: Always ensure you have a fresh system snapshot or a full backup before running the simulation. A built-in 10-second safety delay is included to prevent accidental execution.

## Features
AES Encryption: Uses the cryptography library for high-standard data locking.

Extension Manipulation: Automatically appends .encrypted to target files for behavioral tracking.

Dynamic Path Selection: Allows users to specify target directories through terminal input.

Secure Key Management: Generates a unique encrypted_key.key for each session.

## Installation
Clone the repository.

Install requirements: pip install -r requirements.txt

Run the simulator: python ransomSim.py

Use the decrypter to restore files: python ransomDecrypter.py