# Adding custom visual elements

Although Taipy GUI comes with a set of visual elements that lets users create comprehensive
user interface, there are situations where applications may need to provide a very specific
kind of element, with capabilities that one cannot find in Taipy out-of-the-box.

Taipy GUI lets developers add their own visual elements in order to address specific use
cases or integrate third-party Web components. One can expand the functionality
offered by the base Taipy GUI package to create custom components that can be
effortlessly used in pages and shared with the community.

A custom visual element is made of two parts:

- The Python part.<br/>
  New visual elements are declared using Python code. They are grouped into
  what is referred to an *element library*.
  Element libraries can hold several elements.<br/>
  In the page definition text you can reference a custom visual element using the
  element name `<library_name>.<element_name>` in your Markdown pages (or
  `<library_name>:<element_name>` with the HTML syntax).

- The Javascript part.<br/>
  Visual element declarations indicate how the browser should display the element
  and what interactions are available.

## Prerequisites

In order to create and use custom visual elements, you need to install:

- Python 3.8 or higher.
- Taipy GUI 2.0 or higher (included in Taipy and Taipy Enterprise).
- NodeJS
- NPM


TODO
* Example1: my_company.name -> <span>My Company Name</span>
* Example2: my_company.logo -> <img />
* Example3: my_company.input -> ...
* Example4: my_company.button -> ...
* Example5: my_company.list -> ...
* Example6: my_company.table -> ...
