# Physics-Driven Synthetic Data Generation and Regression Model Evaluation

This project implements a simulation-based approach to generate structured synthetic data using mathematical modelling and evaluates machine learning regression algorithms on the generated dataset.

The workflow demonstrates how modelling, simulation, and machine learning integrate to form a complete analytical pipeline.

---

## Project Objective

The objective of this work is to:

- Design a physics-based simulation system  
- Generate synthetic training data using mathematical equations  
- Train regression models on simulation-generated observations  
- Evaluate predictive performance using statistical metrics  
- Compare linear, nonlinear, and ensemble learning approaches  

This approach is particularly useful when real-world data collection is expensive, time-consuming, or impractical.

---

## System Overview

A projectile motion model is used to generate synthetic observations. The system is governed by deterministic physical equations, while Gaussian noise is introduced to simulate measurement uncertainties.

This produces a dataset similar to sensor-generated readings in real-world environments.

---

## Mathematical Model

Projectile range is calculated using:

R = (v² · sin(2θ)) / g  

Where:

- v = initial velocity  
- θ = launch angle  
- g = gravitational acceleration (9.81 m/s²)  

The nonlinear structure of this equation makes it ideal for testing machine learning algorithms.

---

## Simulation Parameters

| Parameter | Description | Range |
|----------|-------------|------|
| Velocity | Initial speed | 12 – 95 m/s |
| Angle | Launch angle | 15° – 88° |
| Gravity | Constant | 9.81 m/s² |
| Samples | Generated observations | 1000 |

---

## Data Generation Pipeline

1. Define physics model  
2. Randomize input parameters  
3. Compute projectile range  
4. Inject Gaussian noise  
5. Store structured dataset  
6. Export for ML training  

Output dataset file:

`synthetic_projectile_data.csv`

---

## Simulation Analysis

### Angle vs Range Distribution

This visualization confirms nonlinear projectile behaviour.

![Angle vs Range](physics_simulation_visual.png)

---

### Velocity Influence on Range

Higher initial velocity produces significantly larger projectile distance.

![Velocity vs Range](velocity_range_relationship.png)

---

### Angle vs Velocity Density Distribution

Shows interaction between input variables across the dataset.

![Angle Velocity Density](angle_velocity_density.png)

---

## Machine Learning Workflow

1. Load generated dataset  
2. Perform train-test split  
3. Train regression models  
4. Evaluate predictions  
5. Compare performance  

---

## Regression Models Implemented

- Linear Regression  
- Ridge Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- Support Vector Regressor  
- K-Nearest Neighbors Regressor  

---

## Evaluation Metrics

### R² Score
Measures variance explained by the model.

### RMSE
Measures prediction error magnitude.

---

## Model Evaluation Visualizations

### Model Performance Comparison (R²)

![Model R2 Comparison](regression_model_comparison.png)

---

### RMSE Comparison

![RMSE Comparison](rmse_model_comparison.png)

---

### Prediction vs Actual (Best Model)

Illustrates how closely predicted values align with actual simulation outputs.

![Prediction Accuracy](prediction_vs_actual.png)

---

### Residual Error Distribution

Shows error dispersion across predictions.

![Residual Plot](residual_error_distribution.png)

---

### Feature Importance (Tree-Based Models)

Highlights contribution of input variables in prediction.

![Feature Importance](feature_importance_plot.png)

---

## Results and Observations

Key findings from experiments:

- Linear models underperform due to nonlinear relationships  
- Tree-based models adapt better to structured nonlinear data  
- Ensemble methods achieve highest predictive accuracy  
- Random Forest and Gradient Boosting provide stable performance  

The results confirm that simulation-generated nonlinear datasets benefit significantly from ensemble learning approaches.

---

## Project Structure

### Notebooks

- `physics_simulation_pipeline.ipynb`  
  Synthetic data generation using mathematical modelling  

- `regression_training_evaluation.ipynb`  
  Model training, evaluation, and performance comparison  

---

### Generated Data

- `synthetic_projectile_data.csv`  
  Dataset produced from simulation  

- `regression_performance_summary.csv`  
  Evaluation metrics for all regression models  

---

### Visual Outputs

- `physics_simulation_visual.png`  
- `velocity_range_relationship.png`  
- `angle_velocity_density.png`  
- `regression_model_comparison.png`  
- `rmse_model_comparison.png`  
- `prediction_vs_actual.png`  
- `residual_error_distribution.png`  
- `feature_importance_plot.png`  

---

## Technology Stack

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  
- Google Colab  

---

## Conclusion

This project validates the effectiveness of combining modelling, simulation, and machine learning into a single pipeline. Synthetic datasets generated from physics equations provide a controlled environment for evaluating algorithmic performance.

Ensemble models demonstrate strong capability in learning nonlinear relationships, making them well-suited for simulation-driven datasets.

---

## Author

**Name:** Himayat Singh Tiwana  
**Roll No:** 102313049
