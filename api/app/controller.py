"""
Handles API endpoints related to user authentication,file upload,model prediction and results download
"""

import os
import io
import csv
from  datetime import datetime
import numpy as np
import pandas as pd
from .forms import LoginForm, SignUpForm
from ._models import classification_model, regression_model
from .db import User, db, AnalysisResult
from app.config import get_logger
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify, render_template, redirect, flash, Response, session, url_for



#Allowed file extensions
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

#Flask Blueprint for API endpoints related to prediction
prediction_app = Blueprint('prediction_app', __name__)
_logger = get_logger(logger_name = __name__)

# Route for the home page
@prediction_app.route('/', methods=['GET'])
def home():
    #if request.method == 'GET':
        _logger.info('health status OK')
        return redirect(url_for('prediction_app.login'))


#Login endpoint
@prediction_app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login form submission
    login_form = LoginForm(request.form)
    
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username).first()

        # Validate user credentials
        if user and check_password_hash(user.password, password):
            flash("Login successful")
            session['user_id'] = user.id
            return redirect(url_for('prediction_app.predict'))
        else:
            flash("Invalid username or password")
            return redirect('/')

    # Render login template with login form
    return render_template('login.html', login_form=login_form)

# Signup endpoint
@prediction_app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Handle signup form submission
    signup_form = SignUpForm(request.form)

    if request.method == 'POST' and signup_form.validate():
        username = signup_form.username.data
        email = signup_form.email.data
        password = signup_form.password.data

        # Hash password for security
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Check if user already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email already exists", 'error')
            return redirect('/')

        # Create new user
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash("User created successfully", 'success')
        return redirect(url_for('prediction_app.predict'))

    # Render signup template with signup form
    return render_template('signup.html', signup_form=signup_form)


'''
handling file inputs
check if file extension is allowed
'''
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Endpoint for handling file upload and prediction
@prediction_app.route('/predict', methods=['GET','POST'])
def predict():
    try:

        # Ensure the user is authenticated
        if 'user_id' not in session:
            flash("Please log in to access this page.")
            return redirect(url_for('prediction_app.login'))

        if request.method == 'POST':
            file = request.files['file']
            model_type = request.form['model']

            
            # Process uploaded file based on its extension and model chosen
            if file.filename != "" and allowed_file(file.filename):
                file_extension = file.filename.rsplit('.', 1)[1].lower()

                # Handle classification model prediction for CSV files
                if file_extension =="csv" and model_type == "classification":
                    df1 = pd.read_csv(file)
                    df1 = df1.iloc[:, 1:].T
                    # Drop the first column(intensity)
                    df1.drop(df1.columns[0], axis=1)
                    index_range = range(1451, len(df1.columns))
                    df1.drop(df1.columns[index_range], axis=1, inplace=True)
                    pred = classification_model(df1)


                    session['pred'] = pred
                    if pred is not None:
                        return render_template('classification_result.html', pred=pred)
                    else:
                    # Handle the case where the regression_model returns None
                        return render_template('error_page.html')
                
                # Handle classification model prediction for XLSX files
                elif file_extension =="xlsx" and model_type=='classification':
                    df2 = pd.read_excel(file)
                    
                    #Extract intensities column and traspose the data
                    df2 = df2.iloc[:, 1:].T
                    # Drop the first column(intensity)
                    df2.drop(df2.columns[0], axis=1)

                    index_range = range(1451, len(df2.columns))
                    df2.drop(df2.columns[index_range], axis=1, inplace=True)
                    pred = classification_model(df2)

                    session['pred'] = pred

                    if pred is not None:
                        return render_template('classification_result.html', pred=pred)
                    else:
                    # Handle the case where the regression_model returns None
                        return render_template('error_page.html')
                    
                
                # Handle regression prediction model for CSV files
                elif file_extension =="csv" and model_type=="regression":
                    df3 = pd.read_csv(file)
                    df3 = df3.iloc[:, 1:].T

                    df3.drop(df3.columns[0], axis=1)
                    index_range = range(1451, len(df3.columns))
                    df3.drop(df3.columns[index_range], axis=1, inplace=True)
                    print(df3.head())

                    pred = regression_model(df3)
                    
                    session['pred'] = pred
                    if pred is not None:
                        return render_template('regression_result.html', pred=pred)
                    else:
                    # Handle the case where the regression_model returns None
                        return render_template('error_page.html')
                
                # Handle regression prediction model for XLSX files
                elif file_extension =="xlsx" and model_type == 'regression':
                    df4 = pd.read_excel(file)
                    
                    #Extract intensities column and traspose the data
                    df4 = df4.iloc[:, 1:].T
                    # Drop the first column(intensity)

                    df4.drop(df4.columns[0], axis=1)

                    index_range = range(1451, len(df4.columns))
                    df4 = df4.drop(df4.columns[index_range], axis=1, inplace=True)
                    pred = regression_model(df4)

                    session['pred'] = pred
                    if pred is not None:
                        return render_template('regression_result.html', pred=pred)
                    else:
                    # Handle the case where the regression_model returns None
                        return render_template('error_page.html')
                     
                else:
                    return redirect(url_for('prediction_app.predict'))
                    
            else:
                return redirect(url_for('prediction_app.predict'))
        return render_template('main.html')
        
    except Exception as e:
        return render_template('error_page.html')


'''
prepare output for download

'''
def generate_csv(data):
    output = io.StringIO()
    csv_writer = csv.writer(output)
    for row in data:
        csv_writer.writerow([row])  # Each string is placed in its own cell
    return output.getvalue()

'''
Endpoint to download results
'''
@prediction_app.route('/download_csv')
def download_csv():
    if 'user_id' not in session:
        return redirect(url_for('prediction_app.login'))
    
    else:
        data = session['pred']
        df = generate_csv(data)
        headers = {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=data.csv',
        }

        # Return a Flask Response object with the CSV data and headers
        return Response(
        df,
        headers=headers,
        status=200,
        mimetype='text/csv')

# Your logout route
@prediction_app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Clear the session data
    session.clear()
    return redirect('/')   
