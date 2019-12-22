from flask import Flask,jsonify,request
import run_test
import requests
import json
import bs4
app = Flask(__name__)#创建一个服务，赋值给APP

@app.route('/get_file',methods=['post'])#指定接口访问的路径，支持什么请求方式get，post

#json方式传参
def get_ss():
    articleid = request.json.get('id')#获取带json串请求的username参数传入的值
    url = r"http://39.106.54.106:8080/Entity/U47b03b310e54f0/tournote2/Article/" + articleid
    t = requests.get(url)
    a = json.loads(t.content)
    content = bs4.BeautifulSoup(a['content']).getText()
    num = run_test.get_score(content)
    a['score'] = str(num)
    print(a)
    requests.put(url, a)

#如果不在的话，返回err对应key的value转成的json串信息

app.run(host="0.0.0.0",port=5000,debug=True)