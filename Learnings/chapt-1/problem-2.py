# install an external module and use it

# in order to solve this problem, we will use the "pyttsx3" module
# install the module using pip
# pip install pyttsx3
# this module is used to convert text to speech

import pyttsx3
engine = pyttsx3.init()
# engine.say("I will speak this text")
engine.say("hey there, this is Mursaleen STB and today is Day 4 of 30 Days of Python Challenge")
engine.runAndWait()
