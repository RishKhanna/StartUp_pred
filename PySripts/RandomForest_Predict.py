import pandas as pd
import pickle as pkl

def RF_Predict(in_df):
	X = ['Website Link', 'App Link', 'Team Size', 'revenue slab',
	   'VC funded', 'Angle funding / Seed funding', 'B2B', 'Crowd funded', 'Bootstrapped',
	   'Product is not live yet', 'B2C', 'C2C', 'B2B2C', 'Govt. funded', "[Traction] app downloads",
	   'Bank funded / Loan', 'Incubator/Accelerator funded', "[Traction] # user",
	   'Collected from worksheet',"[Traction] Less than 2" ,"[Brief] word count", 
	    "[Traction] More than 2","[Traction] makes sense"]
	model = pkl.load(open("./static/Model.pkl",'rb'))
	fin = model.predict(in_df[X])
	fin = ["Yes" if i==1 else "No" for i in fin]
	return fin