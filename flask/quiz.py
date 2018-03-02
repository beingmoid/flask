from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def index():
    return 'this is homepage'
@app.route('/tuna')
def tuna():
    return '<h1> tuna is good</h1>'
@app.route('/username/<username>')
def profile(username):
    return 'Hello %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h1>Post Id is %s</h1>' % post_id
@app.route('/method')
def showMethod():
    return 'This Methid is %s'% request.method
@app.route('/bacon',methods=['GET','POST'])
def bacon():
    if request.method=='GET':
        return 'You are using GET'
    else:
        return 'You are probably using POST'
def showMethod():
    return 'This Methid is %s'% request.method


if __name__=="__main__":
    app.run(debug=True) 

