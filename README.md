# poc
A project for testing different technologies


## App 1: Dash/Plotly POC

Using full-stack python, I'd like to POC creating a template website where I can perform basic exploratory data analysis. This incorporate the following components:
  - Uploading a CSV of any kind
  - Passing to a summary function to review descriptive statistics about the dataset
  - Basic charting and multiple linear regression output


### Notes
The structure of each of the functions is interesting within Dash. Each section is composed of an action, and a corresponding set of Divs / HTML components that react dynamically to user input.

This is especially useful when an existing framework already exists - or a set of data has already been loaded. However, charts will automatically be rendered as a result of these behaviors. I need a way to trigger certain functions to run. I can do this through global switches.
