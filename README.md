# Ascii Art Project (WIP)

### Overview

This is an ascii art project I made for fun.

It converts an image into an ascii art image.

## Prerequisites


- Python
- Pillow - The photo image library used for this project.
- Flask - The webserver library 
- Pycharm - IDE

## How to run it (on Windows)

Create virtual environment

```
$ python -m venv venv
```

Activate virtual environment

```
$ venv\Scripts\activate.bat
```

Install requirements.txt

```
$ pip install -r requirements.txt
```

Run Flask
````
$ set FLASK_APP=src/main.py
$ flask run
````

### How to check that it is working

There are two test photos located in the resources directory.
The spider_man2.jpg image is a great example of an image that converts well to
ascii art. The Attack On Titan photo demonstrates the limitations
of ascii art and does not show up well.
````
$ curl -v -X POST -H "Content-Type: multipart/form-data" -F "file=@resources\spider_man2.jpg" localhost:5000/ascii
````

### Connect to frontend app

Part two of this project involves using React as the frontend
to upload an image to this backend server, and an ascii art image 
is returned to the user.

For more information and directions on how to connect the two projects,
go to the image-upload-frontend repository here:
https://github.com/CSprat451/image-upload-frontend
