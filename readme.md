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

I started with numerical columns `['Age', 'Rating', 'Purchase_Amount']`:
```python
df.describe()
df.isna().sum()
df.isna().any()
```

The results showed that the columns were complete and with no missing.

The other types of data *(categorical data)* gave info that indicated that I should create my own id system since the one they used was not helpful for my case, and I tested the `Purchase_Date` column and found that I needed to convert it into valid a `datetime` object that I can then use.

I found that I had 367 days that were duplicated, 

I also converted `['Gender', 'Category', 'Product_Date', 'Payment_Method', 'Discount_Applied', 'Repeat_Customer']` to `int` so that I can use the values to gain more information about the dataset and also inporporate machine learning later on.

After this, I discovered that xxxxxxxxx.


## References

1. [EverythingData][everythingdata-link]
2. [DataCamp][datacamp-link]  


[everythingdata-link]: [https://www/example.com] "Link is Missing"
[datacamp-link]: https://www.datacamp.com/ "Landing page of DataCamp"
