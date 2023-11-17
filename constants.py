
# Define constants for Coursework Question 2.1
L = 20          # Maximum tabu list size
gamma = 10      # Acceptance threshold  
K = 1000        # Maximum number of iterations

# Incidence matrix of the DAG in the form of a dictionary, according to Appendix A
DAG = {(1, 31): 1, (2, 1): 1, (3, 8): 1, (4, 3): 1, (5, 2): 1, (6, 16): 1, 
     (7, 6): 1, (8, 7): 1, (9, 8): 1, (10, 9): 1, (11, 1): 1, (12, 5): 1, 
     (13, 12): 1, (14, 13): 1, (17, 15): 1, (15, 11): 1, (16, 5): 1, 
     (17, 16): 1, (18, 17): 1, (19, 18): 1, (20, 19): 1, (21, 18): 1, 
     (22, 21): 1, (23, 22): 1, (24, 5): 1, (25, 24): 1, (26, 25): 1, 
     (27, 26): 1, (28, 26): 1, (29, 28): 1, (30, 4): 1, (30, 10): 1, 
     (30, 14): 1, (30, 20): 1, (30, 23): 1, (29, 27): 1, (30, 29): 1}

# Theoretical processing times for each node according to Appendix B
p = {1: 3, 2: 10, 3: 2, 4: 2, 5: 5, 6: 2, 7: 14, 8: 5, 
     9: 6, 10: 5, 11: 5, 12: 2, 13: 3, 14: 3, 15: 5, 
     16: 6, 17: 6, 18: 6, 19: 2, 20: 3, 21: 2, 22: 3, 23: 14, 
     24: 5, 25: 18, 26: 10, 27: 2, 28: 3, 29: 6, 30: 2, 31: 10}

# Initial schedule for Coursework Queston 2.1
x0 = [30, 29, 23, 10, 9, 14, 13, 12, 4, 20, 22, 3, 27, 28, 8, 7, 19, 21, 26, 18, 25, 17, 15, 6, 24, 16, 5, 11, 2, 1, 31]

# Due dates for each node extracted from Appendix A.3
d = {1: 172, 2: 82, 3: 18, 4: 61, 5: 93, 6: 71, 7: 217, 8: 295, 9: 290, 10: 287, 11: 253, 12: 307, 13: 279, 14: 73, 15: 355, 16: 34, 
     17: 233, 18: 77, 19: 88, 20: 122, 21: 71, 22: 181, 23: 340, 24: 141, 25: 209, 26: 217, 27: 256, 28: 144, 29: 307, 30: 329, 31: 269}

# Mean processing times values for each type of job running on Azure, obtained with gettimes.py 
vii = 17.3270
emboss = 2.2013
muse = 13.3265
night = 21.2220
blur = 5.9509
wave = 9.2330
onnx = 3.8556

# Real processing times for each job in the DAG
p_real = {1: onnx, 2: muse, 3: emboss, 4: emboss, 5: blur, 6: emboss, 7: vii, 8: blur, 9: wave, 10: blur, 11: blur, 12: emboss, 13: onnx, 
          14: onnx, 15: blur, 16: wave, 17: wave, 18: wave, 19: emboss, 20: onnx, 21: emboss, 22: onnx, 23: vii, 24: blur, 25: night, 
          26: muse, 27: emboss, 28: onnx, 29: wave, 30: emboss, 31: muse}

# Define maximum neighbourhood generation level for VNS
I = len(x0)
