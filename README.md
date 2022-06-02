# House Price Prediction
Not only investing in properties is a relatively safe place to put money into if you have enough cash flow, buying one is usually a better choice for a family who want to settle down. Even though the price of the houses is constantly changing and fluctuating, in most of the countries, it not only rises in the long run, but the demand seems to be escalated [1]. For example, in US, New York, the price increases approximately 100 percent during 10-year period [1]. However, in order to understand what affects the price of the real estates is difficult and complicated. Some might think that only the neighborhood, living area or year built would be enough to determine the appropriate value of the house but there are many factors that are needed to consider. Here we show that which data from the elements of the houses can specify the property’s price. My approach uses the data of household to find correlation heatmap and calculate feature importance and then analyze which factors that are related with the prices and predict them. From the analysis I found that the features that have high effect to the price is the quality of material that are used to build the houses, capacity of car in garage and the living area. Although the result for quality of material and living area are expectable but the car capacity gives me a more perspective of what to be accounted for the houses price.

## Data Description
The prices of the residential homes described by 79 variables (numerical data, categorical data with order, and categorical data without order) is collected in Ames, Iowa. The dataset has 1460 rows. Our target is to accomplish house pricing prediction.

The data is from https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview

| Numerical data  | Categorical data with order | Categorical data without order |
| ------------- | ------------- |  ------------- |
| - MSSubClass |
| - LotArea
| - OverallQual
| - OverallCond
| - YearBuilt
| - YearRemodAdd
| - MasVnrArea
| - BsmtFinSF1
| - BsmtFinSF2
| - BsmtUnfSF
| - TotalBsmtSF
| - 1stFlrSF
| - 2ndFlrSF
| - LowQualFinSF
| - GrLivArea
| - BsmtFullBath
| - BsmtHalfBath
| - FullBath
| - HalfBath
| - BedroomAbvGr
| - KitchenAbvGr
| - TotRmsAbvGrd
| - Fireplaces
| - GarageYrBlt
| - GarageCars
| - GarageArea
| - WoodDeckSF
| - OpenPorchSF
| - EnclosedPorch
| - 3SsnPorch
| - ScreenPorch
| - PoolArea
| - MiscVal
| - MoSold
| - YrSold  | Content Cell  | Content Cell  |
