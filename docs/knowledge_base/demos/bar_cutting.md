Precision bar cutting is an essential task in various industries, and the Bar Cutting demo 
powered by Taipy is here to transform it. In this demo, we will explore this application's 
capabilities, which optimize bar cutting using different algorithms for enhanced efficiency and 
minimized losses.

# Understanding Bar Cutting Optimization

[Bar Cutting](https://en.wikipedia.org/wiki/Cutting_stock_problem) optimization is the process 
of choosing the best size of cuts to make in bars to minimize waste, and maximize the raw material utilization. It's a critical task in industries where material lost represents important costs or shortfalls.


# The Bar Cutting application

## Page 1: A Glimpse of the Initial Page

On the application's starting page, users can choose one of the two cases they want to run. 
When they click the RUN button, it initiates the following series of actions:

1. Loading of the selected dataset (Case 1/Case 2 or Case 3).
2. Execution of two algorithms: Baseline and Optim.
3. Display of results, with the loss depicted in blue on the bar chart.

The bar chart displays the cutting patterns, showing the lengths of customer bars and, 
importantly, the amount of material wasted. Users can switch between algorithms to 
quickly see the difference in material waste, with the Optim algorithm usually 
performing better than the Baseline.

<img src=bar cutting page 1](https://github.com/Avaiga/taipy-doc/assets/31435778/fb5b9154-888d-4640-9e8d-e52596d622b3 width="500">
  

## Page 2: Exploring Input Data and Metrics

For more detailed information, users can open the Parameters panel to review the input data 
for the selected case. This includes details about the available stock (the original bars for cutting) and the demand.

The Metrics page displays important metrics for both the Baseline and Optim models, 
presenting them in various ways like bar charts and pie charts. These metrics demonstrate 
the material waste as a percentage of the total length of the original bars (mother bars) used 
or as the actual amount of material wasted (in millimeters).

<img src=https://github.com/Avaiga/taipy-doc/assets/31435778/3ccbead1-e756-43c2-8375-b7309e76fe36 width="500">

## Page 3: Comparing Model Performance

The balance icon on the left panel leads users to another page where the performance of the two 
models is displayed side by side. This comparative view provides valuable insights into which 
algorithm yields superior results for the selected case.

<img src=https://github.com/Avaiga/taipy-doc/assets/31435778/7ab84665-083e-4c43-8ccb-c22ed43f3f27 width="500">


## Page 4: Comparing Scenarios 

For a comprehensive analysis, users can compare the performance of each model across different 
use cases (scenarios) by clicking on the balance icon. This feature aids in understanding how 
each algorithm performs under varying conditions.

<img src=https://github.com/Avaiga/taipy-doc/assets/31435778/f9a7c59a-598f-42dd-98dd-63f0cd79ac07 width="500">


## Page 5: Databases 
The results are summarized and displayed in a table that can be conveniently downloaded 
as a CSV file for further analysis.

<img src=https://github.com/Avaiga/taipy-doc/assets/31435778/0a1d793b-6e81-4231-8291-9585ff4c8f7b width="500">


# Disclaimer

Please note that the code for this demo is not publicly available at this stage but can be 
shared upon request. Feel free to [contact us](https://www.taipy.io/contact-us/) if you wish to 
receive a sample.

# Conclusion

The Bar Cutting demo exemplifies Taipy's prowess in precision cutting optimization. Whether 
you're involved in manufacturing, logistics, or any industry requiring efficient bar cutting, 
Taipy simplifies the process and minimizes losses in an intuitive and visually appealing manner.

Take the time to explore the application, experiment with various scenarios, 
and utilize the capabilities of Taipy for more accurate and efficient bar cutting.

