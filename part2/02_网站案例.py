class LoginPage:
    def __init__(self,name,password,code):
        self.usarname =name
        self.password =password
        self.code=code
        self.btn='登录'
    def login(self):
        print(f'请输入用户名：{self.usarname}')
        print(f'请输入密码：{self.password}')
        print(f'请输入验证码：{self.code}')
        print(f'点击登录按钮{self.btn}')
login=LoginPage('admin','123456','1234')
login.login()


