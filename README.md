# Installing Dependencies

## Before installing dependencies

Make sure you have Microsoft Visual C++ 14.0 or greater installed
To install it, go to this link

```
https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

During install, select `Desktop Development with C++`, and then proceed to install
![alt text](image.png)

After install make sure to restart windows.

## Setup/Dependencies

You will first need to setup the virtual environment using cuda
The terminal command (on Windows) is:

```
python -m venv cuda
```

And then you will install your dependencies onto the virtual environment
Use the following command to enter the virtual environment, when you are installing your dependencies or doing any other work afterwards:

```
cuda\Scripts\activate
```

You will need to install the following dependencies

1. matplotlib
2. numpy
3. pylzma
4. ipykernel
5. jupyter
6. torch

You can download all of the dependencies using this terminal command (on Windows):

```
pip3 install matplotlib numpy pylzma ipykernel jupyter
```

if you have errors with installing the dependencies, and the error tells you to update pip3 
go ahead and use the command given by the error message to update pip3 in the virtual environment
(Do not forget to go into the virtual environment first, using the command given above, before you do the update)

To install torch you can go to this link

```
https://pytorch.org/
```

Scroll down until you see this:

![alt text](image-1.png)

And choose your preferences and use the link given to you at the bottom
For reference, the image contains my preferences and the command I used

```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu128
```