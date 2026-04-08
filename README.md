Assignment3-371
Peer-to-Peer Chat Application

Course Information
Course: CMPT 371 - Data Communications & Networking
Instructor: Mirza Zaeem Baig
Semester: Spring 2026

RUBRIC NOTE: As per submission guidelines, only one group member will submit the link to this repository on Canvas.

Group Members

Name: TANUSH DHOOPAR, JASON SANDHU
Student ID: 301596040 , 301584310

Project Description

This project is a Peer-to-Peer (P2P) chat application developed using Python and the Socket API. It allows two users to communicate directly over a TCP connection without requiring a centralized server.

The application provides two modes:

Host Mode: Starts a server and waits for a connection
Join Mode: Connects to an existing host using an IP address and port

A graphical user interface (GUI) is implemented using Tkinter to make interaction simple and user-friendly.

Limitations and Design Considerations

The following limitations and potential issues may arise in this application:

Only supports communication between two users at a time
Messages are sent in plain text (no encryption)
Requires manual input of IP address and port number
No authentication mechanism (any user can connect if IP/port is known)
No persistent message storage (chat history is lost after closing the program)
No support for file transfer or multimedia
Connection may fail if firewall blocks the selected port
If a client disconnects unexpectedly, the connection is terminated
High network latency may cause delays in message delivery
No automatic reconnection handling

Video Demo
Requirements

Software Requirements

Python 3.x

Setup and Installation Guide

Follow these steps exactly to run the application on a fresh system.

Step 1: Download the Project

Option 1 (Git): git clone cd

Option 2:

Download the ZIP from GitHub
Extract it
Open a terminal in the project folder

Step 3: Install Dependencies

Run the following command:

pip install -r requirements.txt

Note:

The application uses built-in libraries such as socket and threading
Tkinter is required for the GUI

If tkinter is not installed on your system:

Windows: pip install tk
Linux: sudo apt-get install python3-tk
Mac: brew install python-tk

Academic Integrity & References

Generative AI tools (ChatGPT) were used to assist in designing and refining the graphical user interface (GUI) components of the application. All networking logic, socket programming, threading, and application functionality were implemented independently.

How to Run the Application

Make sure you are inside the project directory.

Run: python main.py

(Replace main.py with your actual file name if it is different)

How to Use the Application

Case 1: Two Users on the Same Computer

Host (User 1):

Select "Host"
Enter a listening port (e.g., 5000)
Click "Start"
Wait for the second user to connect

Join (User 2):

Select "Join"
Enter IP address: 127.0.0.1
Enter the same port (e.g., 5000)
Click "Start"

Case 2: Two Different Devices (Same Network)

Host:

Find your local IP address

Windows: ipconfig

Mac/Linux: ifconfig

Use your IPv4 address (example: 192.168.x.x)
Start hosting with a chosen port

Join:

Enter the host's IP address
Enter the same port number
Click "Start"

Important Notes

Both users must use the same port number
The host must start first before the client connects
Ensure firewall settings allow the selected port
Use 127.0.0.1 for testing on the same machine
