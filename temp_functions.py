"""This script file includes two functions that can convert temperature values from Fahrenheit to Celsius degrees
and classify temperatures given in Celsius degrees. """

def fahr_to_celsius(temp_fahrenheit):
    """ 
    This function converts temperature given in Fahrenheit to Celsius. 
    Function has 1 parameter which is the temperature in Fahrenheit and 
    it returns temperature in Celsius.


    Parameters
    ---------
    temp_fahrenheit: <numerical>
        Temperature in Fahrenheit

    Returns
    -------
    <float>
        Temperature in Celsius
    
    """
    
    # Here converted temperature is stored in a variable inside the function
    converted_temp = (temp_fahrenheit - 32) / 1.8
    
    # This row returns the converted value
    return converted_temp



def temp_classifier(temp_celsius):
    """
    This function allows you to classify temperatures given in Celsius degrees. 

    Parameters
    ---------
    temp_celsius: <numerical>
        Temperature in Celsius

    Returns
    -------
    <int>
        Class value as integer number

    """
    # The value of temp_celsius is classified in needed conditional statements which return a number identifying the class
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    elif temp_celsius >= 15:
        return 3
