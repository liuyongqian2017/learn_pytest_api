# @Time : 2022/5/27 20:30
# @Author : Liuyongqian

import requests,pytest

@pytest.fixture(scope="class",autouse=False)
def api_login():
    session=requests.session()
    url="http://127.0.0.1:5055/login"
    data={
        "uname":"liuyongqian",
        "pword":"123456"
    }
    res=session.post(url=url,data=data)
    session.headers.update({"cookie":res.json()["cookie"]})
    yield session






