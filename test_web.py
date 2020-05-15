

login_id={
    'donghuibiao':'123456',
    'gaohao':'123456',
}

def login():
    while True:
        username= input("输入账号")
        password= input('输入密码')
        if password != login_id[username]:
            print('密码不对')
        elif password == login_id[username]:
            print('登录成功')
            break
        else:
            print('未注册')

def log_up():
    while True:
        username_get=input('设定您的账号')
        if username_get in login_id: 
            print('youle')
            continue
        password_get=input("设定您的密码")
        login_id[username_get]=password_get
        print('设置成功')
        break

if __name__=='__main__':
    
    login()