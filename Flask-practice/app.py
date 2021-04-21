from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')                   #// 기본주소로 접속되었을 때 실행할 함수 지정
def hello():
    return 'Hello world'

@app.route('/about')             #// '/about'으로 접속되었을 때 실행할 함수 지정
def about():
    return 'This is about page'

@app.route('/contact')          #'/contact'으로 접속되었을 때 실행할 함수 지정
def contact():
    return 'This is contact page'

@app.route('/test') 
def index():
  return render_template('index.html',user="최종환",data={'temper':str(17)+"'C",'humidity':str(30)+"%",'dust':str(10)+"um"})

if __name__ == '__main__':         # //웹서버 구동
    app.run(debug=True)