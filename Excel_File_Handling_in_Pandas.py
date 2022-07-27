import pandas as pd
data_frame = pd.read_excel('Family_info.xlsx')       # Reading an Excel file  in pandas
data_frame.to_excel('New_family.xlsx', index=False)   # writing an Excel file in pandas


