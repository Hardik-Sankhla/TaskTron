# TaskTron

**Task Automator Web Application**

## Overview

TaskTron is a powerful web application designed to automate a wide variety of tasks through both voice and text commands. The application offers features such as executing system commands, sending emails, downloading YouTube videos and audio, and more. With real-time server logs and status updates, TaskTron provides an efficient and interactive experience for users.

## Features

- **Voice Command Execution**: Perform system commands via voice input.
- **Email Automation**: Send emails with custom subjects and messages.
- **YouTube Content Download**: Download videos and audio directly from YouTube.
- **Real-Time Logs**: Monitor server logs and status updates in real-time.
- **User Authentication**: Secure login and authentication for users.
- **Chatbot Integrations**: Enhanced communication through various chatbot integrations.

## Technologies Utilized

- **Programming Language**: Python
- **Web Framework**: Flask
- **Real-time Communication**: Flask-SocketIO
- **Voice Recognition**: SpeechRecognition
- **Logging**: Logging, RotatingFileHandler
- **Email Handling**: smtplib, email.mime
- **YouTube Downloading**: pytube
- **Front-end Technologies**: HTML, CSS, JavaScript

## Chatbot Integrations

The Autotasker chatbot has been upgraded with the following integrations to enhance its functionality and interactivity:

- **Webchat**: Implemented via Botpress for seamless communication through a web interface.
- **groq**: Utilized for advanced query processing, allowing efficient handling of complex tasks.
- **OpenAI**: Incorporated to provide intelligent, context-aware responses through AI models.
- **Anthropic**: Ensured safe and ethical AI interactions, fostering responsible conversation dynamics.
- **Browser**: Enabled dynamic web interactions, allowing the chatbot to browse and retrieve information on the go.
- **Charts**: Integrated real-time data visualization capabilities, supporting various chart types for immediate analysis.
- **Chat for Botpress**: Ensured smooth HTTP-based interactions within the Botpress framework.

### Chatbot Integration Visuals

<div align="center">
  <table>
    <tr>
      <td><img src="https://github.com/Hardik-Sankhla/TaskTron/blob/main/Chatbot/1.png" alt="Integration 1" width="450"/></td>
      <td><img src="https://github.com/Hardik-Sankhla/TaskTron/blob/main/Chatbot/2.png" alt="Integration 2" width="450"/></td>
    </tr>
    <tr>
      <td><img src="https://github.com/Hardik-Sankhla/TaskTron/blob/main/Chatbot/3.png" alt="Integration 3" width="450"/></td>
      <td><img src="https://github.com/Hardik-Sankhla/TaskTron/blob/main/Chatbot/4.png" alt="Integration 4" width="450"/></td>
    </tr>
  </table>
</div>

## Python Tasks Accomplished

In addition to core functionalities, several specific Python-based tasks were completed:

- **Email Messaging**: Developed Python scripts to send email messages.
- **SMS Messaging**: Created Python scripts to send SMS messages.
- **Web Scraping**: Implemented Python code to scrape and retrieve the top 5 search results from Google.
- **Geo-location**: Developed Python code to identify and provide current geo-coordinates and location data.
- **Text-to-Audio Conversion**: Created a Python script for converting text to audio.
- **Volume Control**: Implemented Python code for controlling laptop volume.
- **Mobile SMS Integration**: Developed Python code to connect to mobile devices for sending SMS using the mobile messaging app.
- **Bulk Email Sending**: Created Python functions for sending bulk emails efficiently.

## Machine Learning Tasks Accomplished

The project integrated several machine learning tasks into the application:

- **Automated Data Processing**: Developed Python programs to automate data processing on datasets.
- **Model Integration**: Created and integrated a machine learning model within the web application.
- **Image Processing**: Captured images, cropped faces, and applied various filters.
- **Custom Image Creation**: Utilized numpy for generating custom images.
- **Cool Filters**: Applied entertaining filters like sunglasses and stars to images.

## GenAIOps Tasks Accomplished

For the GenAIOps component, the following tasks were completed:

- **Google Drive Search**: Created a tool to search and retrieve information from Google Drive based on a given prompt.
- **Database Search**: Developed a tool to execute queries on a database according to user prompts.
- **AWS Instance Search**: Implemented a tool to extract information from an AWS instance based on specific prompts.
- **LinkedIn Search**: Designed a tool to search and gather information from LinkedIn according to provided prompts.

## Installation

### Clone the Repository

```bash
git clone https://github.com/Hardik-Sankhla/TaskTron.git
cd TaskTron
Setup Virtual Environment
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
Install the required Python packages using the requirements.txt file:


pip install -r requirements.txt
Configuration
Before running the application, configure your email settings in the send_email function within the app.py file:

python
sender_email = "your_email@example.com"
sender_password = "your_email_password"
Replace these placeholders with your actual email and password.

Running the Application
Start the Flask application with SocketIO:


python app.py
Open your browser and navigate to http://localhost:5000 to view the application.
```

### File Structure

```bash
TaskTron/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── Image/
│       └── Logo1.png
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── tools.html
│   ├── home.html
│   ├── w1.html
│   ├── g3.html
│   ├── NoteEditor.html
│   ├── MemGame.html
│   ├── MusicPlayer.html
│   ├── G2.html
│   ├── char.html
│   ├── comp.html
│   ├── TodoMemo.html
│   ├── G4.html
│   ├── age.html
│   ├── Speed.html
│   └── Yaud.html
│
├── app.py
├── requirements.txt
├── README.md
└── TaskTron.log
```

### Usage :
Voice Commands
TaskTron listens for voice commands and executes them. Some of the supported commands include:

"Open Chrome"
"Open Instagram"
"Open WhatsApp"
"Open Telegram"
"Open Gmail"
"Open Camera"
"Open Snapchat"
"Open Excel"
"Open PowerPoint"
"Open Paint"
"Open Notepad"
"Open OBS Studio"
"Open File Manager"
"Open LW Intern Folder"
"Open Terminal and Run Jupyter Notebook"
"Save Notebook"
"Open Media Player"
"Open LinkedIn"

### Sending Emails

To send an email, use the voice command "send email." The application will prompt for the recipient's email address, subject, and message.

### Downloading YouTube Videos and Audio

TaskTron provides routes to download YouTube content:

/download_video: Download YouTube videos.
/download_audio: Download YouTube audio.

Real-Time Server Logs
Server logs and recognized voice commands are displayed in real-time on the web interface.

## Conclusion
The TaskTron project successfully amalgamates advanced voice recognition, intelligent chatbot functionalities, and specialized Python, Machine Learning, and GenAIOps tasks into a single web-based task automation platform.
Users can effortlessly execute system commands, manage emails, download multimedia content, and engage with an intuitive, feature-rich chatbot.
The application offers real-time updates and comprehensive logging, significantly enhancing user interaction and task monitoring.

## Future Scope

Enhanced Voice Command Recognition: Further improvement of voice command accuracy and expansion of supported commands.
Expanded Automation Features: Inclusion of more system commands and integration with additional third-party services.
User Authentication and Personalization: Implementation of user authentication for personalized settings and command history.
Mobile Application Development: Creation of a mobile version of the application for enhanced accessibility.
Integration with AI Services: Ongoing enhancement of AI capabilities for advanced command recognition, context understanding, and additional chatbot functionalities.

## Contributing

If you'd like to contribute to TaskTron, please follow these steps:

## Fork the repository.

Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
css
Copy code

This updated README file should now include all the details and features of your TaskTron project. You can 
