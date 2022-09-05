import pytest,allure,os
class TestClass001:
    @allure.feature("用户登录功能")#用于定义被测试的功能，被测产品的需求点
    @allure.story("登录成功")     #用于定义被测功能的用户场景，即子功能点
    def testsuccess(self):
        print("--test1--")
        assert 1==1
    @allure.feature("用户登录功能")#用于定义被测试的功能，被测产品的需求点
    @allure.story("登录失败")     #用于定义被测功能的用户场景，即子功能点
    def testfail(self):
        print("--test2--")
        assert 1==2
if __name__ == '__main__':
   # pytest.main(["--html=./report4.html", "Test_A.py::TestClass001"])
    #os.system('allure generate ./temp -o ./report --clean')
    pytest.main(['--alluredir', 'report/result', 'Test_A.py'])  #生成json类型的测试报告
    split = 'allure ' + 'generate ' + './report/result ' + '-o ' + './report/html ' + '--clean'  #将测试报告转为html格式
    os.system(split)  # system函数可以将字符串转化成命令在服务器上运行
   #pytest.main(["-s","-v","--html=Outputs/test_report/pytest.html","--alluredir=Outputs/allure"])
