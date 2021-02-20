import numpy as np
from flask import Flask, render_template
from flask import request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def home():
    '''
    For rendering results on HTML GUI
    '''
    d1= request.form['a']
    d2= request.form['b']
    d3= request.form['c']
    d4= request.form['d']
    d5= request.form['e']
    d6= request.form['f']
    d7= request.form['g']
    d8= request.form['h']
    d9= request.form['i']
    d10= request.form['j']
    d11=request.form['k']
    d12= request.form['l']
    d13= request.form['m']
    d14= request.form['n']
    d15= request.form['o']
    d16= request.form['p']
    d17= request.form['q']
    d18= request.form['r']
    d19= request.form['s']
    d20= request.form['t']
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
