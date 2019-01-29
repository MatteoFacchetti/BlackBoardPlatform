# Quick access to the BlackBoard platform (Bocconi University)

All the Bocconi students know how annoying is the fact that that you cannot directly access BBoard by just digiting http://blackboard.unibocconi.it/ inside the URL bar. If we have just opened our browser, that link will redirect us to the You@B log in page. Opening the BlackBoard platform is thus not straightforward and requires at least two steps: you can access BBoard only after you have successfully logged into your Agenda You@B.

This program lets you save time by doing it all for you. It will open your Agenda You@B, perform the Log In, and then instantly open BBoard. The program has been written to work smoothly on Linux operating systems (and this step-by-step guide will let you run it on Linux), however it can run on all the operating systems; you might just want to modify the code a little bit if you want to use it on Windows or MacOS (do not worry, the code is short and simply understandable!).

Let's start!

## Quick Setup

First of all, make sure you have *Python* installed on your computer: the program is written in Python and will not run without it.

Second: the program uses Google Chrome to connect to BlackBoard, so make sure you have it installed. Also, you will need a *web driver*, you can download it [here](http://chromedriver.chromium.org/). Once you have downloaded the zip file, extract the webdriver, rename it *webdriver* (it should be named like that by default) and put it inside your **/usr/local/** directory.
In order to do that, you may need *root privileges*: open a terminal and digit

```sudo nautilus```

and enter your password; your file manager will automatically open giving you root privileges. Now you can put the chromedriver inside the folder mentioned above.

After that, download the `bboard.py` file that you find in this repository. Once you have downloaded it, put it inside your **/bin/** directory. If you need to open the file manager with root privileges, just repeat what we have done with the webdriver.

Now open another terminal and run

```sudo chmod +x /bin/bboard.py```

and enter your password.

Last step: open your terminal and install selenium by running

```pip install selenium```

The setup is finally complete!

## Run the program

In order to run the program, you just need to open a terminal and run the following command:

```bboard.py```

A window will pop up asking for your Student ID and your Password. If you digit them correctly, Google Chrome will open and, after few seconds, you will be successfully logged in your BlackBoard platform!

_Disclaimer: your Student ID and your Password ARE NOT shared with anyone when you run this program. You can check the code if you have any doubt._
