# Project Title: Protein Property Explorer (Flask App)
#
# This project creates a simple web application using Flask. The app allows
# a user to upload a FASTA file containing a protein sequence and then
# generates a hydropathy plot of the sequence using matplotlib. This
# project combines web development (Flask) with data visualization (matplotlib)
# and showcases a full-stack, data-driven application.
#
# The code is well-commented to guide you through the process of setting up
# a web application from scratch.
#
# To run this code, you will need to install Flask, pandas, and matplotlib:
# pip install Flask pandas matplotlib
#

import io
import re
import base64
from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Amino acid hydropathy values for plotting
hydropathy_values = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'Q': -3.5, 'E': -3.5,
    'G': -0.4, 'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8,
    'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

def parse_fasta_for_protein(fasta_content):
    """
    Parses FASTA content to extract the first protein sequence.
    Returns the header and sequence.
    """
    header = None
    sequence = ''
    lines = fasta_content.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if header is None:
                header = line[1:].split()[0]
        else:
            if header is not None:
                sequence += line
    return header, sequence.upper()

def create_hydropathy_plot(sequence, header):
    """
    Generates a hydropathy plot for a given protein sequence.
    Returns the plot as a base64 encoded string.
    """
    if not sequence:
        return None
    
    # Calculate hydropathy scores for each amino acid in the sequence
    scores = [hydropathy_values.get(aa, 0) for aa in sequence]
    
    plt.figure(figsize=(10, 6))
    plt.plot(scores)
    plt.title(f'Hydropathy Plot for {header}')
    plt.xlabel('Amino Acid Position')
    plt.ylabel('Hydropathy Score')
    plt.grid(True)
    
    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    # Encode the image to base64 for embedding in HTML
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return image_base64

# --- Flask Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route for the web application. Handles file upload and plot generation.
    """
    plot_data = None
    sequence_name = None
    error_message = None

    if request.method == 'POST':
        if 'fasta_file' not in request.files:
            error_message = 'No file part'
        else:
            file = request.files['fasta_file']
            if file.filename == '':
                error_message = 'No selected file'
            elif file:
                fasta_content = file.read().decode('utf-8')
                sequence_name, protein_sequence = parse_fasta_for_protein(fasta_content)
                if not protein_sequence:
                    error_message = 'Invalid or empty protein sequence in FASTA file'
                else:
                    plot_data = create_hydropathy_plot(protein_sequence, sequence_name)
                    if plot_data is None:
                        error_message = 'Failed to generate plot'
    
    return render_template('index.html', plot_data=plot_data, sequence_name=sequence_name, error=error_message)

@app.route('/index.html')
def index_html():
    return render_template('index.html')

if __name__ == '__main__':
    # To run the app, you need to create the 'templates' folder and 'index.html' file.
    # The 'index.html' code is provided below.
    app.run(debug=True)

