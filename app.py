from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from models import User, query_user



import random
import get_data
from get_data import df, never_list

app = Flask(__name__)
app.secret_key = '1234567'



login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = '请登录'
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id

        return curr_user


@app.route('/',methods=['GET','POST'])
@login_required
def index():
    nameid = current_user.get_id()
    one=get_one()
    question, answer, belong, pages ,count= get_question(one)
    # "清理"
    question=str(question).replace(" ","")
    question=question.replace("：","：\n")
    question=question.replace("；","；\n")
    answer=str(answer).replace(" ","")
    belong=str(belong).replace("","")

    return render_template('webtest.html',
                           titles=question,
                           answers=answer,
                           fromes=belong,
                           pages=pages,
                           name=nameid,
                           countsum=countsum,
                           countnow=count,
                           count_know=count_know,
                           )  # 从templates中找到
    # return 'Logged in as: %s' % current_user.get_id()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userid')
        user = query_user(user_id)
        if user is not None and request.form['password'] == user['password']:
            curr_user = User()
            curr_user.id = user_id

            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)

            return redirect(url_for('index'))

        flash('Wrong username or password!')

    # GET 请求
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')


# ============> 后台
# 数据常量
neverfile = 'neverlook.csv'
# 原始长度
countsum = get_data.count_lines

# 用不看题号
never_num = len(never_list)
never_look_list = never_list
count_know=len(never_look_list)
# 用于记录本次看了多少题
count = len(never_list)
# index的列表
keys = get_data.index_list
keys = [item for item in keys if item not in never_look_list]


def get_question(num):
    global count
    count += 1
    question = df.loc[num, ['题干'][0]]
    answer = df.loc[num, ['答案'][0]]
    belong = df.loc[num, ['出处'][0]]
    pages = df.loc[num, ['页码'][0]]
    if str(pages) == "nan": pages = "page记录为空"
    print(question, answer, belong, pages)
    return question, answer, belong, pages,count


def get_one():
    global never_num,keys
    one = random.sample(keys, 1)[0]
    keys.remove(one)  #保证绝对不会重复
    print(len(keys))
    never_num = one
    # print("选择的:", one)
    # with open(neverfile, 'a+') as neverdf:
    #     neverdf.writelines(str(never_num) + '\n')
    return one


def never_add():
    global never_num,count_know
    if never_num not in never_look_list:
        never_look_list.append(never_num)
        print("不再看的加入新的后:", never_look_list)
        count_know = len(never_look_list)
        print("加入成功:",count_know)
    else:
        pass


def clean_csv():
    global never_look_list,count_know

    with open(neverfile, 'w') as neverdf:
        neverdf.writelines('')
    never_look_list = []
    count_know = len(never_look_list)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
    # app.run(host = '0.0.0.0')
