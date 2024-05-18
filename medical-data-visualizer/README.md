# Medical Data Visualizer

This is the boilerplate for the Medical Data Visualizer project. 

This project visualizes and calculates insights from a dataset of medical examination data. The dataset includes various patient information such as body measurements, blood test results, and lifestyle choices. The goal is to explore the relationship between cardiac disease and these variables.

## Dataset Description
The dataset contains the following features:

* Age: Age of the patient in days (int)
* Height: Height of the patient in cm (int)
* Weight: Weight of the patient in kg (float)
* Gender: Gender of the patient (categorical code)
* Systolic Blood Pressure (ap_hi): Systolic blood pressure (int)
* Diastolic Blood Pressure (ap_lo): Diastolic blood pressure (int)
* Cholesterol: Cholesterol levels (1: normal, 2: above normal, 3: well above normal)
* Glucose: Glucose levels (1: normal, 2: above normal, 3: well above normal)
* Smoking (smoke): Smoking status (binary)
* Alcohol Intake (alco): Alcohol intake status (binary)
* Physical Activity (active): Physical activity status (binary)
* Cardiovascular Disease (cardio): Presence or absence of cardiovascular disease (binary)

## Project Tasks
### 1. Import Data
The data is imported from medical_examination.csv and assigned to the df variable.

### 2. Add Overweight Column
An overweight column is added to the dataset. The Body Mass Index (BMI) is calculated using the formula:
BMI = weight (kg)/(height (m))2​
 
If the BMI is greater than 25, the person is considered overweight (value 1), otherwise not overweight (value 0).

### 3. Normalize Data
The data is normalized by making 0 always good and 1 always bad:

* Cholesterol and glucose values of 1 are set to 0 (normal).
* Cholesterol and glucose values greater than 1 are set to 1 (above normal).

### 4. Draw Categorical Plot
A categorical plot is drawn to show the counts of good and bad outcomes for the cholesterol, glucose, alcohol intake, physical activity, and smoking variables for patients with and without cardiovascular disease.

Steps:

* Convert the data into long format using pd.melt.
* Group and reformat the data to split it by the cardio variable.
* Create a seaborn catplot to show the value counts of the categorical features, split by the cardio value.

### 5. Clean Data
The data is cleaned by filtering out the following patient segments:

* Diastolic pressure is higher than systolic pressure.
* Height is less than the 2.5th percentile or more than the 97.5th percentile.
* Weight is less than the 2.5th percentile or more than the 97.5th percentile.

### 6. Draw Heat Map
A heat map is drawn to show the correlation matrix of the dataset. The upper triangle of the correlation matrix is masked.

Steps:

* Calculate the correlation matrix.
* Generate a mask for the upper triangle.
* Set up the matplotlib figure.
* Plot the correlation matrix using seaborn's heatmap.

## File Structure
medical_data_visualizer.py: Contains the code for data manipulation and visualization.
test_module.py: Contains unit tests for the project.
medical_examination.csv: The dataset file.

## Usage
Ensure all necessary libraries are installed: pandas, matplotlib, seaborn.
Run medical_data_visualizer.py to generate the plots and perform data analysis.
Use test_module.py to run the unit tests and verify the correctness of the code.

## Conclusion
This project provides visual insights into the relationship between cardiac disease and various medical and lifestyle factors. The categorical plot and heat map help in understanding the distribution and correlation of these factors with cardiovascular disease.

replit link to run the project: https://replit.com/@rahulramakrish2/boilerplate-medical-data-visualizer-2#medical_data_visualizer.py
