# Cartoonizer_offline.py
When fed with the input image with the command,
python Cartoonize_offline.py imagename.jpg
it generates the output cartoonized image as imagenamep.jpg.

The values can be tweaked to get an optimized cartoonified image.

# Webcam in PHP Using html5
Use webcam in PHP using HTML5, Jquery and Save the Image to Database

This repository will help you to integrate and save the captured image to the database or local folder.

# webcamClass.php
Here are some code structure to understand the important parts of this class.
````
$imageFolder="your folder"; - This is your folder where you would like to save the file
````
````
showImage() - This function will get the image and return the name including the path
````
If you want to save the image to database than you can use this function.
````
changeImagetoBase64() - This function will change the image to base64 
````
````
saveImageToDatabase() -  It will help you to save the image to database
````

# Action2.php
Calls the python file Cartoonize_offline.py.
It output the errors in the python code to the error log file.