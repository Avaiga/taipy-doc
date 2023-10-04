# Multi-page Application

Are you tired of messy and confusing dashboards that make it hard to find the information you need? 
If so, it might be a good idea to switch to multipage applications!

![Multi-page Application](multipage_application.png){width=100%}

Multipage applications allow you to organize your data and visualizations into separate pages, 
making it easier to navigate and focus on specific insights. At Taipy, we understand 
how important clear and effective data visualization is, 
which is why we've created a multipage feature that lets you build user-friendly dashboards 
that are easy to understand.

We've prepared a two-part series of articles to explain how to use Taipy's multipage functionality:

In Part 1, we'll go over the basics of creating a multipage application, including 
how to set up your app and add pages.

Stay tuned for Part 2, where we'll cover more advanced features like interactivity and customization. 
Taipy makes creating multipage applications a breeze.

So, if you're ready to enhance your data visualization, check out our multipage feature 
and start creating your own intuitive and insightful applications with Taipy:

## Part 1 – Building a Basic Multi-Page Application

While it's possible to create a multi-page Taipy application in a single script, 
it's often a good practice to organize your code into a folder structure like this:

![Building a Basic Multi-Page Application](multipage_application_2.png){width=100%}

In this arrangement, every submodule in the **pages** folder (like `home.py` and `temperature.py`) 
holds the code for each page in our application. 
We're demonstrating with just two pages in this example, but you can add as many as you need.

## Defining the Pages

To make it simpler, we'll ensure that each page doesn't affect any other page. 
In other words, when you do something on one page, it won't affect the other pages. 
We'll discuss how pages interact with each other in the second part of this series.

Now, let's examine the code for each of our page modules.

![Defining the Pages](multipage_application_3.png){width=100%}

![Defining the Pages](multipage_application_4.png){width=100%}

No need to worry if you don't understand all the code details! 
What's important is that both pages work independently:

- The `home_md` page shows a welcome message.
- The `temperature_md` page lets a user convert temperatures from Fahrenheit (°F) to Celsius (°C).

Usually, if we were making a simple one-page application, we'd give one of our pages 
(Taipy [Markdown](https://docs.taipy.io/en/latest/manuals/reference/taipy.gui.Markdown/) or [HTML](https://docs.taipy.io/en/latest/manuals/reference/taipy.gui.Html/) objects) 
to the `taipy.gui.Gui` constructor. 
For example, to turn `home.py` into a one-page Taipy application, we could add these lines:

![Defining the Pages](multipage_application_5.png){width=100%}

## Defining a Multi-Page Application

Up to this point, we've structured our multi-page Taipy application by 
keeping two one-page applications in a subfolder named "pages."

Now, the next step is to create and define our main module, `main.py` within the *app* directory. 
After that, we'll initialize our multi-page Gui object.

![Defining a Multi-Page Application](multipage_application_6.png){width=100%}

We started by importing two Markdown objects, *home_md* and *temperature_md* from the two scripts we previously created. 
Then, we made a dictionary called `pages`:

1. Each key in the dictionary specifies the URL where you can access that page.
2. Each value in the dictionary is the *Markdown* object for that page.

In the end, we provided this *pages* dictionary as an argument to the *pages* parameter of the Taipy Gui object. 
Then, we called its *run* method, and that's how we got our first Taipy multi-page application working!

If you open your web browser and go to **localhost:5000** (assuming you're using the [default port](https://docs.taipy.io/en/latest/manuals/reference/taipy.gui.Gui/#taipy.gui.gui.Gui.run)), you'll see the following:

![Defining a Multi-Page Application](multipage_application_7.png){width=50%}

You're directed to the */home* URL automatically because it was the first page listed in the *pages* dictionary, and that's where you'll find our first page!

If you change the URL from */home* to */temperature*, you will see the following:

![Defining a Multi-Page Application](multipage_application_8.png){width=50%}

## How to navigate between pages?

Manually changing the URL to navigate between pages isn't ideal. 
Taipy provides several methods for adding navigation to your multi-page application, 
making it more user-friendly and intuitive.

### 1. The navbar

![The navbar](multipage_application_9.gif){width=50%}

One straightforward method to make your application's navigation more appealing 
is by utilizing the Taipy navbar control. 
To incorporate the navbar into the home page, all you need to do is add a single line 
to the beginning of the "home_md" page definition:

![The navbar](multipage_application_9.png){width=100%}

By default, the navbar control automatically creates an entry for each page in the *pages* dictionary, 
requiring no further required specification of properties — making it a quick and easy way to add navigation.

However, the code change above only added a navbar to the home_md page — we would still need to make the same 
change to temperature_md and any other page we have in our application. 
A better alternative that doesn’t require any code modification in any of the pages is to add a **root page**.

Rather than modifying each page to include the navbar, we can also simply modify `main.py` to utilize the [root page](https://docs.taipy.io/en/latest/manuals/gui/pages/#root-page):

![The navbar](multipage_application_10.png){width=100%}

Since every page inherits the root page, you can easily make every page inherit the navbar control 
by adding just one line to `main.py`. 
As an additional tip, you can use HTML *center* tags to center the *navbar* on the page: `<center><|navbar|></center>`

The concept of the *root* page is more advanced in Taipy and will be explored 
in more detail in Part 2 of this Taipy multi-page series.

### 2. The navigate function

The `taipy.gui.navigate` function is self-explanatory in its purpose, 
it is used to navigate to other pages. 
For example, this is a code snippet of the `navigate` function being used to navigate 
to the *home* page when the [button](https://docs.taipy.io/en/latest/manuals/gui/viselements/button/) control is clicked:

![The navigate function](multipage_application_11.png){width=100%}

Naturally, this function is only used within callbacks. To use `navigate`, we simply pass 
along the `state` variable present in all callbacks, as well as the name of the page we wish to go to. 
In the example above, the user will be directed to the */home* page.

The `navigate` function provides a lot of flexibility to the developer to manage navigation 
in the application beyond what the navbar offers. For example, we can manage:

1. After executing some process, direct the user to either the /success or /failure page depending on the process status. 
   
2. Direct the user back to the /home page when an exception occurs 
   by using navigate in [on_exception](<https://docs.taipy.io/en/latest/manuals/gui/callbacks/#exception-handling>).

If you prefer, you can replicate the functionality of the *navbar* using the `navigate` feature 
with a different control, like a [selector](https://docs.taipy.io/en/latest/manuals/gui/viselements/selector/) control or [tree](https://docs.taipy.io/en/latest/manuals/gui/viselements/tree/) control. 
In this example, let's combine the `navigate` feature with the [menu](https://docs.taipy.io/en/latest/manuals/gui/viselements/menu/) control 
(a collapsible side panel) to create the following app:

![The navigate function](multipage_application_11.gif){width=50%}

The menu navigation was implemented by modifying `main.py` to the following:

![The navigate function](multipage_application_12.png){width=100%}

Unlike *navbar* which automatically populates its *lov* (list of values) with the page names 
and intrinsically navigates the user to the selected page when it is interacted with, 
the code example above using the menu control and navigate is a little more verbose.

We define two properties for the menu control:

1. *lov={page_names}*: The list of values which may be selected from the menu. 
   In this case, we interpolate the `page_names` variable, which we then assign the keys from `pages` 
   (other than "/") — functionally equivalent to `page_names = ["home", "temperature"]`. 
   Refer to the [menu](https://docs.taipy.io/en/latest/manuals/gui/viselements/menu/) for more details, such as for setting icons and labels.
2. *on_action=menu_action*: Assigns the `menu_action` function as the callback function which is executed when the user clicks an item from the menu.

We define the `menu_action` function with the parameters as stated in the menu control documentation, 
then call `navigate(state, page)` to direct the user to the selected `page`. 
In practice, we effectively have the same functionality as the navbar, 
but had to do a bit more work to expressly create that functionality.

### 3. Hyperlinks

Finally, the simplest way to implement navigation in Taipy is with a hyperlink:

![Hyperlinks](multipage_application_13.png){width=100%}

This results in the following clickable **temperature** text, which directs the user to the */temperature* URL:

![Hyperlinks](multipage_application_14.png){width=50%}

## Part 2

In preparation for Part 2 of the **Taipy Tips: Building a Multi-Page Application** series, 
you can anticipate learning about the following topics:

1. Accessing state variables across multiple pages, enabling interaction between pages.
2. Gaining insight into how Taipy GUI searches for variables and functions utilized in Markdown pages.
3. Practical code examples to illustrate these concepts.
