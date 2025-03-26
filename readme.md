# Introduction to the Project
I chose a project from **Kaggle** and you can download it from [here](https://www.kaggle.com/datasets/logiccraftbyhimanshi/walmart-customer-purchase-behavior-dataset). This project is created as part of the coursework in [everythingdata][everythingdata-link] where I have to showcase my expertise in the data science course that I have been talking, which was a joint facilitation between [everythingdata][everythingdata-link] and [DataCamp][datacamp-link].

A big shoutout to both [everythingdata][everythingdata-link] and [DataCamp][datacamp-link] for helping me get the education and classes.

## Objectives on the project
1. Use the data to find what demographic shops the most products -> Shopper demographics
2. Find what is the businest time and dates to shop -> Peak shopping times
3. Find out if most shoppers just go for the discounts or are frequest shoppers who simply need a product and got the discount as a bonus -> Discount influences
4. Relate what cities have shoppers with the most similar items purchased -> Shopping trends in cities
5. Find out if shoppers of similar products give a consistent Rating to indicate product quality -> Product ratings
6. Group products purchased by age and show what age group loves to shop similar items and if they prefer to get discounts -> Product prefences by age group
7. Check the different modes of payment by age groups -> Payment preferences

## Project Exploration Details

I chose to include the CSV dataset since I needed the project to be as air-gapped as possible and not require an internet connection after a `git pull`.

I first started with data exploration, as seen in the jupyter notebook. This is also the very first time I am using notebooks so please bear with me.

The dataset contains 12 columns and had 5,000 rows, and they were all found to have the expected dataset.

The original columns in the datasaet were:
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
 10  Rating            50000 non-null  int64  
 11  Repeat_Customer   50000 non-null  object 
dtypes: float64(1), int64(2), object(9)
memory usage: 4.6+ MB
```

I started with numerical columns `['Age', 'Rating', 'Purchase_Amount']`:

The results showed that the columns were complete and with no missing.

#### Categorical Data

The other types of data *(categorical data)* gave info that indicated that I should create my own id system since the one they used was not helpful for my case, and I tested the `Purchase_Date` column and found that I needed to convert it into valid a `datetime` object that I can then use.

> Note that I also did a `df = df.copy()` so that the edits I make can be reflected on the df var I have been pointing at in memory

#### Checking Dataset

For simplicity of use, I briefly created an id column and set it as index, I found 367 days that were duplicated, I checked using boxplots for outliers and I saw none.

#### Converting Columns to integers

I also converted `['Gender', 'Category', 'Product_Date', 'Payment_Method', 'Discount_Applied', 'Repeat_Customer']` to `int` so that I can use the values to gain more information about the dataset and also inporporate machine learning later on.

Sample Data that was converted into `int` includes:
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
This is going to be useful as a reference later on and it is easier written on the notes.

All these changes made my new df to have the following types:
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
 10  Rating            50000 non-null  int64         
 11  Repeat_Customer   50000 non-null  int64         
dtypes: datetime64[ns](1), float64(1), int64(7), object(3)
memory usage: 5.0+ MB
```
### Achieving Objectives
#### Shopper Demograpghics

I now started achieving my objectives by starting by finding the relationships in shopper demographics.


## References

1. [EverythingData][everythingdata-link]
2. [DataCamp][datacamp-link]  


[everythingdata-link]: [https://www/example.com] "Link is Missing"
[datacamp-link]: https://www.datacamp.com/ "Landing page of DataCamp"
