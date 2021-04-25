from flask import Flask, request, render_template, jsonify
import json
app = Flask(__name__,template_folder='./')
# template_folder='./'

# 新增一個route


# 動態路由
@app.route('/' )
def hello():
    return render_template('form.html')

@app.route('/process',methods=['POST','GET'])
def process():
    # data = request.values.get['name']
    data = request.values.to_dict()
    return json.dumps(
        data,ensure_ascii=False) 

#如何換成dir格式,一次得到所有值


