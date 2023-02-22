# ROS Raspberry Pi

This documentation provides step-by-step instructions for setting up ROS (Robot Operating System) on Raspberry Pi. Please follow the instructions carefully to ensure a successful installation.
## Prerequisites
Before getting started, you will need the following:
* Raspberry Pi with Ubuntu 20.04 OS installed
* An SD card reader
* A Wi-Fi connection
* A computer to act as the main PC
## Steps
1) Install the Raspberry Pi Imager by running the following command in the terminal:  
  ```sudo snap install rpi-imager```  
  Use the Imager to flash the SD card with Ubuntu 20.04 OS. If you plan to use the Raspberry Pi without a screen, make sure to enable SSH and enter the Wi-Fi SSID and password during the setup.  
2)Enable the internal Bluetooth controller by running the following command:  
```sudo apt install pi-bluetooth```

3) Check the date on the Raspberry Pi. An incorrect date can cause installation issues. To check the date, run the following command:  
```date```  
Check the date on the Raspberry Pi. An incorrect date can cause installation issues. To check the date, run the following command:  
```sudo date --set "dd mm aaaa hh:mm:ss" ```  
 Replace dd mm aaaa hh:mm:ss with the actual date and time.  

4)Install ROS Noetic by following the instructions in the official documentation [here].  

5) Clone the following repository using the terminal:  
```git clone https://github.com/your-username/your-repository.git```  
6) Download or clone the sphero v2 library and manually copy it into the scripts folder of your repository.  

7) Set up the main PC as the host by exporting the IP address of the computer in the terminal:  
```export ROS_MASTER_URI=http://<your-PC-IP-address>:11311 ```  
  
8) set the ROS master URI address to the main PC by running the following command in the terminal:  
  
  
