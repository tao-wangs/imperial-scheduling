# Project Title

70068 - Workflow Scheduling Coursework Solution  

## Authors

The following individuals contributed to this coursework:

- Purin Sukpanichnant (ps1620)
- Tao Wang (tw520) 

## Introduction

This folder contains all the implemented code and printouts for the 70068 - Scheduling and Resource Allocation coursework. 

## Files Included

- `tabu.py`: Contains the full implementation of the Tabu Search algorithm, methods for experimentation and solutions to Question 2.
- `vns.py`: Contains the full implementation of the Reduced Variable Neighbourhood Search algorithm, neighbourhood generation functions and solutions to Question 3.
- `utils.py`: Contains helper methods used in the tabu search and VNS algorithms.
- `constants.py`: Contains the global constant values for computing solutions to Question 2 and 3. Values are corresponding to 
Appendix A and B in the coursework specification, as well as experimental values obtained from Azure VM.    
- `test.py`: Contains test cases for verifying the correctness of the Tabu Search algorithm implementation. 
- `tabu_output.txt`: Printout of the execution of the Tabu Search algorithm. Shows the current solution considered at each iteration of the Tabu Search method and their cost.
- `vns_output.txt`: Printout of the execution of the Reduced Variable Neighbourhood Search algorithm. Shows the current solution considered at each iteration of the VNS method and their cost.

## Required Dependencies

- Python 3.x: Programming language used for all code implementations.
- collections: For efficient O(1) appending and removing of elements. 
- numPy: For efficient vectorised operations on arrays. 
- random: For pseudo-random generation of numbers in VNS algorithm.
- csv: For converting schedules to CSV format to run on Azure VM, if necessary.  

### Question 2 (`tabu.py`)

Execute the file without any additional arguments, and the solutions for Question 2.1 and 2.2 will be output in the terminal.

`python tabu.py`

### Question 3 (`vns.py`)

Execute the file without any additional arguments, and the solutions for Question 3.2 and 3.1 will be output in the terminal.

`python vns.py`

### Utilities (`utils.py` and `constants.py`)

The relevant functions and variables from these modules are already imported by both`tabu.py` and `vns.py`, thus no additional configuration work is required. 
