from flask import Flask, send_from_directory
import os

# Initialize Flask app, pointing the static folder to the React build output ('dist')
app = Flask(__name__, static_folder='dist', static_url_path='')

# Create a catch-all route for the Single Page Application (SPA)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # If the file exists in the static folder, serve it (e.g. JS, CSS, images)
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    # Otherwise, return index.html to let React Router handle the route
    else:
        # Note: make sure to build the React app first!
        if not os.path.exists(os.path.join(app.static_folder, 'index.html')):
            return "React build not found! Please run 'npm run build' first.", 404
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    # Run server on all interfaces (0.0.0.0) so it's accessible on your local network
    # E.g. http://192.168.0.x:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
