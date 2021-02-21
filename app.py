import os
import xlrd
import pickle
import openpyxl
import numpy as np
from flask import Flask, render_template
from flask import request, jsonify
from werkzeug.utils import secure_filename


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict',methods=['GET', 'POST'])
def home():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        f = request.files['file']
        f.filename = 'patient_data.xlsx'
        f.save(secure_filename(f.filename))
        # return 'file uploaded successfully'

    path = 'patient_data.xlsx'
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    # print(sheet_obj.cell(row = 2, column = 1).value)
    
    d1 = sheet_obj.cell(row = 2, column = 2).value
    d2 = sheet_obj.cell(row = 2, column = 3).value
    d3 = sheet_obj.cell(row = 2, column = 4).value
    d4 = sheet_obj.cell(row = 2, column = 5).value
    d5 = sheet_obj.cell(row = 2, column = 6).value
    d6 = sheet_obj.cell(row = 2, column = 7).value
    d7 = sheet_obj.cell(row = 2, column = 8).value
    d8 = sheet_obj.cell(row = 2, column = 9).value
    d9 = sheet_obj.cell(row = 2, column = 10).value
    d10= sheet_obj.cell(row = 2, column = 11).value
    d11= sheet_obj.cell(row = 2, column = 12).value
    d12= sheet_obj.cell(row = 2, column = 13).value
    d13= sheet_obj.cell(row = 2, column = 14).value
    d14= sheet_obj.cell(row = 2, column = 15).value
    d15= sheet_obj.cell(row = 2, column = 16).value
    d16= sheet_obj.cell(row = 2, column = 17).value
    d17= sheet_obj.cell(row = 2, column = 18).value
    d18= sheet_obj.cell(row = 2, column = 19).value
    d19= sheet_obj.cell(row = 2, column = 20).value
    d20= sheet_obj.cell(row = 2, column = 21).value
    arr=np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20]])

    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    prediction = model.predict(arr)

    output = prediction[0]
    if output==0:
        print("Chemotherapy Not Suitable")
    else:
        print("Chemotherapy Suitable")
    return render_template('home.html', data=prediction, prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
