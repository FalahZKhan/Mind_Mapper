import os
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager
from functions import karatsuba, clear_karatsuba_folder, plot_karatsuba_step, plot_closest_pair, allowed_file, save_file, parse_points_from_file, closest_pair_algorithm
from routes import api  

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

@app.route('/closest-pair', methods=['GET', 'POST'])
def closest_pair():
    plot_files = [] 
    closest_pair = None
    distance = None

    if request.method == 'POST':
        # Handle file upload
        file = request.files.get('file')  # Use .get() to avoid KeyError
        if file and allowed_file(file.filename):
            filename = save_file(file)
            points = parse_points_from_file(filename)
            closest_pair, distance = closest_pair_algorithm(points)
            
            # Generate and save the plot in the static folder (step 0 initially)
            plot_filename = 'static/plots/step_0.png'
            plot_closest_pair(points, closest_pair, distance, plot_filename)

            # Get all the plot files in the static/plots directory and sort them
            plot_dir = os.path.join(app.root_path, 'static', 'plots')
            if os.path.exists(plot_dir):
                plot_files = [f for f in os.listdir(plot_dir) if f.endswith('.png')]
                plot_files.sort(key=lambda f: int(f.split('_')[1].split('.')[0]), reverse=True)

            return render_template('closest.html', closest_pair=closest_pair, distance=distance, plot_files=plot_files)
        else:
            return jsonify({'error': 'Invalid file format.'}), 400

    # Make sure plot_files is passed even on GET request
    return render_template('closest.html', plot_files=plot_files)


@app.route('/integer-multiplication', methods=['GET', 'POST'])
def integer_multiplication():
    result = None
    error = None
    plot_files = []  # Ensure consistent variable name

    if request.method == 'POST':
        file = request.files.get('file')
        
        if file and allowed_file(file.filename):
            filename = save_file(file)
            try:
                with open(filename, 'r') as f:
                    numbers = f.readlines()
                    if len(numbers) >= 2:
                        x = int(numbers[0].strip())
                        y = int(numbers[1].strip())
                        
                        clear_karatsuba_folder()  # Clear Karatsuba plots

                        result = karatsuba(x, y)  # Perform Karatsuba multiplication

                        karatsuba_dir = os.path.join(app.root_path, 'static', 'karatsuba')
                        plot_files = [f for f in os.listdir(karatsuba_dir) if f.endswith('.png')]
                        plot_files.sort(key=lambda f: int(f.split('_')[1].split('.')[0]))  # Sort by step
                    else:
                        error = 'File must contain at least two integers.'
            except ValueError:
                error = 'File contains invalid integer values.'
        else:
            error = 'Invalid file format. Please upload a .txt file.'

    return render_template('integer.html', result=result, error=error, karatsuba_files=plot_files)

if __name__ == '__main__':
    app.run(debug=True)