Course: CMPT 371 - Data Communications & Networking  
Instructor: Mirza Zaeem Baig  
Semester: Spring 2026  




Group Members
TANUSH DHOOPAR, JASON SANDHU 
301596040, 301584310


1. Project Overview & Description

This project is a Peer-to-Peer (P2P) chat application built using Python’s Socket API (TCP) and a graphical user interface (GUI) using Tkinter. The application allows two users to establish a direct connection and exchange messages in real-time without the need for a centralized server.

One user acts as the host, creating a listening socket, while the other user joins by connecting to the host’s IP address and port. The application demonstrates core networking concepts such as socket creation, connection establishment, data transmission, and concurrent communication using threads.



2. System Limitations & Edge Cases

As required by the project specifications, the following limitations and potential issues have been identified:

Handling Multiple Clients Concurrently:  
Solution: The application uses Python’s threading module to handle message receiving in a separate thread, ensuring the GUI remains responsive.  
Limitation: The system only supports a single peer-to-peer connection (2 users). It does not scale to multiple clients.

Client Disconnection:  
Solution: If a peer disconnects, the application detects an empty message or exception and safely closes the connection.  
Limitation: There is no automatic reconnection feature.

Network Errors / Invalid Input:  
Solution: Basic error handling is implemented using try/except blocks to prevent crashes.  
Limitation: No advanced validation or recovery mechanisms are implemented.

High Latency:  
Limitation: Messages may be delayed depending on network conditions. No buffering or optimization is implemented.

Security:  
Limitation: Messages are transmitted in plain text. No encryption or authentication is implemented.



3. Video Demo

https://www.youtube.com/watch?v=T96xUCGRjRA

Our 2-minute video demonstration covering connection establishment, data exchange, and application termination can be viewed below:

Watch Project Demo: 


4. Prerequisites (Fresh Environment)

To run this project, you need:

- Python 3.10 or higher
- Tkinter (for GUI)

Built-in libraries used:
- socket
- threading

RUBRIC NOTE: A requirements.txt file is included. Tkinter may require installation depending on the system.


5. Step-by-Step Run Guide

RUBRIC NOTE: The grader must be able to copy-paste these commands.



Step 1: Start Host (User 1)

Open terminal and run:

python main.py

In the application:
- Select "Host"
- Enter a port (e.g., 5000)
- Click "Start"


Step 2: Start Client (User 2)

Open a second terminal and run:

python main.py


   In the application:
- Select "Join"
- Enter host IP:
  - Use `127.0.0.1` for same machine
  - Or local IP (e.g., 192.168.x.x) for different devices
- Enter same port (e.g., 5000)
- Click "Start"



    Step 3: Chat

- Once connected, both users can send messages
- Messages appear in real-time
- If one user disconnects, the connection closes


6. Technical Protocol Details

The application uses TCP sockets for communication.

- Protocol: TCP
- Communication Type: Peer-to-Peer (direct connection)
- Message Format: Plain text strings encoded using UTF-8
- Sending: sendall()
- Receiving: recv(1024)

Threading is used to continuously listen for incoming messages without blocking the GUI.



7. Academic Integrity & References

RUBRIC NOTE: List all references used and help you got.

Code Origin:  
The socket structure and GUI integration were developed based on course concepts and lectures. All networking logic, threading, and application functionality were implemented independently.

GenAI Usage:  
ChatGPT was used to assist in designing and refining the graphical user interface (GUI) .

References:
- Python Socket Programming Documentation  
- Tkinter Documentation  
- Course Lecture Notes and Tutorials  

