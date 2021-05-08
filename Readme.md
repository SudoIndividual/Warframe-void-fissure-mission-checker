# Warframe void fissure mission tracker
## Description
This Python script uses [Callmebot](https://www.callmebot.com/blog/free-api-whatsapp-messages/) API to send message via whatsapp to users every 30 mins to notify about the user choice of mission and [Warframestat](https://docs.warframestat.us/) API to find the current mission for the certain platform. To setup up this bot, you will need follow the steps to set up [Callmebot](https://www.callmebot.com/blog/free-api-whatsapp-messages/)  , install the necessary requirements for it to work and most importantly **Python**. 

Currently this programm only notify user on whatsapp. Will implement more feature.

## Usuage
To run the script do:

    python3 Main.py
Import the necessary info and follow this guide line

 - do not input anything else except given options
 - For missions and relic, you can select as many as you want as long as it is seperated with a comma

## Setup
Git clone the file into your directory

    git clone https://github.com/Zhien02/Warframe-void-fissure-mission-checker.git
In command prompt go to the cloned directory

    cd Warframe-void-fissure-mission-checker
  Install the necessary requirements

    pip3 install -r requirements.txt
  
Run the script

    python3 Main.py
Do not close the program if you want the bot to continue to run

## Edit
If you want to edit how long the bot send you updates. Change the value in the bracket of time.sleep(). This code is located at the bottom of the code as seen in the image.
![](https://github.com/Zhien02/Warframe-void-fissure-mission-checker/blob/master/Image/Edit.PNG)


