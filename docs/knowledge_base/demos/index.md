---
hide:
  - toc
---

Let's explore demos of applications made with Taipy.

<!-- Filters -->
<ul class="tp-pills-list tp-pills-filter">
  <li>
    <input type="checkbox" name="filter-all" id="filter-all" value="all" checked>
    <label class="tp-pill" for="filter-all">
      <span>All</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-gui" id="filter-gui" value="gui">
    <label class="tp-pill" for="filter-gui">
      <span>GUI</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-vizelement" id="filter-vizelement" value="vizelement">
    <label class="tp-pill" for="filter-vizelement">
      <span>Visual elements</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-chart" id="filter-chart" value="chart">
    <label class="tp-pill" for="filter-chart">
      <span>Chart</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-navbar" id="filter-navbar" value="navbar">
    <label class="tp-pill" for="filter-navbar">
      <span>Navbar</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-table" id="filter-table" value="table">
    <label class="tp-pill" for="filter-table">
      <span>Table</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-layout" id="filter-layout" value="layout">
    <label class="tp-pill" for="filter-layout">
      <span>Layout</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-part" id="filter-part" value="part">
    <label class="tp-pill" for="filter-part">
      <span>Part</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-menu" id="filter-menu" value="menu">
    <label class="tp-pill" for="filter-menu">
      <span>Menu</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-state" id="filter-state" value="state">
    <label class="tp-pill" for="filter-state">
      <span>State</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-multi-page" id="filter-multi-page" value="multi-page">
    <label class="tp-pill" for="filter-multi-page">
      <span>Multi-page</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-callback" id="filter-callback" value="callback">
    <label class="tp-pill" for="filter-callback">
      <span>Callback</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-markdown" id="filter-markdown" value="markdown">
    <label class="tp-pill" for="filter-markdown">
      <span>Markdown</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-dashboard" id="filter-dashboard" value="dashboard">
    <label class="tp-pill" for="filter-dashboard">
      <span>Dashboard</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-scenario" id="filter-scenario" value="scenario">
    <label class="tp-pill" for="filter-scenario">
      <span>Scenario</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-task" id="filter-task" value="task">
    <label class="tp-pill" for="filter-task">
      <span>Task</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-datanode" id="filter-datanode" value="datanode">
    <label class="tp-pill" for="filter-datanode">
      <span>Data node</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-cycle" id="filter-cycle" value="cycle">
    <label class="tp-pill" for="filter-cycle">
      <span>Cycle</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-configuration" id="filter-configuration" value="configuration">
    <label class="tp-pill" for="filter-configuration">
      <span>Configuration</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-submission" id="filter-submission" value="submission">
    <label class="tp-pill" for="filter-submission">
      <span>Scenario submission</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-dag" id="filter-dag" value="dag">
    <label class="tp-pill" for="filter-dag">
      <span>DAG</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-scope" id="filter-scope" value="scope">
    <label class="tp-pill" for="filter-scope">
      <span>Scope</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-job" id="filter-job" value="job">
    <label class="tp-pill" for="filter-job">
      <span>Job</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-standalone" id="filter-standalone" value="standalone">
    <label class="tp-pill" for="filter-standalone">
      <span>Standalone</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-comparison" id="filter-comparison" value="comparison">
    <label class="tp-pill" for="filter-comparison">
      <span>Scenario Comparator</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-subscription" id="filter-subscription" value="subscription">
    <label class="tp-pill" for="filter-subscription">
      <span>Scenario Subscription</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-notify" id="filter-notify" value="notify">
    <label class="tp-pill" for="filter-notify">
      <span>Notify</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-storage_type" id="filter-storage_type" value="storage_type">
    <label class="tp-pill" for="filter-storage_type">
      <span>Storage type</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-partials" id="filter-partials" value="partials">
    <label class="tp-pill" for="filter-partials">
      <span>Partials</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-studio" id="filter-studio" value="studio">
    <label class="tp-pill" for="filter-studio">
      <span>Taipy Studio</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-ai" id="filter-ai" value="ai">
    <label class="tp-pill" for="filter-ai">
      <span>AI</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-ai" id="filter-ai" value="ai">
    <label class="tp-pill" for="filter-ai">
      <span>ML</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-optimization" id="filter-optimization" value="optimization">
    <label class="tp-pill" for="filter-optimization">
      <span>Optimization</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-classification" id="filter-classification" value="classification">
    <label class="tp-pill" for="filter-classification">
      <span>Classification</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-maps" id="filter-maps" value="maps">
    <label class="tp-pill" for="filter-maps">
      <span>Maps</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-notebook" id="filter-notebook" value="notebook">
    <label class="tp-pill" for="filter-notebook">
      <span>Notebook</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-deployment" id="filter-deployment" value="deployment">
    <label class="tp-pill" for="filter-deployment">
      <span>Deployment</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-stylekit" id="filter-stylekit" value="stylekit">
    <label class="tp-pill" for="filter-stylekit">
      <span>Stylekit</span>
    </label>
  </li>
  <li>
    <input type="checkbox" name="filter-cloud" id="filter-cloud" value="cloud">
    <label class="tp-pill" for="filter-cloud">
      <span>Taipy Cloud</span>
    </label>
  </li>
</ul>

<ul class="tp-row tp-row--gutter-sm tp-filtered">
  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui dashboard vizelement layout chart">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="sales_dashboard">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/demo-sales-dashboard.jpg">
      </header>
      <div class="tp-content-card-body">
        <h4> Sales Dashboard </h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Check out our Sales Dashboard demo. It reads Excel files and shows valuable insights.
            You can filter data by city, customer, and gender to find specific metrics and use 
            two dynamic charts for trend analysis.
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="tweet_generation">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/tweet-generation.png">
      </header>
      <div class="tp-content-card-body">
        <h4> Tweet Generation </h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Experience the AI-powered Tweet Generation. Create compelling Tweets effortlessly 
            using GPT-3's Davinci engine for text and DALL·E for images. 
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="face_recognition">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/face-recognition.jpg">
      </header>
      <div class="tp-content-card-body">
        <h4> Real-time Face Recognition </h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Explore real-time face detection and recognition demo. Learn how to create custom UI 
            components and use OpenCV for accurate face identification.
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="sentiment_analysis">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/sentiment-analysis-line.png">
      </header>
      <div class="tp-content-card-body">
        <h4>Sentiment Analysis: Detect emotional tones from a text</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Explore the power of Taipy's sentiment analysis capabilities with our two-page 
            application. Analyze user input and uploaded text to uncover sentiments effortlessly. 
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui optimization scenario">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="bar_cutting">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/bar-cutting-bar-Visualization.png">
      </header>
      <div class="tp-content-card-body">
        <h4>Optimize Bar Cut Sizes</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Try out our Bar Cut Optimization demo. It uses Taipy to optimize bar cut sizes for two 
            scenarios with distinct algorithms that reduces raw material waste in a visually 
            intuitive way.
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai classification">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="image_classif">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/icon-code.svg">
      </header>
      <div class="tp-content-card-body">
        <h4>Image Classification</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Explore our interactive image classification application built with Taipy, Nvidia CUDA, 
            and TensorFlow.
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai classification scenario">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="churn_classification">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/churn-classification-data-Visualization-histogram.png">
      </header>
      <div class="tp-content-card-body">
        <h4>Churn Classification</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Explore our Churn Classification demo. Use Taipy for data analysis, model management,
            and model comparison in churn prediction. Witness the capabilities of Taipy in 
            streamlining and improving decision-making.
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui optimization scenario cycle comparison">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="production_planning">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/production-planning-data-visualization.png">
      </header>
      <div class="tp-content-card-body">
        <h4>Production Planning</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Discover our Production Planning demo application that optimize production, reduce 
            costs, and simulate manufacturing scenarios. 
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai dashboard">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="stock_visualization">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/stock-visualization.png">
      </header>
      <div class="tp-content-card-body">
        <h4>Stock Visualization</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Explore the Stock Visualization Dashboard that leverages Taipy GUI and Prophet to 
            visualize historical stock data and make predictions over 5 years.
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai dashboard multi-page maps scenario datanode">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="covid_dashboard">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/covid-dashboard-country.png">
      </header>
      <div class="tp-content-card-body">
        <h4>Covid Dashboard</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Discover our minimalist yet powerful COVID-19 dashboard. View and forecast COVID-19
            data for various countries, interact with maps, and gain insights into the global 
            pandemic impact.
        </p>
      </div> 
    </a>
  </li>

  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="gui ai dashboard">
    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="movie_genre_selector">
      <header class="tp-content-card-header">
        <img class="tp-content-card-image" src="images/movie-genre-selector.png">
      </header>
      <div class="tp-content-card-body">
        <h4>Movie Genre Selector</h4>
        <span class="tp-tag">Front-end | Back-end</span>
        <p> Explore Movie Genre Selector demo. See how this user-friendly tool helps you 
            effortlessly discover movies from your favorite movie genres.
        </p>
      </div> 
    </a>
  </li>
</ul>
