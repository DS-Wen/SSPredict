# Install and Use
clone the project to where you want to store the package:  

```  
$ cd /path/to/dir
$ git clone https://github.com/DS-Wen/SSPredict.git .
```
and install it with pip3:  
```  
$ cd /SSPredict 
$ pip3 install .
```
Then you can start your own project at any folder you like:
```  
$ cd /path/to/yourproject
```
make sure your input_file is in the project directory, see [input_description](/examples/input_guide.md)  
start prediction with:  
```  
$ sspredict.predict -f input_file -o predicted_data
```
and to plot the pseudo-ternary diagram with predicted_data:  
```  
$ sspredict.plot -f predicted_data 
```
or you can save it the image as .png file:  
```  
$ sspredict.plot -f predicted_data -s image_name
```
