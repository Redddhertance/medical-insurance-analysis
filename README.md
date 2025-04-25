# medical-insurance-analysis
Explores medical insurance data from a CSV file and gets exploratory statistics

US Medical Insurance Costs Analysis

Project Overview:
This project analyses a dataset of US medical insurance costs. The dataset contains information about 1,339 patients, including their age, sex, BMI, number of children, smoking status, region, and insurance charges. 

The goal is to investigate how demographic and behavioural factors relate to insurance charges.

Dataset:
Source: insurance.csv
Features:
age: Age of primary beneficiary
sex: Gender of beneficiary
bmi: Body Mass Index
children: Number of children covered by health insurance
smoker: Whether the individual smokes
region: Residential area in the US
charges: Annual medical insurance charges

Project Structure:
Load and clean data from CSV into Python lists.
Create reusable functions to calculate averages and compare groups.
Analyse relationships between:
smoker status and insurance charges
Gender and insurance charges
Parenting status and average age
Regional differences in insurance charges
Identify the most and least expensive regions for insurance.

Key Results:
Smokers pay significantly higher insurance charges than non-smokers.
Male and female beneficiaries have slight differences in average insurance charges.
Parents tend to be slightly older than non-parents.
Insurance costs vary by region, with certain areas being significantly more expensive.

Future Improvements:
  Add data visualisations using matplotlib or seaborn.
  Explore correlations between features (e.g., BMI vs. charges).
  Develop a Jupyter Notebook version for improved readability.
  Implement simple statistical modelling (linear regression).
