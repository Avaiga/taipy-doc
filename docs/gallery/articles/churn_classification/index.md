---
title: Churn Classification
category: decision_support
data-keywords: ai classification scenario enterprise
short-description: Leverage Scenario management and comparison to improve decision making on a Churn prediction demo.
order: 18
img: churn_classification/images/churn-classification-data-Visualization-histogram.png
---
In the fast-paced world of business, retaining customers
is a top priority because keeping current customers is often
more cost-effective than acquiring new ones. By identifying
customers who may leave early and applying retention strategies,
businesses can lower churn rates and boost customer loyalty.

!!! note "Taipy Enterprise edition"

    Taipy provides robust, business-focused applications tailored for enterprise environments. To
    maintain standards of security and customization, these applications are proprietary like this
    application. If you’re looking for solutions that are immediately deployable and customizable
    to your business needs, we invite you to try them out and contact us for more detailed
    information.

    [Try it live](https://churn-classification.taipy.cloud/Data-Visualization){: .tp-btn target='blank' }
    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

# Understanding the Application

The application comprises four pages accessible via the left panel.

## Page 1: Data Visualization

This page allows to conduct an Exploratory Data Analysis (EDA).
You have the option to select among two types of graph (scatter plot or histogram)
and choose the data content you want to explore with the "Select x" selector.

![Data Visualization](images/churn-classification-data-visualization-scatter.png){width=90% : .tp-image-border }

![Histogram](images/churn-classification-data-Visualization-histogram.png){width=90% : .tp-image-border }

## Page 2: Model Manager

Here, users can access the performance results of the selected algorithm. Users can choose:
- Classification algorithm amongst 2 options (a ‘baseline or ‘ML’)
- A chart type to visualize predictions on a validation dataset.

![Model Manager](images/churn-classification-model-manager.png){width=90% : .tp-image-border }

## Page 3: Model Comparison

This page displays the performance of two models side by side, facilitating easy comparison.

![Model Comparison](images/churn-classification-model-comparison.png){width=90% : .tp-image-border }

## Page 4: Databases

Through this page, access to various datasets, including: training dataset,
test dataset, forecast, scoring results, and the Confusion Matrix of the
selected algorithm. Users can also download specified data frames as CSV files.


![Databases](images/churn-classification-databases.png){width=90% : .tp-image-border }
