# import packages
import pandas as pd

# load in data 
# convert .txt to .csv 
adi = pd.read_csv('US_2019_ADI_Census Block Group_v3.1.txt')
adi.to_csv ('US_2019_ADI_Census Block Group_v3.1.txt', index=None)
# renamed filed to convert to csv 
adi1 = adi.astype(str)

discharges = pd.read_csv('Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
discharges1 = discharges.astype(str)

# get a list of colum names 
list(discharges.columns)
list(adi.columns)

# to make data smaller for merge 
discharges_simple = discharges1['Zip Code - 3 digits']
adi_simple = adi1[['FIPS']]

adi_small = adi[['GISJOIN', 'FIPS', 'ADI_NATRANK', 'ADI_STATERNK']]
print(adi_small.sample(10).to_markdown())

discharges_small = discharges[['Health Service Area', 'Hospital County', 'Facility Id', 'Facility Name', 'Zip Code - 3 digits', 'Total Charges', 'Total Costs']]
print(discharges_small.sample(10).to_markdown())

# merge datasets
combined_df = discharges_simple.merge(discharges_small, adi_small, how= 'left', left_on='FIPS', right_on='Zip Code - 3 digits')

# attribute error with merge so used pd instead
combined_df = pd.merge(discharges_small, adi_small, how= 'left', left_on='FIPS', right_on='Zip Code - 3 digits')