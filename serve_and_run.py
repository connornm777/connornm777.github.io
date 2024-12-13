import http.server
import socketserver
import webbrowser
import os
import sys
import time
from contextlib import closing

# Server configuration
PORT = 0  # Let the OS assign an available port
DIRECTORY = os.path.abspath('.')  # Use current directory as the root


# Define the handler with cache prevention
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Prevent caching by adding appropriate headers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()


# Function to open the browser in a new window
def open_browser(port):
    # Append a timestamp to the URL to further ensure fresh loading
    timestamp = int(time.time())
    url = f'http://localhost:{port}/index.html?cache_bust={timestamp}'
    print(f"Opening {url} in a new browser window...")

    # Attempt to open the URL in a new browser window
    try:
        # 'new=1' attempts to open in a new window
        opened = webbrowser.open(url, new=1)
        if not opened:
            print("Failed to open the browser automatically. Please open the URL manually.")
    except Exception as e:
        print(f"An error occurred while trying to open the browser: {e}")


# Function to find an available port (optional alternative method)
def find_free_port(start_port=8000, end_port=9000):
    for port in range(start_port, end_port):
        with closing(socketserver.TCPServer(("", port), CustomHandler)) as test_server:
            try:
                test_server.server_bind()
                test_server.server_close()
                return port
            except OSError:
                continue
    raise RuntimeError(f"No free ports available in range {start_port}-{end_port}.")


# Start the server
def start_server():
    # Using PORT=0 lets the OS pick an available port
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        # Retrieve the assigned port
        assigned_port = httpd.server_address[1]
        print(f"Serving at http://localhost:{assigned_port}/")

        # Open the browser to the assigned port
        open_browser(assigned_port)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server.")
            httpd.server_close()
            sys.exit(0)


if __name__ == "__main__":
    start_server()
