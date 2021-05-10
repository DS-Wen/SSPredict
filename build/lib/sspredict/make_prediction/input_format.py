class input_format():
    def __init__(self,format_tag):
        self.tag = format_tag
        
    def print_sample_input(self):
        
        if self.tag =='FCC_BCC_Edge_Ternary':
            print('''
Sample JSON for using pseudo-ternary predictions of solid solution strength by Curtin edge dislocation model. 
------------------------------------------------------------
{
    "material":"MnFeCoNiAl",
    "structure":"FCC",
    "pseudo-ternary":{
        "increment": 1,
        "psA": {"grouped_elements":["Mn","Co"],
                "ratio": [1,1],
                "range":[0,100]},
        "psB": {"grouped_elements":["Fe","Ni"],
                "ratio": [1,1],
                "range":[0,100]},
        "psC": {"grouped_elements":["Al"],
                "ratio": [1],
                "range":[0,100]}
    },
    "elements":{
        "Co": {"Vn":11.12,"E":262.9,"G":101.7,"nu":0.292},
        "Ni": {"Vn":10.94,"E":199.1,"G":76.0,"nu":0.309},
        "Al": {"Vn":16.472,"E":65.5,"G":23.9,"nu":0.369},
        "Mn": {"Vn":12.60,"E":197.7,"G":73.4,"nu":0.347},
        "Fe": {"Vn":12.09,"E":194.3,"G":73.4}
    },
    "uncertainty_level":{
        "on/off":"on",
        "a":0.01, 
        "elastic_constants":0.05
    },
    "conditions":{"temperature":300,"strain_r":0.001},
    "model":{
        "name":"FCC_Varvenne-Curtin-2016"
    },
    "savefile":"MnFeCoNiAl_out"
}
------------------------------------------------------------
Nesessary tags: 
"material": material name
--
"structure": "FCC" or "BCC"
--
"pseudo-ternary": containing "psA" "psB" 'psC' for pseudo-ternary components
    "psA":  pseudo-ternary component, can be a single element or grouped element. 
        "grouped_elements": # group specific elements in psA 
                            # eg.  "grouped_elements":["Ni","Co"], Mn and Co are grouped
        "ratio":            # specify the ratio between elements in A
                            # eg.  "ratio": [1,1],  represent Co:Ni=1:1
        "range":            # specify the concentration range for "psA"
                            # eg.  "range":[0,100], range from 0 to 100 at.% 
--
"elements": input data for elements: 
    "Co": element symbol for Co
        "Vn": atomic volume 
        "a": lattice constant
        "b": Burgers vector
        # NOTE, just need to specify one of "Vn", "a" or "b"
        "E": Young's modulus
        "G": shear modulus 
        "nu": Poisson's ratio
        # NOTE, in Voigt notation, as indicated in the paper. 
        # Need to specify 2 of the "E", "G", and "nu" for isotropic.
--
"conditions": experimental conditions
    "temperature": Kelvin
    "strain_r": experiment strain rate, 
                typical tensile tests: 0.001 /s

"model": 
    IMPORTANT!!!
    "name": name of the model, 
            use "FCC_Varvenne-Curtin-2016" for FCC and 
            use "BCC_edge_Maresca-Curtin-2019" for BCC
            
    The following are adjustable parameters for the model 
    "f1":   # dimensionless pressure field parameter for athermal yield stress 
    "f2":   # dimensionless pressure field parameter for energy barrier
    "alpha": # dislocation line tension parameter
    IMPORTANT: 
    If you don't know f1, f2, and alpha for your material,
    DO NOT change f1, f2 and alpha. 
    The default values were optimized for FCC HEAs and BCC HEAs.
    Read Curtin's papers. 
    
-------
Optional tags:
"uncertainty_level": allow uncertainty evaluation on input data. 

    "on/off":"on"              # turn on/off the uncertainty calculation
                               # if off, no need to set the following tags
                               # if on, specify the standard deviations 
                                        for lattice constants and elastic constants
    
    "a": 0.01                  # applied 1% standard deviation to lattice constants
                               # 1000 data points were generated to evaluate the average and standar deviation
                               # this means for each element, 
                               # a new lattice constant will be generated using normal distribution,
                               # centered at the value "a" (lattice constants) in "elements"
                               # with a standard deviation 0.01a. 
                               
    "elastic_constants": 0.05  # applied 5% standard deviation to elastic constants 
                               # 1000 data points were generated to evaluate the average and standar deviation
                               # this means for each element, 
                               # new elastic constants will be generated using normal distribution,
                               # centered at the values "E", "G", "nu" (elastic constants) in "elements"
                               # with a standard deviation 0.01a. 


"savefile": output filename, CSV file. 
    
END
''')
        elif self.tag =='FCC_BCC_Edge_Composition_Temperature':
            print('''
Sample JSON for composition-temperature predictions of solid solution strength by Curtin edge dislocation model. 
------------------------------------------------------------
{
    "material":"MnFeCoNi",
    "structure":"FCC",
    "elements":{
        "Co": {"Vn":11.12,"E":262.9,"G":101.7,"nu":0.292},
        "Ni": {"Vn":10.94,"E":199.1,"G":76.0,"nu":0.309},
        "Mn": {"Vn":12.60,"E":197.7,"G":73.4,"nu":0.347},
        "Fe": {"Vn":12.09,"E":194.3,"G":73.4}
    },
    "compositions":{
        "element_order": ["Co","Ni","Fe","Mn"],
        "concentrations": [
            [25,25,25,25],
            [20,20,30,30],
            [30,30,20,20]
        ]

    },
    "uncertainty_level":{
        "on/off":"on",
        "a":0.01, 
        "elastic_constants":0.05
    },
    "conditions":{
        "temperature":{
            "min": 300,
            "max": 600,
            "inc": 10
        },
        "strain_r":0.001
    },
    "model":{
        "name":"FCC_Varvenne-Curtin-2016"
    },
    "savefile":"MnFeCoNi_out"
}
------------------------------------------------------------
Nesessary tags: 
"material": material name
--
"structure": "FCC" or "BCC"
--
"compositions": containing element symbols and concentrations for calculation. 
    "element_order":  a list of element symbols in order, be consistent with the "concentrations"
    "concentrations": a list of concentrations in at.% for elements in the "element_order", 
                      add up to 100.
--
"elements": input data for elements: 
    "Co": element symbol for Co
        "Vn": atomic volume 
        "a": lattice constant
        "b": Burgers vector
        # NOTE, just need to specify one of "Vn", "a" or "b"
        "E": Young's modulus
        "G": shear modulus 
        "nu": Poisson's ratio
        # NOTE, in Voigt notation, as indicated in the paper. 
        # Need to specify 2 of the "E", "G", and "nu" for isotropic.
--
"conditions": experimental conditions
    "temperature": specify temperature (Kelvin) range and increment for the calculations.
        "max":  max T
        "min":  min T
        "inc":  increment. 
    "strain_r": experiment strain rate, 
                typical tensile tests: 0.001 /s

"model": 
    IMPORTANT!!!
    "name": name of the model, 
            use "FCC_Varvenne-Curtin-2016" for FCC and 
            use "BCC_edge_Maresca-Curtin-2019" for BCC
            
    The following are adjustable parameters for the model 
    "f1":   # dimensionless pressure field parameter for athermal yield stress 
    "f2":   # dimensionless pressure field parameter for energy barrier
    "alpha": # dislocation line tension parameter
    IMPORTANT: 
    If you don't know f1, f2, and alpha for your material,
    DO NOT change f1, f2 and alpha. 
    The default values were optimized for FCC HEAs and BCC HEAs.
    Read Curtin's papers. 
    
-------
Optional tags:
"uncertainty_level": allow uncertainty evaluation on input data. 

    "on/off":"on"              # turn on/off the uncertainty calculation
                               # if off, no need to set the following tags
                               # if on, specify the standard deviations 
                                        for lattice constants and elastic constants
    
    "a": 0.01                  # applied 1% standard deviation to lattice constants
                               # 1000 data points were generated to evaluate the average and standar deviation
                               # this means for each element, 
                               # a new lattice constant will be generated using normal distribution,
                               # centered at the value "a" (lattice constants) in "elements"
                               # with a standard deviation 0.01a. 
                               
    "elastic_constants": 0.05  # applied 5% standard deviation to elastic constants 
                               # 1000 data points were generated to evaluate the average and standar deviation
                               # this means for each element, 
                               # new elastic constants will be generated using normal distribution,
                               # centered at the values "E", "G", "nu" (elastic constants) in "elements"
                               # with a standard deviation 0.05*value. 
                               
"savefile": output filename, CSV file. 
    
END
''')
        elif self.tag =='BCC_Screw_Curtin_Ternary':
            print('''
Sample JSON for predictions of solid solution strength for pseudo-ternary BCC by Curtin screw dislocation model. 
Screw dislocation in BCC. 
------------------------------------------------------------
{
    "material":"NbMoW",
    "pseudo-ternary":{
        "increment": 1,
        "psA": {"grouped_elements":["Nb"],
                "ratio": [1],
                "range":[0,100]},
        "psB": {"grouped_elements":["Mo"],
                "ratio": [1],
                "range":[0,100]},
        "psC": {"grouped_elements":["W"],
                "ratio": [1],
                "range":[0,100]}
    },
    "elements":{
        "Nb": {"a":3.30,"Delta_E_p":0.0345,"E_k":0.6400,"E_v":2.9899,"E_si":5.2563,"Delta_V_p":0.020},
        "Mo": {"a":3.14,"Delta_E_p":0.1579,"E_k":0.5251,"E_v":2.9607,"E_si":7.3792,"Delta_V_p":0.020},
        "W": {"a":3.16,"Delta_E_p":0.1493,"E_k":0.9057,"E_v":3.5655,"E_si":9.5417,"Delta_V_p":0.020}
    },
    "adjustables":{
        "kink_width":10,
        "Delta_V_p_scaler":1,
        "Delta_E_p_scaler":1
    },
    "conditions":{"temperature":300,"strain_r":0.001},
    "model":{
        "name":"BCC_screw_Maresca-Curtin-2019"
    },
    "savefile":"NbMoW_out"
}
------------------------------------------------------------
Nesessary tags: 
"material": material name
--
"pseudo-ternary": containing "psA" "psB" 'psC' for pseudo-ternary components
    "psA":  pseudo-ternary component, can be a single element or grouped elements. 
        "grouped_elements": # group specific elements in psA 
                            # eg.  "grouped_elements":["W","Ta"], Mn and Co are grouped
        "ratio":            # specify the ratio between elements in A
                            # eg.  "ratio": [1,1],  represent W:Ta=1:1
        "range":            # specify the concentration range for "psA"
                            # eg.  "range":[0,100], range from 0 to 100 at.% 
--
"elements": input data for elements: 
    "W": element symbol for W
        below are necessary inputs. 
        "a":                lattice constant
        "E_k":              screw dislocation kink formation energy (usually by DFT or MD calculations)
        "E_v":              vacancy formation energy (usually by DFT or MD)
        "E_si":             self-interstitial formation energy (usually by DFT or MD)
        "Delta_E_p":        solute-dislocation interaction energy (usually by DFT or MD)
        "Delta_V_p":        Peierls barrier (usually by DFT or MD)
--
"adjustables": adjustable parameters for the model. Be VERY careful to change the values.
    "kink_width":10          kink width, default is 10, (unit: burgers vector), usually between 10b to 20b. 
    "Delta_V_p_scaler":1,    Peierls barrier scaler, DFT values are usually very high compared to experiments.
                             So rescaling was taken to fit the experimental yield strengths.
    "Delta_E_p_scaler":1     Solute-dislocation interaction energy scaler.
                             This is also rescaled for DFT/MD values. 
--
"conditions": experimental conditions
    "temperature": specify temperature (Kelvin) the calculations.
    "strain_r":    experiment strain rate, 
                   typical tensile tests: 0.001 /s
--
"model": "BCC_screw_Maresca-Curtin-2019", 
-------
Optional tags:
"savefile": output filename, CSV file. 

END
''')
        elif self.tag =='BCC_Screw_Curtin_Composition_Temperature':
            print('''
Sample JSON for composition-temperature predictions of BCC solid solution strength by Curtin screw dislocation model. 
Screw dislocation in BCC. 
------------------------------------------------------------
{
    "material":"Nb95Mo5",
    "model":"BCC_screw_Maresca-Curtin-2019",
    "properties":{
        "a": 3.289,
        "E_k": 0.6342, 
        "E_v": 2.989,
        "E_si": 5.361,
        "Delta_E_p": 0.0488,  
        "Delta_V_p": 0.020
    },
    "conditions":{
        "temperature":{
            "max":500,
            "min":0,
            "inc":10
        },
        "strain_r":0.001
    },
    "adjustables":{
        "kink_width":10,
        "Delta_V_p_scaler":1,
        "Delta_E_p_scaler":1
    },
    "savefile":"Nb95Mo5_out"
}
------------------------------------------------------------
Nesessary tags: 
"material": material name
--
"properties": input data for the material: 

    "a":                lattice constant
    "E_k":              screw dislocation kink formation energy (usually by DFT or MD calculations)
    "E_v":              vacancy formation energy (usually by DFT or MD)
    "E_si":             self-interstitial formation energy (usually by DFT or MD)
    "Delta_E_p":        solute-dislocation interaction energy (usually by DFT or MD)
    "Delta_V_p":        Peierls barrier (usually by DFT or MD)
--
"conditions": experimental conditions
    "temperature": specify temperature (Kelvin) range and increment for the calculations.
        "max":  max T
        "min":  min T
        "inc":  increment. 
    "strain_r": experiment strain rate, 
                typical tensile tests: 0.001 /s
--
"adjustables": adjustable parameters for the model. Be VERY careful to change the values.
    "kink_width":10          kink width, default is 10, (unit: burgers vector), usually between 10b to 20b. 
    "Delta_V_p_scaler":1,    Peierls barrier scaler, DFT values are usually very high compared to experiments.
                             So rescaling was taken to fit the experimental yield strengths.
    "Delta_E_p_scaler":1     Solute-dislocation interaction energy scaler.
                             This is also rescaled for DFT/MD values. 
--
"model": "BCC_screw_Maresca-Curtin-2019", 
-------
Optional tags:
"savefile": output filename, CSV file. 

END
''')
        elif self.tag =='BCC_Screw_Suzuki_Temperature':
            print('under development')

        else:
            print('NOT a valid name. Available input formats: \n'
                             'FCC_BCC_Edge_Ternary\n'
                             'FCC_BCC_Edge_Composition_Temperature\n'
                             'BCC_Screw_Curtin_Ternary\n'
                             'BCC_Screw_Curtin_Composition_Temperature\n'
                             'BCC_Screw_Suzuki_Temperature\n')