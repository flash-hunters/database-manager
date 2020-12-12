# database-manager

tested on Ubuntu 20.04

### Pre-requisites
Install mongoDB  
Create "invaders" database
Create ""

## Installation

`git clone https://github.com/flash-hunters/database-manager.git`

`cd database-manager`

Copy the configuration file into /etc directory  
```shell script
sudo mkdir /etc/flash-hunters  
sudo cp etc/database_env.sh /etc/flash-hunters
```  

Edit the file with your own configuration  
```shell script
sudo nano /etc/flash-hunters/database_env.sh
```  

### Script automation with crontab

Open editor for crontab  
```shell
crontab -e
```  
and then add the following line (change the script path according to your configuration) :  
`0 22 * * sun ~/database-manager/bin/updateMosaics.sh` (for an update every sunday at 10pm) 