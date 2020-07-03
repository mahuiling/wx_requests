import requests


def test_token():
    # 获取 token
    corpid = "wwe653983e4c732493"
    corpsecret = "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return res.json()["access_token"]

def test_get():
    # 根据 id查询部门列表
    #res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token()}&userid=zhangsan")
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}")
    print(res.json())
    assert res.json()["errcode"] == 0

def test_creatdepartment():
    #创建部门
    data ={
        "name": "VR研发中心12",
        "name_en": "VRGZ12",
        "parentid": 1,
        "order":1
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}",json=data)
    print(res.json())

def test_updatedepartment():
    # 更新部门
    data = {
        "id": 2,
        "name": "VR研发中心",
        "name_en": "VRGZ",
        "parentid": 1,
        "order": 1
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}",json=data)
    print(res.json())

def test_delparment():
    # 删除部门
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2")
    print(res.json()["errcode"])
    assert res.json()["errcode"] == 0



