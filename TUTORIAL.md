
# Tutorial
Then you can start your own project at any folder you like:
```  
$ cd /path/to/yourproject
```
## Strength Prediction
make sure your input_file is in the project directory, see [input_description for strength prediction](/examples/input_guide.md)  
start your prediction with:  
```  
$ sspredict.predict -f input_file -o predicted_data
```
and your data is in your output file "predicted_data".
## Plot Strength Pseudo-Ternary Diagram
To plot the pseudo-ternary diagram with predicted_data:  
```  
$ sspredict.plot -str predicted_data 
```
or you can save it the image as .png file:  
```  
$ sspredict.plot -str predicted_data -s image_name
```
## Plot Strength and Phase Diagram in one Pseudo-Ternary Plot
1. Make sure you put a file ('phase_diagram') generated from ThermoCalc.  
2. In ThermoCalc console mode, you generate a phase diagram for your system at desired temperature.  
3. Make sure your phase diagram share the same coordinate as the pseudo-ternary strength contour plot.  
4. You can generate a file of coordinates in from the ThermoCalc console mode. The file looks like this [example of MnFe-CoNi-Al](/examples/MnFe-CoNi-Al/PD_MnFe-CoNi-Al). The file contains the coordinates of phase boundaries in your phase diagram. 
5. Put this phase diagram file in your project folder.   
Then use: 
```  
$ sspredict.plot -str predicted_data -pd phase_diagram 
```
And save the image by:
```  
$ sspredict.plot -str predicted_data -pd phase_diagram -s image_name
```
