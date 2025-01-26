VoiceSync.
 🎯
Basic Details:
Team Name: Dev Divas
Team Members
Member 1: Diya Elsa George - Govt. Model Engineering College
Member 2: Aswini P - Govt. Model Engineering College
Member 3: Adhina Anup - Govt. Model Engineering College
Hosted Project Link
[mention your project hosted project link here]

Project Description:

VocalSync is a revolutionary tool designed to assist individuals with stuttering by:

1.Converting stuttered speech into fluent text.
2.Transforming the fluent text into natural-sounding voice output.

This project aims to bridge communication gaps, enhance confidence, and empower individuals with stammering to express themselves fluently in real-time.

The Problem statement:

People with stammering find it very difficult to talk with normal people.
To solve such an indiscrepancy we decided to implement this project that takes stuttered speech as an input and converts it into a normal speech. 

The Solution
To address the problem, we leveraged:

Real-time voice capturing technology.

Advanced speech processing algorithms to correct stuttering patterns.

Text-to-speech engines to provide fluent and natural-sounding voice outputs.



Technical Details
Technologies/Components Used
For Software:

* Frontend: html,css,javascript for user interaction
* Backend: Python for implementing NLP module
* API: Flask framework
* Speech-to-text Conversion: 
* Text-to-speech Conversion:

For Hardware:
Microphone (to capture live speech input)

Laptop/Desktop (for processing and output)


Implementation
For Software:

--> The website implemented has three webpages.
    --> The first page is a starting interface that act as a home page.
    --> The second page allows users to record their speech and the stuttered speech will be displayed. 
    --> The stuttered text is fetched by using Flask API and is given as an input to the NLP module .
    --> NLP module uses the nltk toolkit that has in built functions to remove repeating characters, words and sentences.
    --> The corrected speech from the NLP module is fetched by the flask and is displayed on the third page.
    --> By using the Text-to-Speech converter, the corrected text is converted to speech
    --> Back buttons are also added for moving to the previous pages.

Installation
pip install flask
pip install nltk
pip install SpeechRecognisition

Project Documentation
For Software:

Screenshots (Add at least 3)

![Screenshot1] Added as Screenshot(2).png in repo


![Screenshot2]Added as Screenshot(4).png in repo

![Screenshot3]Added as Screenshot(5).png in repo


Build Photos
![Team] Added in repo

Project Demo
Video
https://youtu.be/0A5MuWJvrbs

Team Contributions:

Diya Elsa George: Developed the speech-to-text conversion module and text-to-speech conversion module.

Adhina Anup: Implemented the stuttering correction algorithms and managed real-time processing.

Aswini P: Designed the user interface and have done deployment.
