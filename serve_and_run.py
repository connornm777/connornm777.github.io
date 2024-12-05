import http.server
import socketserver
import webbrowser
import os

# Server configuration
PORT = 8000
DIRECTORY = os.path.abspath('.')  # Use current directory as the root

# Define the handler
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Open the browser
def open_browser():
    url = f'http://localhost:{PORT}/index.html'
    print(f"Opening {url} in the default browser...")
    webbrowser.open(url)

# Start the server
def start_server():
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}/")
        open_browser()  # Open browser after the server starts
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
