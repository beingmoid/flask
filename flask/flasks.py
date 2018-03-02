from flask import Flask,requst,render_template
app=Flask(__name__)
@app.route('/send',methods=['GET','POST'])
def send():
    if request.method=='get':
        age=request.form['age']
        return render_template('age.html',age=age)
    else:
        return render_template('age.html', age=age)

    return render_template('HOME.html')
if __name__=="__main__":
    app.run()