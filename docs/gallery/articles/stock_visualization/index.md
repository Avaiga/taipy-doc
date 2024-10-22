---
title: Stock Visualization
category: finance
data-keywords: ai dashboard community
short-description: Leverage Taipy and Prophet to visualize historical stock data and make predictions over 5 years.
order: 2
img: stock_visualization/images/stock-visualization.png
hide:
    - toc
---

In the realm of financial markets, data is king. The ability to quickly and easily visualize
historical stock data and making predictions is essential  for investors and financial analysts.
This demo, built with Taipy and powered by the
[Prophet library](https://facebook.github.io/prophet/docs/quick_start.html),
offers a way to achieve this.

[Try it live](https://stock-visualization.taipy.cloud/){: .tp-btn target='blank' }
[Get it on GitHub](https://github.com/Avaiga/demo-stock-visualization){: .tp-btn .tp-btn--accent target='blank' }

# Understanding the Application

This one-page demo's primary objective is to illustrate how
you can build a forecast data visualization dashboard effortlessly using Taipy.
This fully interactive web application can be created with fewer than 120 lines of Python code.


![Stock Visualization](images/stock-visualization.png){width=90% : .tp-image-border }

Forecasting stock trends is a vital part of financial analysis. In this demo,
Meta's Prophet library offers stock predictions for 1 to 5 years.
This predictive feature empowers users to make informed choices with the assistance of Taipy.


## How to use the Application

1. Select the ticker you wish to predict
2. Open the Historical Data Panel
3. Select the period of prediction (from 1 to 5)
4. Click on the ‘PREDICT" button
5. See your predictions in the Forecast Data Panel...
6. Try it repeatedly using different tickers to compare the results.
7. Optional: You'll get the prediction ranges as a table by clicking on the "More info" button at the bottom.
