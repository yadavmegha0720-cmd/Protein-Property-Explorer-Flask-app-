# Protein-Property-Explorer-Flask-app-
Protein Property Explorer (Flask App)
Project Overview
This is a web-based application built with the Flask framework that allows users to upload a protein sequence in FASTA format and instantly generate a hydropathy plot. This project showcases my skills in full-stack development, from handling file uploads and server-side processing to rendering dynamic data visualizations in a web browser. It's a great example of applying coding to a biomedical challenge.

Skills Demonstrated:

Flask: Building a web application with a simple front-end and back-end.

Python: Used for all server-side logic, including file parsing and plot generation.

Matplotlib: For creating the scientific visualization (the hydropathy plot).

HTML/Tailwind CSS: For designing a clean, user-friendly interface.

Data Handling: Processing and validating user-uploaded data.

What is a Hydropathy Plot?
A hydropathy plot is a chart that shows the hydrophobic (water-repelling) or hydrophilic (water-attracting) properties of a protein along its amino acid sequence. It is often used to predict regions of a protein that are likely to be transmembrane domains, which are crucial for understanding a protein's function and structure.

How to Run
Prerequisites
Python 3.x

The following Python libraries:

Flask

pandas

matplotlib

You can install them by running this command in your terminal:

pip install Flask pandas matplotlib

Setup
Create a new folder for your project.

Inside this folder, create a subfolder named templates.

Save the Python code as app.py in the main project folder.

Save the HTML code as index.html inside the templates folder.

Execution
Open your terminal or command prompt.

Navigate to the main project folder.

Run the application using this command:

python app.py

The application will start, and you will see a link (usually http://127.0.0.1:5000). Open this link in your web browser to use the tool.

Future Improvements
Implement a smoother plot.show() call so that the browser does not freeze.

Add more interactive elements to the plot using libraries like Plotly.

Include the ability to calculate other protein properties, such as isoelectric point (pI) or molecular weight.

Allow for direct input of a protein sequence in a text field, in addition to file upload.
