# Topsis-Himayat-102313049

## TOPSIS Implementation --- Command Line Tool, PyPI Package, and Web Service

**Assignment 3 --- Predictive Analytics**\
**Name:** Himayat\
**Roll No:** 102313049

------------------------------------------------------------------------

## Project Overview

This project implements the **TOPSIS (Technique for Order Preference by
Similarity to Ideal Solution)** decision-making method in three stages:

1.  A **Command Line Interface (CLI) TOPSIS tool**
2.  A **PyPI-published Python package**
3.  A **Web-based TOPSIS service** that emails results to users

The system accepts a dataset, weights, and impacts, computes TOPSIS
scores, ranks alternatives, and outputs results.

------------------------------------------------------------------------

## Part 1 --- Command Line TOPSIS Tool

A Python CLI program that computes TOPSIS rankings.

### Usage

``` bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example

``` bash
python topsis.py data.csv "1,1,1,2" "+,+,-,+" output.csv
```

### Features Implemented

-   Validates number of input parameters
-   Handles file not found errors
-   Ensures minimum three columns in input file
-   Ensures numeric values in criteria columns
-   Ensures weights and impacts match criteria count
-   Ensures impacts are only `+` or `-`
-   Computes TOPSIS scores and ranks
-   Saves output as CSV

------------------------------------------------------------------------

## Part 2 --- PyPI Package

The CLI tool was packaged and published as a Python package.

### Package Name

    Topsis-Himayat-102313049

### Installation

``` bash
pip install Topsis-Himayat-102313049
```

### Run After Installation

``` bash
topsis data.csv "1,1,1,2" "+,+,-,+" output.csv
```

### Packaging Features

-   Structured Python package
-   Entry-point CLI command (`topsis`)
-   Versioned releases
-   Upload via Twine
-   GitHub integration

------------------------------------------------------------------------

## Part 3 --- Web Service for TOPSIS

A Flask-based web application that allows users to:

-   Upload dataset files
-   Enter weights and impacts
-   Enter sender and receiver email credentials
-   Compute TOPSIS rankings
-   Automatically email results to users

### Web App Features

-   File upload interface
-   Input validation
-   Email-based result delivery
-   Secure handling of credentials (not stored)
-   Real-time TOPSIS execution

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Flask
-   SMTP (Email Delivery)
-   GitHub
-   PyPI

------------------------------------------------------------------------

## How to Run Web App

``` bash
pip install flask pandas numpy
python app.py
```

Open in browser:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## Output

The final output includes: - Original dataset - TOPSIS score for each
alternative - Ranking based on closeness to ideal solution

------------------------------------------------------------------------

## Summary

This project demonstrates: - Decision-making analytics using TOPSIS -
CLI-based automation - Package distribution using PyPI - Web-based
analytical services - Secure handling of user credentials

------------------------------------------------------------------------

## Author

**Himayat**\
**Roll No:** 102313049\
**Course:** Predictive Analytics
