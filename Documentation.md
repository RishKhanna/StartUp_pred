# TGS shortlisting 
The following document will contain text explaining the various files found in the repository `StartUp_pred`. 

## File tree
The repository follows this structure:

```
StartUp_pred
├── app.py
├── Documentation.md
├── Procfile
├── PySripts
│   ├── pandas_implementation.py
│   ├── preprocessing.py
│   └── RandomForest_Predict.py
├── README.md
├── requirements.txt
├── runtime.txt
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   └── style.css
│   ├── js
│   │   ├── bootstrap.min.js
│   │   ├── jquery-3.3.1.slim.min.js
│   │   └── popper.min.js
│   └── Model.pkl
└── templates
    ├── base.html
    └── index.html
```

The subdirectories `templates` and `static` control the website structure and UI/UX. They contain html and css files that describe the various components of the website built using flask. 

The central python file that controls the working of the website is `app.py`, which imports and uses flask + the scripts in the folder `PySripts` to run the ML model on the data received from the user. It uses `Flask` and other related libraries to render and host the website. 

## PySripts
The files in the subdirectory `PySripts` are the three python files that encompass the main utility of the website, which is to preprocess the data fed into the website in the `csv` format and predict the success of the enlisted ventures using our pre-trained model. 

- `pandas_implementation.py`: takes input filename and if it posesses filetype: csv, converts it into a `pandas.DataFrame` object for further processing.
- `preprocessing.py`: contains 3 functions that perform normalization (`normalize`), finds if a brief text makes sense (`makes_sense`) and a main function `find_cols` which takes as input the output of `pandas_implementation.py` with columns in the format of the current application form for TGS-TiE 2022, and converts it into a `pandas.DataFrame` object with the columns supported by the model.
- `RandomForest_Predict.py`: imports scikit learn and the stored Random Forest model file that has been trained to a recall of 77.5, precision of 82.0 and F1 score of 85.3. This is then fed with the preprocessed  `pandas.DataFrame` and then the results are shown in the webapp.




