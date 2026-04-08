import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class P2PChatGUI:
    """
    This class represents the full Peer-to-Peer chat application.
    It handles both hosting a server and connecting to another peer,
    along with managing the GUI and message flow.
    """

    def __init__(self, root):
        # Store the root window and set title
        self.root = root
        self.root.title("Peer-to-Peer Chat")

        # These will keep track of our connection state
        self.conn = None              # Active socket connection
        self.server_socket = None     # Server socket (only used in host mode)
        self.connected = False        # Simple flag to check if we are connected

        # ------------------- TOP FRAME (SETTINGS) -------------------
        # This section contains all the inputs like mode, ports, etc.
        top_frame = tk.Frame(root)
        top_frame.pack(padx=10, pady=10, fill="x")

        # Mode selection (Host or Join)
        self.mode_var = tk.StringVar(value="host")

        tk.Label(top_frame, text="Mode:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(top_frame, text="Host", variable=self.mode_var, value="host", command=self.update_mode).grid(row=0, column=1, sticky="w")
        tk.Radiobutton(top_frame, text="Join", variable=self.mode_var, value="join", command=self.update_mode).grid(row=0, column=2, sticky="w")

        # Input for listening port (used when hosting)
        tk.Label(top_frame, text="Listening Port:").grid(row=1, column=0, sticky="w")
        self.listen_port_entry = tk.Entry(top_frame)
        self.listen_port_entry.grid(row=1, column=1, padx=5, pady=2)

        # Input for peer IP (used when joining)
        tk.Label(top_frame, text="Peer IP:").grid(row=2, column=0, sticky="w")
        self.peer_ip_entry = tk.Entry(top_frame)
        self.peer_ip_entry.grid(row=2, column=1, padx=5, pady=2)

        # Input for peer port
        tk.Label(top_frame, text="Peer Port:").grid(row=3, column=0, sticky="w")
        self.peer_port_entry = tk.Entry(top_frame)
        self.peer_port_entry.grid(row=3, column=1, padx=5, pady=2)

        # Button to actually start the chat (either host or join)
        self.start_button = tk.Button(top_frame, text="Start", command=self.start_chat)
        self.start_button.grid(row=4, column=0, columnspan=3, pady=10)

        # ------------------- CHAT DISPLAY -------------------
        # This is where messages will show up
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", width=50, height=20)
        self.chat_area.pack(padx=10, pady=10, fill="both", expand=True)

        # ------------------- MESSAGE INPUT -------------------
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(padx=10, pady=10, fill="x")

        # Text box where user types messages
        self.message_entry = tk.Entry(bottom_frame)
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        # Pressing Enter should send the message (makes it feel smoother to use)
        self.message_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(bottom_frame, text="Send", command=self.send_message)
        self.send_button.pack(side="right")

        # Set initial UI state
        self.update_mode()

    def update_mode(self):
        """
        This function updates the UI based on whether the user selects
        Host or Join mode. Basically enables/disables inputs.
        """
        mode = self.mode_var.get()

        if mode == "host":
            # When hosting, you dont need peer IP/port
            self.peer_ip_entry.config(state="disabled")
            self.peer_port_entry.config(state="disabled")
        else:
            # When joining, those fields become important
            self.peer_ip_entry.config(state="normal")
            self.peer_port_entry.config(state="normal")

    def append_chat(self, text):
        """
        Adds a message to the chat window safely.
        We temporarily enable the box, insert text, then disable again
        so user cant edit it manually.
        """
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, text + "\n")
        self.chat_area.see(tk.END)  # Auto-scroll to the latest message
        self.chat_area.config(state="disabled")

    def start_server(self, listen_port):
        """
        Starts the application in host mode.
        This sets up a server socket and waits for another peer to connect.
        """
        try:
            # Create TCP socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Allow quick reuse of the port (avoids annoying restart issues)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind to all available network interfaces
            self.server_socket.bind(("0.0.0.0", listen_port))
            self.server_socket.listen(1)  # Only one peer allowed

            self.append_chat(f"Hosting chat on port {listen_port}...")
            self.append_chat("Waiting for another peer to join...")

            # This will block until someone connects
            conn, addr = self.server_socket.accept()

            # Save connection
            self.conn = conn
            self.connected = True

            self.append_chat(f"Peer joined from {addr[0]}:{addr[1]}")
            self.append_chat("Chat is ready.")

            # Start listening for incoming messages in background
            threading.Thread(target=self.receive_messages, daemon=True).start()

        except Exception as e:
            # Catch any server-related errors
            self.append_chat(f"Server error: {e}")

    def connect_to_host(self, peer_ip, peer_port):
        """
        Connects to another peer (host mode).
        """
        try:
            # Create client socket
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Attempt to connect to the host
            client.connect((peer_ip, peer_port))

            self.conn = client
            self.connected = True

            self.append_chat(f"Connected to host at {peer_ip}:{peer_port}")
            self.append_chat("Chat is ready.")

            # Start receiving messages in background
            threading.Thread(target=self.receive_messages, daemon=True).start()

        except Exception as e:
            self.append_chat(f"Connect error: {e}")

    def receive_messages(self):
        """
        Continuously receives messages from the peer.
        Runs in its own thread so the UI doesnt freeze.
        """
        while True:
            try:
                # Receive and decode message
                msg = self.conn.recv(1024).decode()

                # If empty message, connection likely closed
                if not msg:
                    self.append_chat("Peer disconnected.")
                    break

                # Display received message
                self.append_chat(f"Peer: {msg}")

            except:
                # Any error here usually means connection is gone
                self.append_chat("Connection closed.")
                break

        # Cleanup after disconnect
        self.connected = False

        try:
            if self.conn:
                self.conn.close()
        except:
            pass
        self.conn = None

        try:
            if self.server_socket:
                self.server_socket.close()
        except:
            pass
        self.server_socket = None

    def start_chat(self):
        """
        Entry point when user clicks Start.
        Decides whether to host or join based on selection.
        """
        mode = self.mode_var.get()

        if mode == "host":
            try:
                # Convert port input to integer
                listen_port = int(self.listen_port_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid listening port.")
                return

            # Run server in separate thread so GUI stays responsive
            threading.Thread(target=self.start_server, args=(listen_port,), daemon=True).start()
            self.start_button.config(state="disabled")

        else:
            try:
                peer_ip = self.peer_ip_entry.get().strip()
                peer_port = int(self.peer_port_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid peer port.")
                return

            if not peer_ip:
                messagebox.showerror("Input Error", "Please enter the host IP.")
                return

            # Start connection attempt in background
            threading.Thread(target=self.connect_to_host, args=(peer_ip, peer_port), daemon=True).start()
            self.start_button.config(state="disabled")

    def send_message(self, event=None):
        """
        Sends a message to the connected peer.
        Triggered by button click or pressing Enter.
        """
        msg = self.message_entry.get().strip()

        # Ignore empty messages
        if not msg:
            return

        # Check if we are actually connected
        if not self.connected or self.conn is None:
            messagebox.showwarning("Not Connected", "No connection yet.")
            return

        try:
            # Send message over socket
            self.conn.sendall(msg.encode())

            # Show message in chat window
            self.append_chat(f"You: {msg}")

            # Clear input field after sending
            self.message_entry.delete(0, tk.END)

        except Exception as e:
            self.append_chat(f"Send error: {e}")


# Create main window and run the app
root = tk.Tk()
app = P2PChatGUI(root)
root.mainloop()
