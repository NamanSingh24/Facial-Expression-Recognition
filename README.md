# Facial Expression Recognition

## Overview
This repository contains a facial expression recognition application built using PyTorch. It includes a pre-trained model, a web interface, and all necessary files to run the application on a personal machine.

## Features
- **Model**: Pre-trained PyTorch model for recognizing facial expressions.
- **Web Interface**: Flask-based web interface for interaction with the model.
- **Deployment**: Instructions for deploying the application locally and on Heroku.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Files and Directories](#files-and-directories)
- [Model Details](#model-details)
- [Deployment](#deployment)


## Prerequisites
- Python 3.7+
- pip

## Installation

### Cloning the Repository
1. Clone the repository:
    ```bash
    git clone https://github.com/NamanSingh24/Facial-Expression-Recognition.git
    cd Facial-Expression-Recognition
    ```

### Setting Up the Environment
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

### Installing Dependencies
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application
1. Start the Flask application:
    ```bash
    python app.py
    ```
2. Open your web browser and navigate to `http://127.0.0.1:5000` to access the web interface.

## Files and Directories
- `app.py`: Main Flask application file.
- `best-weights.pt`: Pre-trained model weights.
- `requirements.txt`: List of required Python packages.
- `static/`: Contains static files such as CSS and JavaScript.
- `templates/`: Contains HTML templates for the web interface.
- `model.py`: Script for model architecture and loading weights.
- `utils.py`: Utility functions for data processing and prediction.

## Model Details
- The model is a convolutional neural network (CNN) trained to recognize facial expressions from images.
- It has been trained on a publicly available dataset and achieves state-of-the-art performance in facial expression recognition.

## Deployment



### Local Deployment
- Follow the [Installation](#installation) and [Usage](#usage) steps to run the application on your local machine.


