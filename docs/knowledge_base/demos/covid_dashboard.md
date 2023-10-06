In the realm of COVID-19 data analysis, access to real-time insights is paramount.
Introducing the COVID-19 Dashboard, a multi-page Taipy application, designed for
in-depth data visualization and trend forecasting.

[Try it live](https://covid-dashboard.taipy.cloud/Country) 

[Get it on GitHub](https://github.com/Avaiga/demo-covid-dashboard)

# Understanding the Application
The application comprises four pages accessible via the upper tabs : Country, Map, Predictions, World.

## Page 1: Country
- Detailed country-specific COVID-19 statistics.
- Easily switch between cumulative and density data views.
- Interactive line chart for dynamic data exploration.
- Pie chart illustrating case distribution (Confirmed, Recovered, Deaths).

<img src=covid-dashboard-country width ="615">

## Page 2: Map
Visual representation of COVID-19 impact through dynamic color-coded maps.

<img src=covid-dashboard-map width ="615">

## Page 3: Predictions
Generate COVID-19 predictions by creating scenarios and selecting prediction
dates. This is generated with an ARIMA and a Linear Regression algorithms defined as predictions_x and predictions_y.

How to use it:

1. Initiate a new scenario by assigning it a name.
2. Specify a prediction date.
3. Choose a country.
4. Click the "Submit" button and here we go!
5. To view your scenario, access it in the Scenario tab located within the Results section.

<img src=covid-dashboard-country width ="615">

## Page 4: World
Global COVID-19 statistics summarized via line and pie charts. The Comparison of Covid countries' impact can be seen by changing the toggle between ‘Absolute’ and ‘Relative’.  

<img src=covid-dashboard-world width ="615">
