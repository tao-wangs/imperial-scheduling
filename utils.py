from constants import *  
import csv


def calculateTotalTardiness(x, params):
    """
    Given a schedule x and list of processing times and due dates, 
    calculates the total tardiness of the schedule. 
    """

    p = params[0]
    d = params[1]

    C_i = 0
    T_sum = 0
    for i in range(len(x)):
        C_i += p.get(x[i])
        T_sum += max(0, C_i - d.get(x[i]))

    return T_sum


def convertListToCSV(filename, integer_list):
    """
    Given a schedule of jobs as a list, converts schedule to a csv file.
    """

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(integer_list)


