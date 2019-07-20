# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask import url_for
app=Flask(__name__)

name = 'liangwei'
movies = [
    
{"index": "1", "image": "http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c", "title": "霸王别姬", "actor": "张国荣,张丰毅,巩俐", "time": "1993-01-01(中国香港)", "score": "9.6"},
{"index": "2", "image": "http://p0.meituan.net/movie/__40191813__4767047.jpg@160w_220h_1e_1c", "title": "肖申克的救赎", "actor": "蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿", "time": "1994-10-14(美国)", "score": "9.5"},
{"index": "3", "image": "http://p0.meituan.net/movie/23/6009725.jpg@160w_220h_1e_1c", "title": "罗马假日", "actor": "格利高利·派克,奥黛丽·赫本,埃迪·艾伯特", "time": "1953-09-02(美国)", "score": "9.1"},
{"index": "4", "image": "http://p0.meituan.net/movie/fc9d78dd2ce84d20e53b6d1ae2eea4fb1515304.jpg@160w_220h_1e_1c", "title": "这个杀手不太冷", "actor": "让·雷诺,加里·奥德曼,娜塔莉·波特曼", "time": "1994-09-14(法国)", "score": "9.5"},
{"index": "5", "image": "http://p0.meituan.net/movie/11/324629.jpg@160w_220h_1e_1c", "title": "泰坦尼克号", "actor": "莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩", "time": "1998-04-03", "score": "9.5"},
{"index": "6", "image": "http://p0.meituan.net/movie/92/8212889.jpg@160w_220h_1e_1c", "title": "教父", "actor": "马龙·白兰度,阿尔·帕西诺,詹姆斯·凯恩", "time": "1972-03-24(美国)", "score": "9.3"},
{"index": "7", "image": "http://p0.meituan.net/movie/99/678407.jpg@160w_220h_1e_1c", "title": "龙猫", "actor": "日高法子,坂本千夏,糸井重里", "time": "1988-04-16(日本)", "score": "9.2"},
{"index": "8", "image": "http://p0.meituan.net/movie/62/109878.jpg@160w_220h_1e_1c", "title": "唐伯虎点秋香", "actor": "周星驰,巩俐,郑佩佩", "time": "1993-07-01(中国香港)", "score": "9.2"},
{"index": "9", "image": "http://p0.meituan.net/movie/9bf7d7b81001a9cf8adbac5a7cf7d766132425.jpg@160w_220h_1e_1c", "title": "千与千寻", "actor": "柊瑠美,入野自由,夏木真理", "time": "2001-07-20(日本)", "score": "9.3"}

]



@app.route('/index/')
def index():
  return render_template('index.html',name=name,movies=movies)

 
@app.route('/')
def hello():
  return 'ssssss'
 

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0',port=80)
