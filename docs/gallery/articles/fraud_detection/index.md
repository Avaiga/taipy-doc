---
title: Fraud Detection
category: finance
data-keywords: dashboard vizelement layout chart ai multi-page classification enterprise
short-description: A Taipy Application that analyzes credit card transactions to detect fraud.
order: 20
img: fraud_detection/images/transactions_page.png
hide:
    - toc
---

A Taipy Application to analyze credit card transactions, detect fraud, and collaborate with other
application users.

!!! note "Taipy Enterprise edition"

    Taipy provides robust, business-focused applications tailored for enterprise environments. To
    maintain standards of security and customization, these applications are proprietary like this
    application. If you're looking for solutions that are immediately deployable and customizable to
    your business needs, we invite you to try them out and contact us for more detailed information.

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }


# Understanding the Application

This application displays a list of credit card transactions. A model estimates whether a
transaction is fraudulent; this task can be automatically handled by a pipeline. However,
some transactions may require further human review.

![Transactions](images/transactions_page.png){width=90% : .tp-image-border }

Within this page, you can access various analyses and data visualizations:

- List of transactions
- Client information
- Fraud details

This demo includes user management and collaboration features. You need to select one of the
available users to access the application.

![Users](images/login_page.png){width=90% : .tp-image-border }

After logging in, you can navigate to your user page to view the transactions assigned to you
for investigation. You can see both your past transactions and those requiring your attention.
Clicking on a transaction in the table will select it and navigate you to the Analysis page.

This page also includes a newsfeed showing the application or other users' activities.

![User Page](images/user_page.png){width=90% : .tp-image-border }

The Analysis page presents several pieces of information. The left section explains the model's
results (providing explanations on the model output), the middle section displays details about
the transaction, and the right section shows information about the client. Here, you can verify
the client's identity using a deep learning model.

You can decide whether the transaction is fraudulent or not. If you are unsure, you can share the
transaction with someone else for further review.

![Analysis](images/analysis_page.png){width=90% : .tp-image-border }

For educational purposes, you can adjust the model's threshold— the output value above which a
transaction is considered fraudulent. You can select the threshold by examining the displayed
confusion matrix and reviewing false positive and false negative transactions.

![Threshold Selection Page](images/threshold_page.png){width=90% : .tp-image-border }
