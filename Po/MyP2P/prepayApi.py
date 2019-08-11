from Libs.business import LoginClass


# 使用业务类的管理业务
class PrepayClass(LoginClass):

    # 线下充值Api
    def prepayApi(self):

        # 调用登录
        self.loginApi()

        # 线下支付
        prepay_path = '/member.php?ctl=uc_money&act=incharge_done'

        # 线下充值需要的参数
        prepay_data = {
            'check_ol_bl_pay': 'on',
            'money': '1234567',
            'pingzheng': '',
            'memo': '777771',
            'payment': '5',
            'bank_id': '0',
        }
        prepay_result = self.sendHttp(path=prepay_path, data=prepay_data, cookies=self.cookies)
        return prepay_result






