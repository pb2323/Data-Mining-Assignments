# Auto AI Airline Passenger Satisfaction Predictor

This project uses Auto AI to predict airline passenger satisfaction based on a dataset from Kaggle. The model was trained and deployed using Akkio, achieving a high accuracy rate.

## Demo

A video demonstration of the project is available on YouTube:

[Watch Demo Video](https://www.youtube.com/watch?v=hRRFqHXi9-g)

## Project Overview

- **Dataset**: Airline Passenger Satisfaction from Kaggle
- **AI Platform**: Akkio
- **Model Accuracy**: 93%
- **Deployment**: Successfully deployed and tested

## Dataset

### Overview

This repository contains an analysis of airline passenger satisfaction based on a dataset that includes various factors affecting customer experiences. The goal is to understand the key drivers of passenger satisfaction and to develop predictive models to assess customer satisfaction.

### Dataset Characteristics

The dataset consists of 103,594 rows and 24 columns with the following characteristics:

### Columns Description

id: Unique identifier for each passenger (integer).

Gender: Gender of the passenger (categorical: Male, Female).

Customer Type: Type of customer (categorical: Loyal Customer, Disloyal Customer).

Age: Age of the passenger (integer).

Type of Travel: Purpose of travel (categorical: Business travel, Personal Travel).

Class: Travel class (categorical: Business, Eco, Eco Plus).

Flight Distance: Distance of the flight (integer).

Inflight wifi service: Rating of inflight wifi service (integer).

Departure/Arrival time convenient: Rating of the convenience of departure/arrival time (integer).

Ease of Online booking: Rating of the ease of online booking (integer).

Gate location: Rating of the convenience of the gate location (integer).

Food and drink: Rating of food and drink quality (integer).

Online boarding: Rating of the online boarding process (integer).

Seat comfort: Rating of seat comfort (integer).

Inflight entertainment: Rating of inflight entertainment (integer).

On-board service: Rating of on-board service (integer).

Leg room service: Rating of legroom service (integer).

Baggage handling: Rating of baggage handling (integer).

Checkin service: Rating of check-in service (integer).

Inflight service: Rating of inflight service (integer).

Cleanliness: Rating of cleanliness (integer).

Departure Delay in Minutes: Minutes of departure delay (integer).

Arrival Delay in Minutes: Minutes of arrival delay (integer).

satisfaction: Overall customer satisfaction (categorical: neutral or dissatisfied, satisfied).


[View Dataset on Kaggle](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)

## Model Training and Testing

- The dataset was uploaded to Akkio for automatic AI model creation.
- 80% of the data was used for training the model.
- The remaining 20% was used for testing, resulting in a 93% accuracy rate.

## Deployment

The model has been successfully deployed and is available for testing:

[Access Deployed Model](https://app.akkio.com/deployments/5ed31860-3a83-430f-818c-c6ecfe2f7a82)

## Data Exploration

Using AI, we explored the dataset by asking questions such as:
- Average customer satisfaction
- Relationship between customer age and satisfaction

## How to Use

1. Visit the deployed model link above.
2. Input the required passenger information.
3. Get the predicted satisfaction level for the passenger.

## Future Work

- Incorporate more recent data to improve model relevance.
- Explore feature importance to understand key factors affecting passenger satisfaction.
- Develop a user-friendly interface for easier interaction with the model.

