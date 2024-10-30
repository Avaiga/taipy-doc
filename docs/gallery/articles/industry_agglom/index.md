---
title: US Industry Distribution
category: visualization
data-keywords: dashboard maps community
short-description: Explore where industries are concentrated and how they are distributed across the United States.
order: 10
img: industry_agglom/images/map_image.png
hide:
    - toc
---

Explore where industries are concentrated and how they are distributed across
the United States on this interactive map with a chart that also shows the evolution
of these concentrations over time.

[Try it live](https://industry-agglom.taipy.cloud/){: .tp-btn target='blank' }
[Get it on GitHub](https://github.com/Avaiga/demo-industry-agglom){: .tp-btn .tp-btn--accent target='blank' }

![Map](images/map_image.png){width=90% : .tp-image-border }

# Understanding the Application

Traditionally, industrial agglomeration is measured using a metric called Location
Quotient (LQ). This metric is simple but has its limits. For example, less populated
and remote counties will sometimes have high LQs, despite having low employment counts.
This [paper](https://www.statsamerica.org/downloads/user-guides/user-guide-PALQ.pdf){target='blank'} proposes a new metric to resolve these issues called Proximity Adjusted
Location Quotients (PA-LQ or CLQ).

In this demo, you can explore LQs and CLQs for different industries and counties and
notice the differences in the results.
