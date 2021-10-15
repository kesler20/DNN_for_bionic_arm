import pandas as pd

number_of_gestures = 7
gestures = { '0': 'Clench-Fist', 
'1': 'Spider-Man',
'2': 'Thumb-to-pinky',
'3': 'Wrist-side-to-side-horizontal',
'4': 'Wrist-up-and-down',
'5': 'Wrist-rotate-inwards',
'6': 'Wrist-side-to-side-vertical',
'7': 'Pointer-finger'}

#import all the data
data0 = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\data_final-mark_emgData-G0.csv')
data1 = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\data_final-mark_emgData-G1.csv')
data2 = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\data_final-mark_emgData-G2.csv')
data3 = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\data_final-mark_emgData-G3.csv')
data4 = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\data_final-mark_emgData-G4.csv')
data5 = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\data_final-mark_emgData-G5.csv')
data6 = pd.read_csv(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\data_final-mark_emgData-G6.csv')

classes_data0 = []
for i in range(len(data0)):
    classes_data0.append(0)

classes_data1 = []
for i in range(len(data1)):
    classes_data1.append(1)

classes_data2 = []
for i in range(len(data2)):
    classes_data2.append(2)

classes_data3 = []
for i in range(len(data3)):
    classes_data3.append(3)

classes_data4 = []
for i in range(len(data4)):
    classes_data4.append(4)

classes_data5 = []
for i in range(len(data5)):
    classes_data5.append(5)

classes_data6 = []
for i in range(len(data6)):
    classes_data6.append(6)

data0['Classes'] = pd.DataFrame(classes_data0)
data1['Classes'] = pd.DataFrame(classes_data1)
data2['Classes'] = pd.DataFrame(classes_data2)
data3['Classes'] = pd.DataFrame(classes_data3)
data4['Classes'] = pd.DataFrame(classes_data4)
data5['Classes'] = pd.DataFrame(classes_data5)
data6['Classes'] = pd.DataFrame(classes_data6)

big = data0.append(data1)
data = data2.append(data3)
big_data = big.append(data)
t = data4.append(data5)
g = big_data.append(t)
p = g.append(data6)
p = p.fillna(0)

p.replace('Repeat 1', 0, inplace=True)
p.replace('Repeat 2', 0, inplace=True)
p.replace('Repeat 3', 0, inplace=True)
p.replace('Repeat 4', 0, inplace=True)
p.replace('Repeat 5', 0, inplace=True)
p.replace('Repeat 6', 0, inplace=True)
p.replace('Repeat 7', 0, inplace=True)
p.replace('Repeat 8', 0, inplace=True)
p.replace('Repeat 9', 0, inplace=True)
p.replace('Repeat 10', 0, inplace=True)
p.replace('Repeat 11', 0, inplace=True)
p.replace('Repeat 12', 0, inplace=True)
p.replace('Repeat 13', 0, inplace=True)

p.to_excel('clean_data_mark.xlsx')