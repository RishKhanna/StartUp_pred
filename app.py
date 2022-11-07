from flask import Flask, render_template, request, send_file
import pandas as pd
from PySripts.preprocessing import *
from PySripts.pandas_implementation import *
from PySripts.RandomForest_Predict import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		# input file
		f = request.files['file']
		# decodes utf-8 into a python string 
		decoded = f.read()
		# Converts the string into a Pandas DataFrame
		Data_extracted = input_to_df(decoded, f.filename)
		del f

		# Returns a Warning if the DataFrame is empty, given all input conditions 
		if(len(Data_extracted)==0):
			return render_template("index.html", incorrect_file_type=1)
		
		# Preprocessing the input data to fit in our model.
		name_col = Data_extracted["Startup Name"]
		Data_extracted = find_cols(Data_extracted)

		# Now we have data processed such that we can use it for prediction.
		Data_extracted['Predict'] = RF_Predict(Data_extracted)
		Data_extracted["Company Name"] = pd.DataFrame(name_col)

		# Update index.html to show few rows of the DataFrame and to allow downloading the 
		# generated csv file of outputs.
		output_df = Data_extracted[["Company Name", "Predict"]]
		output_df.to_csv("./static/result.csv", index=False)
		print(output_df.head())
		return render_template('index.html', result_after_pred=1,tables=[output_df.to_html(classes='data')], titles=output_df.columns.values)
		# return render_template('index.html', result_after_pred=1, file ='/static/result.csv')

@app.after_request
def add_header(response):
	"""
		Add headers to both force latest IE rendering engine or Chrome Frame,
		and also to cache the rendered page for 10 minutes.
		"""
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response


@app.route('/download')
def download_file():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./static/result.csv"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
	app.run(debug=True)
