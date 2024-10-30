---
title: RAG Chatbot
category: llm
data-keywords: vizelement ai community
short-description: A chatbot to ask questions about pdf files using RAG
order: 14
img: rag_chatbot/images/rag_screen.png
hide:
    - toc
---
This demo showcases Taipy's ability to enable end-users to run inference using LLMs.
Here, we use Langchain to query Mistral's LLM model hosted on HuggingFace to ask questions
about PDF files using RAG.

[Get it on GitHub](https://github.com/Avaiga/demo-gpt-4o/tree/rag){: .tp-btn .tp-btn--accent target='blank' }

# Understanding the Application

This application uses RAG (Retrieval-Augmented Generation) to answer questions about PDF files.
The user can upload his PDF files in a specific folder and ask questions about them on
the Taipy interface. This project uses Langchain to query Mistral's LLM model hosted on HuggingFace, but this can be easily adapted to other models or APIs.

![RAG Screenshot](images/rag_screen.png){width=100% : .tp-image-border }

A tutorial on how to write similar
LLM inference applications is available
[here](../../../tutorials/articles/rag_chatbot/index.md).
