import os
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager
from functions import plot_closest_pair, allowed_file, save_file, parse_points_from_file, closest_pair_algorithm
from routes import api  # Import routes from the routes.py

app = Flask(__name__)

# Configuring the Flask app
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt'}

# Initializing JWTManager
jwt = JWTManager(app)

# Registering API blueprint
app.register_blueprint(api, url_prefix='/api')

# Route for the homepage
@app.route('/')
def homepage():
    return render_template('dashboard.html')

# Route for finding the closest pair
@app.route('/closest-pair', methods=['GET', 'POST'])
def closest_pair():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = save_file(file)
            points = parse_points_from_file(filename)
            closest_pair, distance = closest_pair_algorithm(points)
            
            # Generate and save the plot in the static folder (step 0 initially)
            plot_filename = 'static/plots/step_0.png'
            plot_closest_pair(points, closest_pair, distance, plot_filename)

            # Get all the plot files in the static/plots directory and sort them
            plot_dir = os.path.join(app.root_path, 'static', 'plots')
            plot_files = [f for f in os.listdir(plot_dir) if f.endswith('.png')]
            plot_files.sort(key=lambda f: int(f.split('_')[1].split('.')[0]), reverse=True)

            return render_template('closest.html', closest_pair=closest_pair, distance=distance, plot_files=plot_files)
        else:
            return jsonify({'error': 'Invalid file format.'}), 400
    return render_template('closest.html')

# Route for integer multiplication problem
@app.route('/integer-multiplication')
def integer_multiplication():
    return render_template('integer.html')

if __name__ == '__main__':
    app.run(debug=True)
