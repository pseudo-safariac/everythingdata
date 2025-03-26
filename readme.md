# Table of Contents
- [Introduction to the Project](#introduction-to-the-project)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Data and Methodology](#data-and-methodology)
    - [Data Overview](#data-overview)
    - [Handling Categorical Data](#handling-categorical-data)
    - [Checking Dataset Integrity](#checking-dataset-integrity)
    - [Data Conversion](#data-conversion)
- [Achieving Objectives](#achieving-objectives)
    - [Shopper Demographics](#shopper-demographics)
- [References](#references)

# Introduction to the Project
I chose a project from **Kaggle**, and you can download it from [here](https://www.kaggle.com/datasets/logiccraftbyhimanshi/walmart-customer-purchase-behavior-dataset). This project is created as part of the coursework in [everythingdata][everythingdata-link], where I have to showcase my expertise in data science. The coursework is a joint facilitation between [everythingdata][everythingdata-link] and [DataCamp][datacamp-link].

A big shoutout to both [everythingdata][everythingdata-link] and [DataCamp][datacamp-link] for providing the education and resources.

# Problem Statement
Understanding consumer behavior is essential for businesses to optimize marketing strategies, inventory management, and overall customer satisfaction. This project aims to analyze customer purchasing patterns using a dataset of Walmart transactions to extract insights into demographics, shopping trends, and discount effectiveness.

# Objectives
1. Identify the demographic group that shops the most -> **Shopper demographics**
2. Determine the busiest shopping times and dates -> **Peak shopping times**
3. Analyze whether discounts attract more buyers or if customers shop based on necessity -> **Discount influences**
4. Examine shopping trends in various cities -> **City-based shopping trends**
5. Evaluate if customers consistently rate similar products the same -> **Product ratings**
6. Analyze product preferences by age group and discount impact -> **Product preferences by age**
7. Explore different payment methods preferred by various age groups -> **Payment preferences**

## Data and Methodology

### Data Overview

The dataset consists of **12 columns** and **50,000 rows**. It contains essential customer transaction data:

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50000 entries, 0 to 49999
Data columns (total 12 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Customer_ID       50000 non-null  object
 1   Age               50000 non-null  int64  
 2   Gender            50000 non-null  object
 3   City              50000 non-null  object
 4   Category          50000 non-null  object
 5   Product_Name      50000 non-null  object
 6   Purchase_Date     50000 non-null  object
 7   Purchase_Amount   50000 non-null  float64
 8   Payment_Method    50000 non-null  object
 9   Discount_Applied  50000 non-null  object
10   Rating            50000 non-null  int64  
11   Repeat_Customer   50000 non-null  object
dtypes: float64(1), int64(2), object(9)
memory usage: 4.6+ MB
```

## Data Cleaning and Preprocessing

### Handling Categorical Data
Some categorical columns needed modifications:
- **Customer_ID** was removed as it was not useful for analysis.
- **Purchase_Date** was converted to a proper `datetime` format.
- A unique **id** was assigned as the index.

### Checking Dataset Integrity
- Identified **367 duplicate dates**.
- Conducted **boxplot analysis** for outliers (none found).
- Verified missing values and ensured data consistency.

### Data Conversion
To facilitate modeling and analysis, categorical values were mapped to integers:
```python
category_mapping = {
    "Electronics": 0,
    "Clothing": 1,
    "Beauty": 2,
    "Home": 3
}

gender_mapping = {
    "Female": 0,
    "Male": 1,
    "Other": 2
}

payment_mapping = {
    "Cash on Delivery": 0,
    "Debit Card": 1,
    "Credit Card": 2,
    "UPI": 3
}
```

This transformation aids in numerical analysis and machine learning applications.

### Updated Data Types
```python
<class 'pandas.core.frame.DataFrame'>
Index: 50000 entries, 1 to 50000
Data columns (total 12 columns):
 #   Column            Non-Null Count  Dtype         
---  ------            --------------  -----         
 0   Customer_ID       50000 non-null  object        
 1   Age               50000 non-null  int64         
 2   Gender            50000 non-null  int64         
 3   City              50000 non-null  object        
 4   Category          50000 non-null  int64         
 5   Product_Name      50000 non-null  object        
 6   Purchase_Date     50000 non-null  datetime64[ns]
 7   Purchase_Amount   50000 non-null  float64       
 8   Payment_Method    50000 non-null  int64         
 9   Discount_Applied  50000 non-null  int64         
10   Rating            50000 non-null  int64         
11   Repeat_Customer   50000 non-null  int64         
dtypes: datetime64[ns](1), float64(1), int64(7), object(3)
memory usage: 5.0+ MB
```

> **Exploratory Data Analysis (EDA)** : 
The Exploratory Data Analysis (EDA) has been a countinuous and parallel process that is ongoing simultaneously with the dataset cleaning and pre-processing, ensuring that the data doesn't have missing or wrong data types, enhance data visualizations to communicate findings etc.

## Modeling and Predicative Analysis


# Achieving Objectives
## Shopper Demographics
- Conducted an **exploratory data analysis (EDA)** to visualize and understand shopper demographics.
- Used **pivot tables** to compare purchase behavior across different groups.

I used pivot_tables to show relationships between different data columns starting with `Age` and its association with other factors such as `Gender`.

This showed that people of all genders were spending equal amounts of money on shopping and also that they were of the same spread as shown by the pie chart.



# References
1. [EverythingData][everythingdata-link]
2. [DataCamp][datacamp-link]  

[everythingdata-link]: [https://www/example.com] "Link is Missing"
[datacamp-link]: https://www.datacamp.com/ "Landing page of DataCamp"

