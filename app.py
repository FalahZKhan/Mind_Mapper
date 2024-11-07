from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes import api  # Import the API routes

app = Flask(__name__)

# Configure your Flask app
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize JWTManager
jwt = JWTManager(app)

# Register the API blueprint
app.register_blueprint(api, url_prefix='/api')

# Define routes for the main app
@app.route('/')
def index():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
