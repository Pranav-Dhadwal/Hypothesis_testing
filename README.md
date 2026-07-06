# DecisionLens – A/B Testing & Business Decision Platform

## Business Problem

An e-commerce company has introduced a **new recommendation engine** to improve the customer shopping experience.

Before deploying it to all users, the company wants to answer an important business question:

> **Does the new recommendation engine genuinely increase customer purchases, or is the observed improvement simply due to random chance?**

As a Data Scientist, your responsibility is to analyze the experiment, validate the results using statistical methods, and recommend whether the company should roll out the new recommendation engine.

---

## Dataset Overview

This project uses a **synthetically generated dataset** that simulates real-world customer behavior on an e-commerce platform.

Each row represents **one customer session**, containing information about:

* Customer profile
* Browsing behavior
* Experiment group assignment
* Purchase outcome

The synthetic data is generated using realistic business assumptions to closely resemble production data while allowing complete control over the experiment.

---

## Dataset Features

### Customer Information

| Column    | Description                                            |
| --------- | ------------------------------------------------------ |
| `user_id` | Unique identifier for each customer                    |
| `age`     | Customer's age                                         |
| `gender`  | Customer's gender                                      |
| `country` | Customer's country                                     |
| `device`  | Device used during the session (Mobile/Desktop/Tablet) |

### Browsing Behaviour

| Column             | Description                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `session_duration` | Total time spent on the website (minutes)                                                 |
| `pages_viewed`     | Number of pages visited                                                                   |
| `products_viewed`  | Number of products viewed                                                                 |
| `previous_orders`  | Number of previous purchases made by the customer                                         |
| `traffic_source`   | Source through which the customer visited the website (Organic, Ads, Email, Social Media) |

### Experiment Information

| Column  | Description                                                               |
| ------- | ------------------------------------------------------------------------- |
| `group` | **A** = Existing recommendation engine, **B** = New recommendation engine |

This column represents the A/B experiment and forms the foundation of the statistical analysis.

### Purchase Information

| Column        | Description                                                      |
| ------------- | ---------------------------------------------------------------- |
| `purchased`   | Purchase outcome (1 = Purchased, 0 = Did Not Purchase)           |
| `order_value` | Amount spent by the customer. Returns 0 if no purchase was made. |

---

## Project Objective

Using this dataset, the project aims to:

* Perform Exploratory Data Analysis (EDA).
* Compare the performance of Recommendation Engine A and B.
* Apply hypothesis testing to determine whether the observed improvement is statistically significant.
* Interpret p-values and confidence levels.
* Provide a business recommendation on whether the new recommendation engine should be deployed.

---

## Expected Outcome

Rather than simply comparing averages, this project focuses on making **data-driven business decisions under uncertainty** by combining descriptive analytics, inferential statistics, and business reasoning.
