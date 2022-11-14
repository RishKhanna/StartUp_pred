import pandas as pd
from io import StringIO, BytesIO

def input_to_df(input, filename):
	"""	
		-----
	"""
	type_input = filename.split(".")[-1]
	if type_input=="csv":
		df = pd.read_csv(StringIO(input.decode('utf-8')), sep=",")
	# elif type_input=="xlsx":
	# 	df = pd.read_excel(BytesIO(input))
	else:
		df = pd.DataFrame()
	return df
