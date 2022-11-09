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
	# fin = ["Yes" if i==1 else "No" for i in fin]
	return fin



def Scoring_top3(in_df):
	"""
	prediction: 33.33%
	Top3 features: B2C + Bootstrap + Wordcount = 66.66%
	"""
	fin_score = []
	# normalise word count
	max_count = max(in_df["[Brief] word count"])
	in_df["[Brief] word count"] = in_df["[Brief] word count"]/max_count
	for index, i in in_df.iterrows():
		score = int(i["Predict"])/3
		score += (int(i["B2B"]) + int(i["Bootstrapped"]) + int(i["[Brief] word count"]))*(2/9)
		fin_score.append(score)
	in_df["Score"] = fin_score
	return in_df[["Company Name", "Predict", "Score"]]
