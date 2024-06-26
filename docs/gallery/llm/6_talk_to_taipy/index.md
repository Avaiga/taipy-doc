---
title: TalkToTaipy
category: llm
data-keywords: dashboard vizelement layout chart ai enterprise
short-description: Explore datasets using only natural language using TalkToTaipy!
img: 6_talk_to_taipy/images/talk_to_taipy_image.jpeg
---
Explore datasets using only natural language using TalkToTaipy!

!!! note "Enterprise application"

    Taipy provides robust, business-focused applications tailored for enterprise environments. To 
    maintain standards of security and customization, these applications are proprietary like this 
    application. If you’re looking for solutions that are immediately deployable and customizable to 
    your business needs, we invite you to try them out and contact us for more detailed information.

    [Try it live](https://talk-to-taipy.taipy.cloud/){: .tp-btn target='blank' }
    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

# Understanding the Application

This application allows users to enter a prompt to manipulate or visualize data such
as "Plot sales by product line in a pie chart" and the app will generate the
appropriate visualization.

This works by calling a quantized version of HuggingFace's StarCoder code generation
LLM model hosted on Azure. The user prompt entered on the Taipy app gets sent to the
model, which uses few-shot learning to generate pandas code to manipulate the data and
Taipy code to create the visualization.

![An example use of TTT](images/talk_to_taipy_example.gif){width=90% : .tp-image-border }

![What are the 5 most profitable cities?](images/talk_to_taipy_image.jpeg){width=90% : .tp-image-border }
