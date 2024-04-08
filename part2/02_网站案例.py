class LoginPage:
    """
    登录页面类，用于模拟登录过程。

    参数:
    - name: 用户名
    - password: 密码
    - code: 验证码

    属性:
    - btn: 登录按钮的文本，默认为'登录'
    """
    def __init__(self, name, password, code):
        self.usarname = name  # 用户名
        self.password = password  # 密码
        self.code = code  # 验证码
        self.btn = '登录'  # 登录按钮文本

    def login(self):
        """
        执行登录操作，模拟输入用户名、密码、验证码并点击登录按钮的过程。
        """
        print(f'请输入用户名：{self.usarname}')  # 显示用户名
        print(f'请输入密码：{self.password}')  # 显示密码
        print(f'请输入验证码：{self.code}')  # 显示验证码
        print(f'点击登录按钮{self.btn}')  # 显示登录按钮提示

# 创建登录页面实例并执行登录操作
login = LoginPage('admin', '123456', '1234')
login.login()

