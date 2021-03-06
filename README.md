# SSPredict: Solid-Solution Strengthening Prediction

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

=================
   * [SSPredict: Solid-Solution Strengthening Prediction](#sspredict-solid-solution-strengthening-prediction)
      * [Introduction](#introduction)
      * [Required Packages](#required-packages)
      * [Usage](#usage)
         * [Using the tool with installation](#using-the-tool-with-installation)
         * [Using the tool WITHOUT INSTALLATION](#using-the-tool-without-installation)
            * [Clone the tool to where you want to start the project:](#clone-the-tool-to-where-you-want-to-start-the-project)
            * [Setup input file](#setup-input-file)
            * [Predict the strengths](#-predict-the-strengths)
            * [Plot the strengths with the outputfile_for_plot](#-plot-the-strengths-with-the-outputfile_for_plot)
      * [Examples](#examples)
      * 🚀 [TUTORIAL](/TUTORIAL.md)

  
  
## Introduction

SSPredict is a command line tool to visualize the [solid solution strengthening](https://en.wikipedia.org/wiki/Solid_solution_strengthening) stresses of **Complex concentrated alloys (CCAs)**.

[Complex concentrated alloys (CCA)](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C15&q=complex+concentrated+alloys&btnG=) is an emerging class of multi-component alloy with promising properties and unexploit possibilities. Accelerating the discovery of high strength CCAs based on solid solution strengthening is challenging because of their complicated compositions. 

This tool is designed to **visualize** the solid solution strengthening stress regarding the combinations of components and the vast composition space of CCAs. Users are allowed to change alloying combinations and concentrations to explore the strengthening effects. The formulations are based on an elasticity-based model for random solid solution alloys.<sup id="a1">[1](#f1)</sup> <sup id="a2">[2](#f2)</sup> <sup id="a3">[3](#f3)</sup>



## Required Packages

It is a python3-based tool, currently not working well on python2.  2.1  Packages 

- **matplotlib** (code version 1.13.3)

- **numpy** (code version 2.1.0)

- **pandas** (code version 0.23.4)



## Usage

### Using the tool with installation

If you want to use the tool in any folder or project you like, please read [INSTALL.md](/INSTALL.md) to install the code.  
For more details of using the tool, [TUTORIAL.md](/TUTORIAL.md) is helpful. 


### Using the tool WITHOUT INSTALLATION

#### Clone the tool to where you want to start the project:

```
$ cd /path/to/dir
$ git clone https://github.com/DS-Wen/SSPredict.git
```

#### Setup input file

[Here to see the input file setup and examples](/examples/input_guide.md)

#### 📍 Predict the strengths

Under sspredict/ 

```
$ cd /path/to/sspredict/
```

Use predictss.py to predict data from an inputfile

```
$ python3 predictss.py -f inputfile -o outputfile_for_plot  
```

Where outputfile_for_plot is a .txt file including input information and data generated.  

Details of the generated data are described in the [data_description.pdf](examples/output_description.pdf)

#### 📍 Plot the strengths with the outputfile_for_plot
You can plot the strength. 
```
$ python3 predictss.py -str outputfile_for_plot
```
You can combine the strength contour plot with phase diagrams if you have a file generated from ThermoCalc. 
See [TUTORIAL.md](/TUTORIAL.md) for details.  
```
$ python3 predictss.py -str outputfile_for_plot -pd phase_diagram_file
```
or to save the .png directly:

```
$ python3 predictss.py -str outputfile_for_plot -s xxx
```


## Examples

![](examples/MnFe-CoNi-Al/MnFe-CoNi-Al_strength_phase.png)
![](examples/Mn-FeCoNi-AlCu/Mn-FeCoNi-AlCu_plot.png)
![](examples/MnFe-CoNi-AlCu/MnFe-CoNi-AlCu_plot.png)



If there’s any questions or advice, please [open an issue](https://github.com/DS-Wen/SSPredict/issues/new) or [email us](mailto:wen94@purdue.edu?subject=[Github]%20SSPredict).



<b id="f1">1</b> Varvenne, Céline, Aitor Luque, and William A. Curtin. "Theory of strengthening in fcc high entropy alloys." *Acta Materialia*118 (2016): 164-176. [↩](#a1)  

<b id="f2">2</b> Varvenne, Céline, et al. "Solute strengthening in random alloys." *Acta Materialia* 124 (2017): 660-683. [↩](#a2)  
   
<b id="f2">3</b> Varvenne, Céline, and William A. Curtin. "Predicting yield strengths of noble metal high entropy alloys." *Scripta Materialia* 142 (2018): 92-95. [↩](#a3)
