from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

USER={
    1:{'name':'黄凯文','gender':'女','city':'马鞍山'},
    2:{'name':'刘永亮','gender':'男','city':'芜湖'},
    3:{'name':'陈秦昊','gender':'女','city':'南京'},
    4:{'name':'李四','gender':'男','city':'苏州'},
    5:{'name':'张三','gender':'女','city':'青岛'},
    6:{'name':'王五','gender':'女','city':'苏州'},
} #这本身就就是一个字典里嵌套字典的 字典，只是 values 又是一个字典

app = Flask(__name__)

@app.route('/')
def home():
    user_list=[]
    for uid,info in sorted(USER.items()):
        item = [uid,info['name']]
        user_list.append(item)

    return render_template('home.html',user_list=user_list)


@app.route('/user/info')           #为啥要用？id= 某个值啊，因为你请求服务器的时候，徐=需要这些值，并且服务器里面需要几个就要传几个
def user_info():
    uid=int(request.args.get('id'))
    user_data=USER[uid]
    return render_template('info.html',user=user_data,uid=uid)

@app.route('/menu')
def menu():
    menu_items=['酸菜鱼','土豆丝','毛血旺','炸猪排','水煮肉片','蒜泥生菜']
    return render_template('menu.html',menu_items=menu_items)

@app.route('/user/update',methods=('POST','GET'))  #这是啥的呢，就是修改信息时会向服务器请求的
def update():
    # 以下整个是表单提交信息，服务器收集的过程
    if request.method == 'POST':
        uid = int(request.form.get(uid)) #用户ID

        info = {
            'name':request.form.get('name'),
            'gender':request.form.get('gender'),
            'city':request.form.get('city')
        }

        USER[uid].update(info)
        print('0822 修改测试-2')
        print('使用 vigor2 进行了修改')
        print('使用 vigor1 进行了修改')
        return redirect('/user/info?id=%s' % uid)

    else:
        uid=int(request.args.get('uid'))  #外面传的uid进来的，就是我们在浏览器中填写的，到了服务器根据id 去掉相应用户信息
        user_data = USER[uid]  #字典 通过字典的键 获得了 字典对应的值，那么现在这个user_data 也是一个字典
        return render_template('update.html',user=user_data,uid=uid)  #将user_data 赋值给了 user,并且以user 传到了 update.html
        #在某个地方点击修改信息申请后，要展示的页面，页面里面有啥东西要到 update.html 去配置

if __name__ == '__main__':
    app.run(host='10.11.52.59',port='5000')







