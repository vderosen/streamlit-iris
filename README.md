# Streamlit Iris

A minimal Streamlit app to explore the Iris dataset, filter data interactively, visualize results, and train a simple classifier.  
The purpose of this project is to demonstrate good project structure with testing, containerization, and continuous integration for the final project of the "Tooling for Data Science" module at the MSci Data Science & AI for Business

---

## Quickstart

Clone the repository, install dependencies, run tests, and launch the app:

```bash
git clone https://github.com/your-username/streamlit-iris.git
cd streamlit-iris
pip install -r requirements.txt
pytest
streamlit run app.py
```

Open your browser at: http://localhost:8501

---

## Features
Load and explore the Iris dataset
Interactive filtering of numeric columns
Scatter plots for visualizing relationships
Train a simple logistic regression classifier and display accuracy
Unit tests for data import and filtering
Containerized with Docker for reproducible deployment
GitHub Actions CI to run tests and validate Docker builds on each push

## How it Works
The app demonstrates a simple end-to-end workflow:

1. Data import
The Iris dataset is loaded from scikit-learn into a Pandas DataFrame.
Columns are renamed for clarity, and the target is mapped to species names.

2. Filtering
Users can select a numeric column and apply range filters.
The dataset updates dynamically based on user input.

3. Visualization
Scatter plots are generated between two chosen features.
Data points are colored by species.

4. Model training
A logistic regression classifier is trained on the filtered dataset.
Accuracy on a holdout test set is reported.

---

## Project Structure
```bash

streamlit-iris/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Optional pytest config
├── Dockerfile            # Containerization recipe
├── src/iris_app/         # Core library code
│   ├── __init__.py
│   ├── data.py           # Load dataset
│   ├── features.py       # Filtering and preprocessing
│   ├── model.py          # ML pipeline (Logistic Regression)
│   └── viz.py            # Visualizations
├── tests/                # Unit tests
│   ├── test_data.py
│   └── test_features.py
└── .github/workflows/    # CI workflows (pytest + Docker build)
    └── ci.yml

```

## Docker Instructions
Build the image:

```bash
docker build -t streamlit-iris:latest .
```

Run the container:

```bash
docker run -p 8501:8501 streamlit-iris:latest
```
Then open: http://localhost:8501

## Continuous Integration
This project uses GitHub Actions for Continuous Integration.
On every push or pull request:
- Run tests with pytest on Python 3.11
- Build the Docker image to ensure reproducibility

You can find the workflow file in .github/workflows/ci.yml.

## Author
Vassili de Rosen - Data Science & AI for Business
Based on the Iris dataset (Fisher, 1936) provided by scikit-learn
