# Synthetic Data Generation using Modelling and Simulation for Machine Learning

This repository presents a complete workflow for generating synthetic data using mathematical modelling and simulation, and subsequently applying machine learning models to learn patterns from the simulated data.

The project demonstrates how simulation can be used as a reliable alternative data source when real-world datasets are unavailable, costly, or difficult to collect. A physics-based system is modelled to produce structured observations, which are then used to train and evaluate regression algorithms.

---

## Project Objective

The primary objectives of this assignment are:

- To develop a simulation-based data generation pipeline  
- To model a physical system using mathematical equations  
- To generate a structured dataset from the simulation  
- To train multiple machine learning models on the generated dataset  
- To compare models using standard evaluation metrics  
- To identify the most suitable model for nonlinear prediction tasks  

This work illustrates how modelling and simulation integrate with machine learning workflows in real-world analytical systems.

---

## Simulation Overview

A projectile motion system is selected as the simulation environment. Projectile motion is governed by deterministic physical equations, making it suitable for generating meaningful numerical data.

The simulation randomly varies input parameters such as launch velocity and angle, and computes the resulting projectile range. To replicate real-world measurement uncertainty, Gaussian noise is introduced into the output values.

This process produces a dataset that mimics sensor-generated observations from a physical system.

---

## Mathematical Foundation

The simulation is based on classical kinematic equations of projectile motion.

Range equation:

R = (v² · sin(2θ)) / g  

Where:

- **R** = horizontal range of the projectile  
- **v** = initial launch velocity  
- **θ** = launch angle  
- **g** = acceleration due to gravity (9.81 m/s²)

The presence of trigonometric and quadratic relationships introduces nonlinear behaviour into the dataset, making it suitable for evaluating machine learning models.

---

## Simulation Parameters

The following parameters were randomized within predefined bounds to generate the dataset:

| Parameter | Description | Lower Bound | Upper Bound |
|----------|-------------|-------------|-------------|
| Velocity (v) | Initial launch speed | 12 m/s | 95 m/s |
| Angle (θ) | Launch angle | 15° | 88° |
| Gravity (g) | Acceleration due to gravity | Fixed | 9.81 m/s² |

Total number of simulations executed: **1000**

---

## Dataset Generation Process

The dataset generation pipeline follows these steps:

1. Define the physics-based projectile model  
2. Randomly generate input parameters within valid ranges  
3. Compute projectile range using mathematical equations  
4. Inject Gaussian noise into outputs to simulate sensor errors  
5. Store generated values in structured tabular format  
6. Export dataset as CSV for machine learning tasks  

The final dataset contains:

- Velocity  
- Launch angle  
- Measured projectile range  

---

## Simulation Visualization

The generated dataset is visualized to verify the physical consistency of the simulation.

The scatter distribution of launch angle versus range forms a nonlinear pattern consistent with projectile motion theory. Higher velocities correspond to larger ranges, while mid-angle launches produce maximum distance.

This confirms that the simulated data correctly reflects real-world physical behaviour.

---

## Machine Learning Workflow

After generating the dataset, machine learning models are trained to learn the relationship between input parameters and projectile range.

Workflow steps:

1. Load generated dataset  
2. Split data into training and testing sets (80/20)  
3. Train regression models on training data  
4. Evaluate performance on testing data  
5. Compare models using evaluation metrics  
6. Identify best-performing model  

---

## Machine Learning Models Implemented

The following regression models were trained and evaluated:

- Linear Regression  
- Ridge Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- Support Vector Regressor (SVR)  
- K-Nearest Neighbors Regressor (KNN)  

These models were selected to compare linear, nonlinear, and ensemble learning approaches.

---

## Evaluation Metrics

Model performance was assessed using the following metrics:

### R² Score
Measures how well the model explains variance in the target variable.  
Higher values indicate better predictive performance.

### Root Mean Squared Error (RMSE)
Measures the magnitude of prediction error.  
Lower values indicate more accurate predictions.

---

## Results and Analysis

The experimental results indicate that nonlinear and ensemble models outperform linear regression techniques.

Key observations:

- Linear models struggle to capture trigonometric and quadratic relationships  
- Tree-based models adapt well to nonlinear patterns  
- Ensemble methods produce the most accurate predictions  
- Random Forest and Gradient Boosting demonstrate superior generalization  

These outcomes align with expectations since projectile motion contains nonlinear dependencies between variables.

---

## Project Structure

### Source Files
- `data_generation.ipynb` – Physics-based simulation and dataset creation  
- `ML_model.ipynb` – Model training, evaluation, and comparison  

### Generated Files
- `simulation_dataset.csv` – Synthetic dataset from simulation  
- `model_metrics.csv` – Performance comparison of machine learning models  

### Visual Outputs (Generated in Notebook)
- Simulation scatter plot  
- Model comparison bar chart  

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

This project demonstrates the effectiveness of simulation-driven data generation for machine learning applications. By modelling a physical system and generating controlled data, it becomes possible to evaluate algorithms in a structured environment.

The results confirm that ensemble-based machine learning models are highly effective in learning nonlinear relationships derived from physics-based simulations.

The integration of modelling, simulation, and machine learning forms a powerful workflow applicable to engineering systems, robotics, physics simulations, and predictive analytics.

---

## Author

**Name:** Himayat Singh Tiwana  
**Roll No:** 102313049
