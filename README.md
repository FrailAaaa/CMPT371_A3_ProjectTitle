Assignment3-371: Peer-to-Peer Chat Application

Course: CMPT 371 - Data Communications & Networking
Instructor: Mirza Zaeem Baig
Semester: Spring 2026

Group Members
Name	Student ID
TANUSH DHOOPAR	301596040
JASON SANDHU	301584310
1. Project Description

This project is a Peer-to-Peer (P2P) chat application developed using Python and the Socket API. It allows two users to communicate directly over a TCP connection without requiring a centralized server.

The application provides two modes:

Host Mode: Starts a server and waits for a connection
Join Mode: Connects to an existing host using an IP address and port

A graphical user interface (GUI) is implemented using Tkinter to make interaction simple and user-friendly.

2. Limitations and Design Considerations

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
No automatic
no i need to be able to copy and past it in

Got you — here is a clean, no-formatting-weirdness, fully copy-pasteable README.md. Just copy everything below directly into your README file.

Assignment3-371: Peer-to-Peer Chat Application

Course: CMPT 371 - Data Communications & Networking
Instructor: Mirza Zaeem Baig
Semester: Spring 2026

Group Members
Name	Student ID
TANUSH DHOOPAR	301596040
JASON SANDHU	301584310
1. Project Description

This project is a Peer-to-Peer (P2P) chat application developed using Python and the Socket API. It allows two users to communicate directly over a TCP connection without requiring a centralized server.

The application provides two modes:

Host Mode: Starts a server and waits for a connection
Join Mode: Connects to an existing host using an IP address and port

A graphical user interface (GUI) is implemented using Tkinter to make interaction simple and user-friendly.

2. Limitations and Design Considerations

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
3. Video Demo

(Add your video link here)

4. Requirements
Software Requirements
Python 3.x
5. Setup and Installation Guide

Follow these steps exactly to run the application on a fresh system.

Step 1: Download the Project

Option 1 (Git):
git clone <your-repo-link>
cd <repo-folder>

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

Windows:
pip install tk

Linux:
sudo apt-get install python3-tk

Mac:
brew install python-tk
