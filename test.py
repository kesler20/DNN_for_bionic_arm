import sklearn
import pandas as pd
import numpy as np
import serial 
from sklearn.neighbours import KNeighboursClassifier
import math

def create_serial_obj(portPath, baud_rate, tout):
    """
    Given the port path, baud rate, and timeout value, creates
    and returns a pyserial object.
    """
    return serial.Serial(portPath, baud_rate, timeout = tout)
    
def read_serial_data(serial):
    """
    Given a pyserial object (serial). Outputs a list of lines read in
    from the serial port
    """
    serial.flushInput()
    
    serial_data = []
    readings_left = True
    timeout_reached = False
    
    while readings_left and not timeout_reached:
        serial_line = serial.readline()
        if serial_line == '':
            timeout_reached = True
        else:
            serial_data.append(serial_line)
            if len(serial_data) == max_num_readings:
                readings_left = False
        
    return serial_data
        
def clean_serial_data(data):
    """
    Given a list of serial lines (data). Removes all characters.
    Returns the cleaned list of lists of digits.
    Given something like: ['0.5000,33\r\n', '1.0000,283\r\n']
    Returns: [[0.5,33.0], [1.0,283.0]]
    """
    clean_data = []
    
    for line in data:
        line_data = re.findall("\d*\.\d*|\d*",line) # Find all digits
        line_data = [float(element) for element in line_data if is_number(element)] # Convert strings to float
        if len(line_data) >= 2:
            clean_data.append(line_data)
 
    return clean_data           

def gen_col_list(num_signals):
    """
    Given the number of signals returns
    a list of columns for the data.
    E.g. 3 signals returns the list: ['Time','Signal1','Signal2','Signal3']
    """
    col_list = ['Time']
    for i in range(1,num_signals+1):
        col = 'Signal'+str(i)
        col_list.append(col)
        
    return col_list 

def save_to_csv(data, filename):
    """
    Saves a list of lists (data) to filename
    """
    with open(filename, 'wb') as csvfile:
        csvwrite = csv.writer(csvfile)
        csvwrite.writerows(data)

def OutputSignal:
    def __init__(self, amplitude, frequency):
        self.amplitude = amplitude
        self.frequency = frequency

    def conversion(output_signal):
        converted_output = []
        for I in output_signal:
            respones = math.sin(I)
            converted_output.append(response)

def find_max(lists):
    new_higher_value = 0
    for item in lists:
        if item > new_higher_value:
            new_higher_value = item

    print(new_higher_value)

  
#remember to initialize number of signals 
#initialize features which correspond to the inputs 
#initialize classes that correspond to the output
num_signals = 1
serial = create_serial_obj()
data = clean_serial_data(read_serial_data(serial))
gen_col_list(num_signals)
save_to_csv(data, test_sample)
# train a knn model with some sample data first save it to a file

feature_columns = ['Signal0']
for item in range(0, num_signals):
    Xin = 'Signal'+ str(item)
    feature_columns.append(Xin)

data = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\test_sample')
X = data.loc[:, feature_columns])
Y = data.loc[:, ['Signal'+ str(len(feature_columns))]]

output = OutputSignal()
test_data = output.conversion(X)
max_valhue = find_max(test_data)
for item in test_data:
    if float(item) => 0.85 * max_value:
        print('flexing')
    else:
        print('''I did not feel anything''')
   
