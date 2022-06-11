# @Time : 2022/5/27 20:44
# @Author : Liuyongqian

import pytest,allure

@allure.feature("一级标签")
class TestApi:
    @allure.story("二级标签")
    def test_po1(self,api_login):
        url="http://127.0.0.1:5055/submitViewform"
        headers={
            "Content-Type":"application/json;charset=UTF-8"
        }
        data={
            "productId":"10086",
            "productName":"HiSearch",
            "siteId":"20210318"
        }
        res=api_login.post(url=url,headers=headers,json=data)
        assert res.status_code==200



