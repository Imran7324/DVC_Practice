import pandas as pd
import os
data={
    "Name":['Max','Mac','Matt'],
    "Age":[24,25,26],
    "City":["Delhi","Nagpur","Bhopal"]
}
df=pd.DataFrame(data)
#Adding new row to df for v2(data version 2)
new={
    "Name":"Lily",
    "Age":26,
    "City":"Noida"
}
new1={
    "Name":"Nina",
    "Age":28,
    "City":"Gurgaon"
}
df.loc[len(df.index)]=new
df.loc[len(df.index)]=new1
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"CSV file saved to {file_path}") 