import csv


def calculateTotalTardiness(x, params):
    """
    Given a schedule x and list of processing times and due dates, 
    calculates the total tardiness of the schedule.

    Inputs:
        x           -- A list representing a schedule 
        params      -- A list of parameters containing processing times and due dates of nodes

    Outputs:
        T_sum       -- Total tardiness
    """

    p = params[0]
    d = params[1]

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
        filename    -- String representing the name of the .csv file 
        schedule    -- A list of integers representing the schedule 
    """

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(schedule)
