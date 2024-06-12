# PestSentry

![WhatsApp Image 2024-06-12 at 12 11 03_95afbde9](https://github.com/Estherkiguru/PestSentry_api/assets/138945105/e3f6b470-7ce2-4f62-a24a-817894060f77)


Pestsentry is an API designed for detecting pesticide residues in agricultural products using spectral data analysis. The API provides a reliable and fast method for ensuring food safety and ethical agricultural practices. This project aims to assist in the monitoring and management of pesticide usage in agriculture, contributing to healthier and safer food production.

**Deployed Site:** https://pestsentry-api.onrender.com

**Project Blog article:** 

**LinkedIn:** http://linkedin.com/in/esther-kiguru-wambui


## Inspiration and Background

The inspiration for Pestsentry came from the growing concern over food safety and the need for more efficient methods to detect harmful pesticide residues in agricultural products. Traditional methods are often time-consuming and expensive. By leveraging spectral data analysis, we aim to provide a more accessible and quicker solution for farmers, regulators, and consumers.


## Technical Details
Pestsentry utilizes spectral data analysis to identify and quantify pesticide residues. The core technology involves machine learning algorithms that have been trained on extensive spectral data samples. The API is built using Flask, and the machine learning models are implemented in TensorFlow.

### Algorithm and Model
We use a Convolutional Neural Network (CNN) to analyze the spectral data. The CNN is trained on labeled datasets of spectra corresponding to different pesticides. The model's architecture allows it to learn intricate patterns in the spectral data, enabling accurate detection and quantification.

### Challenges Faced
- **Model Training:** Training the model to achieve high accuracy required significant computational resources and tuning of hyperparameters.
- **Integration:** Ensuring seamless integration between the Flask API and the machine learning model was crucial for providing fast and reliable responses.

## Installation

1. **Clone the repository:**
git clone https://github.com/yourusername/PestSentry_api.git
cd PestSentry_api

3. **Set up a virtual environment:**
 
 python -m venv PestSentry_api
 source PestSentry_api/bin/activate

4. **Install dependencies:**

   pip install -r requirements.txt


## Usage

1. **Run the application:**
To run the API, execute the following command in the 'api' directory:

   python run.py

The application will be accessible at http://127.0.0.1:5000.

### Using the API
- Create a new account or log in to your existing account

- Upload your spectral data for analysis in CSV or Excel form

-  The API will process the data and provide analysis results.


## Contributing

We welcome contributions to improve the Pestsentry API. Please follow these steps:

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).

3. Commit your changes (git commit -am 'Add new feature').

4. Push to the branch (git push origin feature-branch).

5. Create a new Pull Request.


## Related Projects

pesticide Detection Model

Agricultural Data Analysis Tools

## Future Vision
In the next iteration, we aim to:
- **Enhance User Interface:** Develop a more intuitive and user-friendly interface.
- **Real-time Analysis:** Implement real-time analysis capabilities for faster results.

