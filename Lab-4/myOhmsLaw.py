# Ethan Pham        9-25-25        Lab B
# This application stores functions/calculations
def calculateVoltage(c, r):
    # Citation - https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
    # Citation - Author: All About Circuits
    # Citation - Data Published: 4-16-2020
    # Citation - Date Accessed: 9-11-25
    return c * r

def calculateResistence(v,c):
    # Citation - https://courses.lumenlearning.com/suny-physics/chapter/20-3-resistance-and-resistivity/
    # Citation - Author: Lumen Learning
    # Citation - Date Published: 4-25-2023
    # Citation - Date Accessed: 9-11-25
    return v/c

def calculateCurrent(v,r):
    # Citation - https://study.com/skill/learn/how-to-calculate-the-current-in-an-electric-circuit-using-ohms-law-explanation.html#:~:text=Steps%20for%20Calculating%20the%20Current,resistance%20found%20in%20step%201.
    # Citation - Author: Study
    # Citation - Date Published: 3-22-25
    # Citation - Date Accessed: 9-11-25
    return v/r
