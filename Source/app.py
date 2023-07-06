#pandas to data extraction 
import pandas as pd

# matplot for ploting the data into the graph
import matplotlib.pyplot as plt


cyclone_data_file = 'data.xlsx'

# readign the excel file 
cyclone = pd.read_excel(cyclone_data_file)


# Convert timestamp column to datetime
cyclone['time'] = pd.to_datetime(cyclone['time'])

# Define abnormality criteria
abnormal_threshold = 2  # Number of standard deviations from the mean

# converting non-numeric data type to numeric types dataset using data.dtypes (pd.to_numeric)

cyclone['Cyclone_Inlet_Gas_Temp'] = pd.to_numeric(cyclone['Cyclone_Inlet_Gas_Temp'], errors='coerce')
cyclone['Cyclone_Gas_Outlet_Temp'] = pd.to_numeric(cyclone['Cyclone_Gas_Outlet_Temp'], errors='coerce')
cyclone['Cyclone_Outlet_Gas_draft'] = pd.to_numeric(cyclone['Cyclone_Outlet_Gas_draft'], errors='coerce')
cyclone['Cyclone_cone_draft'] = pd.to_numeric(cyclone['Cyclone_cone_draft'], errors='coerce')
cyclone['Cyclone_Inlet_Draft'] = pd.to_numeric(cyclone['Cyclone_Inlet_Draft'], errors='coerce')
cyclone['Cyclone_Material_Temp'] = pd.to_numeric(cyclone['Cyclone_Material_Temp'], errors='coerce')




# Iterate over each variable
variables = ['Cyclone_Inlet_Gas_Temp', 'Cyclone_Gas_Outlet_Temp', 'Cyclone_Outlet_Gas_draft',
             'Cyclone_cone_draft', 'Cyclone_Inlet_Draft', 'Cyclone_Material_Temp']


for var in variables:
    # Calculate mean and standard deviation
    mean = cyclone[var].mean()
    std = cyclone[var].std()

    # Identify abnormal periods
    abnormal_periods = cyclone[(cyclone[var] > mean + (abnormal_threshold * std)) | 
                            (cyclone[var] < mean - (abnormal_threshold * std))]
    
    # Plot the variable over time with abnormal periods highlighted
    plt.figure(figsize=(10, 6))
    plt.plot(cyclone['time'], cyclone[var], color='blue', label=var)
    plt.scatter(abnormal_periods['time'], abnormal_periods[var], color='red', label='Abnormal')
    plt.xlabel('time')
    plt.ylabel(var)
    plt.title(f'{var} with Abnormal Periods')
    plt.legend()
    plt.show()
