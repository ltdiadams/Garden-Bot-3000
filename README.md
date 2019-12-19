# The Garden-Bot-3000

Django Web App which plots values of moisture, temperature, and light with respect to time, as they are written to an uploaded CSV by a Raspberry Pi monitoring plant readings.

The Web App design was primarily focused on a Home View which displayed 4 graphs in total. However the application also makes use of another view ‘/upload/’ when making POST requests from a python script on the Raspberry Pi itself. There are other views included within the code that were only designed for testing purposes, but the Home and Upload Views are what was made use of within the final product.

On the main page of the site, a user is presented with 4 graphs. An initial graph which displays the current readings of moisture, light, and temperature values. As well as graphs showing the values of moisture, light and temperature at each timestamp (ie., at each second) as the website receives these readings.

The upload view is useful if a user wishes to upload one csv file to the webapp, with matching headers to the csv given by the Pi. They will be prompted to select a file and upload it, once they click ‘upload’ the home page will be reset with the new data, and the user can notice this if they return to the main view. How the python script on the pi (piscript) is working is that it is making these requests to this upload form in an infinite loop every second with the CSV as it is written to with current values from the Pi, every second, until we cancel that script. Ideally, if we were to have this read in values for a very long time, we would only have the CSV file update every few minutes or every hour, so as to minimize a ridiculous number of data points.

This website was created using a high-level web framework for Python called Django. The appeal to Django was its versatility. It can be used to design practically any type of webapp and can deliver content through HTML format easily, and comes with a lot of features, straight out of the box. Coupled with Django and HTML5, I also made use of a JavaScript library for creating charts with an HTML5 canvas, this library was Chart.js, as it was able to create elegant graphs with appealing animations as well. With this, another software library that was made use of was Pandas, used in the web app for reading in columns and rows of a CSV, and then sending that data to be used to make graphs.


*Built for a Digital Signal Processing class project, planning to do more work down the road*
