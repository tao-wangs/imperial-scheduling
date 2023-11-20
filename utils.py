import csv


def checkFeasibility(DAG, x, swap_idx):
    """
    Checks that the adjacent interchange indexes being considered does not violate precendence rules. 

    Inputs:
        DAG        -- A dictionary representing the incidence matrix of the directed acyclic graph
        x          -- A list representing a schedule 
        swap_idx   -- Starting index of adjacent interchange indices (swap_idx, swap_idx+1) 

    Outputs:
        A boolean value for whether the edge is not in the directed acyclic graph.
    """
    
    return (x[swap_idx], x[swap_idx+1]) not in DAG


def calculateTotalTardiness(x, params):
    """
    Given a schedule x and list of processing times and due dates, 
    calculates the total tardiness of the schedule.

    Inputs:
        x       -- A list representing a schedule 
        params  -- A list of parameters containing processing times and due dates of nodes

    Outputs:
        T_sum   -- Total tardiness
    """

    p, d = params[0], params[1]
    C_i = 0
    T_sum = 0

    for i in range(len(x)):
        C_i += p.get(x[i])
        T_sum += max(0, C_i - d.get(x[i]))

    return T_sum


def convertScheduleToCSV(filename, schedule):
    """
    Given a list representing a schedule, converts schedule to a csv file.

    Inputs:
        filename  -- String representing the name of the .csv file 
        schedule  -- A list of integers representing the schedule 
    """

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(schedule)
