from Libs.tools import BaseHttp
from config.secert import host

# 公共业务登录类继承了BaseHttp
class LoginClass(BaseHttp):
    # 定义一个空的字典数据
    cookies = {
        'PHPSESSID': ''
    }

    # 封装公共业务模块
    def loginApi(self):
        # 登录接口
        lgn_path = '/index.php?ctl=user&act=dologin'
        # 登录数据
        lgn_data = {
            'email': 'woshinin001',
            'user_pwd': 'QUhGV0p2WnBhdExZVlVDaFdHak5Wc1JuRE9md0hlTEFsbklvY0tRU01hQU51ZnhNZFYlMjV1NjVCOSUyNXU3RUY0c2YxMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
            'ajax': 1,
        }
        # 发送登录请求
        lgn_result = self.sendHttp(path=lgn_path, data=lgn_data)

        # 登录成功后从响应结果获取cookies
        phpid = lgn_result.cookies['PHPSESSID']

        # 为上面的类变量cookies更新其数据
        self.cookies['PHPSESSID'] = phpid

        return lgn_result

