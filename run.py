import time
import unittest
from HTMLTestReportCN import HTMLTestRunner
from Libs.tools import (
    InsertLog,
    GetNewReport,
    SendEmail
)
from config.secert import (
    email_account,
    email_pwd,
    email_host,
    email_port,
    email_to_account,
)

def run_test():
    try:
        dirpath = './scripts'
        discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')
        currenttime = time.strftime('%y%m%d%H%M%S')
        filedir = './reports/' + 'report_' + currenttime + '.html'
        with open(filedir, 'wb') as fp:
            runner = HTMLTestRunner(stream=fp,
                                    title='Edu自动化测试报告',
                                    description='Edu在线教育平台V1.2自动化测试报告',
                                    tester="测试大神",verbosity=2)
            runner.run(discover)
        f = GetNewReport()
        SendEmail(s_user=email_account,s_pwd=email_pwd,port=email_port,
                  host=email_host,report_file=f,to_user=email_to_account,subject='自动化测试报告',body='老板这是今天的自动化报告，麻烦看看')
        print('发送邮件成功')
    except BaseException as msg:
        log = InsertLog()
        log.error(msg)


if __name__ == '__main__':
    run_test()
