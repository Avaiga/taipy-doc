# Sharing a Taipy Application on Colab with Ngrok

This article will show you how to put a Taipy Application on Colab, which is a Google Notebook 
platform. You'll also learn how to make it accessible through a public URL created with Ngrok.

![Monthly Production Planning](Sharing_Taipy_Ngrok_1.png){width=80%}

## Problem statement

For people who want to create strong graphical interfaces without needing to be an expert in GUI 
(Graphical User Interface), Taipy is definitely the solution.

In addition to coding with Python scripts, Taipy works seamlessly in 
[Notebook environments](https://www.taipy.io/tips/taipy-gui/taipy-in-jupyter-notebooks/).
You can use Notebooks on your computer and on platforms like:

- [Google Colab](https://colab.google/)
- [Kaggle](https://www.kaggle.com/)
- [Databricks](https://www.databricks.com/)
- [Amazon SageMaker](https://aws.amazon.com/fr/sagemaker/)
- [IBM Watson Studio](https://www.ibm.com/products/watson-studio)

In this article, we will demonstrate how to put a Taipy application on Notebooks that are hosted 
on the Google Colab platform. We will achieve this by creating a public URL using 
[Ngrok](https://ngrok.com/).

![Problem statement](Sharing_Taipy_Ngrok_1.png){width=80%}

To begin, let's briefly explain what Ngrok and Google Colab are.

## What is Google Colab?

[Google Colab](https://colab.google/) is a preferred tool for Data Scientists. It offers an 
advanced Notebook environment that provides access to powerful hardware, 
including CPUs and GPUs, essential for tasks like deep learning, without the need to buy 
physical machines.

However, Google Colab is cloud-based, so you can't directly see the graphical user interface 
(GUI) of your web application. But don't worry, we'll show you how Ngrok can help solve this issue.

## What is Ngrok?

Ngrok enables you to share your application directly on the internet. It sets up a connection 
from your computer to the outside world through a public URL.

Please note that the URL is temporary when using the free version of Ngrok, but you can make it 
permanent by opting for a paid solution.

## Setting up your Taipy application on Google Colab

Now, let's begin:

For our example, we will use a Sentiment Analysis Application from 
[Taipy's Getting Started](https://github.com/Avaiga/demo-sentiment-analysis) guide. This 
application showcases multiple pages with a feature-rich graphical user interface.

## Step 1: Getting Started with Taipy and Google Colab

Copy the Taipy Sentiment Analysis code into a Google Colab Notebook. This code creates a 
sentiment analysis web application using Taipy.

You can locate the complete code in this GitHub repository.

When you run the Taipy code (please note the instruction: `Gui.run(...)` which initiates a web 
server), it will start a web application with a local URL. However, keep in mind that 
this URL is only accessible locally and cannot be accessed from the internet. As mentioned 
earlier, Google Colab is hosted on a server, not on your local machine.

## Step 2: Getting your Authtoken on Ngrok

On the Ngrok website (create a hyperlink to Ngrok website), create a free account.

![Getting your Authtoken on Ngrok](Sharing_Taipy_Ngrok_2.png){width=50%}

After you've created your account, you can obtain your personal AuthToken. We require this 
AuthToken to establish the tunnel for our Taipy application.

![Getting your Authtoken on Ngrok](Sharing_Taipy_Ngrok_3.png){width=60%}

Head to Ngrok website and obtain your tunnel Authtoken.

## Sharing our Taipy application in Google Colab with Ngrok

The initial step involves importing Ngrok. To do this, let's install the Ngrok Python wrapper 
called **pyngrok**.

- `pip install pyngrok`

The next step takes place in the Gui.run() call. Taipy has an in-built Ngrok Authtoken reader. 
We just have to add the `ngrok_token` parameter in the `run()` function and put the Authtoken 
provided by Ngrok.

![Sharing our Taipy application in Google Colab with Ngrok](Sharing_Taipy_Ngrok_4.png){width=100%}

Executing this last step will generate a public URL from Ngrok in the terminal.

![Sharing our Taipy application in Google Colab with Ngrok](Sharing_Taipy_Ngrok_5.png){width=70%}
![Sharing our Taipy application in Google Colab with Ngrok](Sharing_Taipy_Ngrok_5_1.png){width=70%}

Now, please click on the Ngrok Public URL link to access our application.

![Sharing our Taipy application in Google Colab with Ngrok](taipy_ngrok_app.gif){width=100%}

Congratulations! You have successfully created and launched our multi-page Taipy application 
from Colab!!

On the first page, you can enter a word or sentence and see its scores determined by an NLP 
algorithm. The results are displayed in a table and a graph. On the second page, you can upload 
a file and see the analysis of an entire text.

To learn more, visit our 
[Getting Started](https://docs.taipy.io/en/develop/getting_started/) page. You can also share 
this application with anyone on the internet.

## Update the delay parameter

Our application, accessed through Ngrok, is updated at intervals determined by a delay parameter.
When we input a word or sentence, you may notice that it's not always registered correctly 
because the page refreshes several times. This happens because of the time it takes for data to 
travel over the internet, causing delays.

To address this issue, you can modify the `change_delay` parameter in one of the following ways:

- **Locally**: You can make changes to this parameter locally, directly within the Taipy visual 
  element.
  ![Update the delay parameter](Sharing_Taipy_Ngrok_6.png){width=100%}

- **Globally**: To adjust the delay for all of Taipy's visual elements.
  ![Update the delay parameter](Sharing_Taipy_Ngrok_7.png){width=100%}

## Reloading after modification

As it stands, when you make changes to a cell, there's no need to restart the kernel. You can 
simply rerun the Notebook to see your changes in action. However, in Ngrok's free version, you 
are restricted to three re-executions, which might require a kernel restart.

Nevertheless, Taipy offers built-in functions that enhance the notebook experience with Taipy. 
This eliminates the limitations of the Ngrok free version 
and enables easy updates with fewer re-executions required. You can learn more about this in the 
[linked article](https://www.taipy.io/tips/taipy-gui/taipy-in-jupyter-notebooks/).

## Modification of the markdown with

`Page.set_content` here are the new cells to add:

1. Import Markdown:
   ![Modification of the markdown](Sharing_Taipy_Ngrok_8.png){width=100%}

2. Set empty new page:
   ![Modification of the markdown](Sharing_Taipy_Ngrok_9.png){width=100%}

3. Set content to `new_page`:
   ![Modification of the markdown](Sharing_Taipy_Ngrok_10.png){width=100%}

4. Update the `pages` definition:
   ![Modification of the markdown](Sharing_Taipy_Ngrok_11.png){width=100%}

## Variable modification with `gui.reload`

1. Add this step
   ![Variable modification](Sharing_Taipy_Ngrok_12.png){width=100%}

2. Update your `Gui.run`
   ![Variable modification](Sharing_Taipy_Ngrok_13.png){width=100%}

3. Add the `gui.reload` function
   ![Variable modification](Sharing_Taipy_Ngrok_14.png){width=100%}

After you've made your modifications, just rerun the cell where you made the changes and 
activate the reload function. Refresh your application page to view the updates you've made.

## Conclusion

To sum it up, deploying a Taipy application on Google Colab with Ngrok offers a convenient way 
to share graphical interfaces and applications on the internet.

Google Colab provides access to high-performance hardware without the need for physical machines.
Ngrok, on the other hand, offers a temporary or permanent public URL for your application, 
making it accessible to anyone. By following the steps outlined in this article, you can easily 
set up your Taipy application on Google Colab and share it with others. Additionally, adjusting 
the delay parameter can enhance the user experience for your application.

In general, this approach is an excellent choice for those looking to develop and deploy 
powerful graphical user interfaces in the cloud without excessive complexity.
