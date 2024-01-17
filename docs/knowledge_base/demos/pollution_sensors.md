---
title: Realtime Pollution Dashboard
category: demos
type: code
data-keywords: gui dashboard vizelement layout chart
short-description: Streams real-time pollution data from sensors and shows air quality on a map.
img: images/pollution_dashboard.png
---
A use-case of measuring air quality with sensors around a factory to showcase the ability of Taipy
to dashboard streaming data.

[Try it live](https://realtime-pollution.taipy.cloud/){: .tp-btn target='blank' }
[Get it on GitHub](https://github.com/Avaiga/demo-realtime-pollution){: .tp-btn .tp-btn--accent target='blank' }

# Understanding the Application

This application shows pollution levels around a factory in real-time. The data is generated on
another server and sent to this Taipy application via a WebSocket. Taipy then processes the data and
displays it on a dashboard. The dashboard is updated in real-time as new data is received.

![Pollution Dashboard](images/pollution_dashboard.png){width=100%}

A tutorial on visualizing data streamed from another thread is available [here](../tips/multithreading/index.md).
