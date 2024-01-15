Explore datasets using only natural language using TalkToTaipy!

[Try it live](https://talk-to-taipy.taipy.cloud/){: .tp-btn target='blank' }

# Understanding the Application

This application allows users to enter a prompt to manipulate or visualize data such
as "Plot sales by product line in a pie chart" and the app will generate the
appropriate visualization.

This works by calling a quantized version of HuggingFace's StarCoder code generation
LLM model hosted on Azure. The user prompt entered on the Taipy app gets sent to the
model, which uses few-shot learning to generate pandas code to manipulate the data and
Taipy code to create the visualization.

![An example use of TTT](images/talk_to_taipy_example.gif){width=100%}

![What are the 5 most profitable cities?](images/talk_to_taipy_image.jpeg){width=100%}
