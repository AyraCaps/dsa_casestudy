from flask import Flask,render_template,request
import pickle
import numpy as np
app= Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method== 'POST':
        gender=request.form['Gender']
        if gender=="Male":
            gender=1
        elif gender=="Female" :
            gender=0
        age=int(request.form['Age'])
        estimated_salary=int(request.form['EstimatedSalary'])
        feature=np.array([[gender,age,estimated_salary]])
        model = pickle.load(open('model (1).pkl','rb'))
        purchased=model.predict(feature)[0]
        if (purchased)==0 :
            purchased='No Purchase'
        elif (purchased)==1 :
            purchased='Purchase'
        print(purchased)

        
    return render_template('prediction.html',purchased=purchased)

if __name__=='__main__':
    app.run()