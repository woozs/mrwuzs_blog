#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json


class TestCreateRoom(unittest.TestCase):



    #@classmethod
    def setUp(self):
        self.url = 'http://192.168.200.88:5526/admin/machince-room/create'
        self.name = '哈哈'
        self.login_url = 'http://192.168.200.88:5526/user/login'
        self.username = 'admin'
        self.password = 'R84NWY3RbfLMMgcuA0g4AMOyMDSJFOoppgWScg9XSp+xSHBhQ/lNWKICnr+V2iM6G4iq0qJW72WToZxmn8DiCntXE4IjDCIBQPdAlKjQaBPQoWh5Yw6gHHQ5Aj1aIkDuhvFfaXVbThDnkVv62ItkwS3QqPWA1nKNyEZfTExrugs='
        self.data= {
            'username': self.username,
            'password': self.password
        }
        self.s = requests.session()
        self.s.post(self.login_url, data=self.data).json()
    def test_ceratrome(self):
        """
        创建可用区
        """
        s=self.s
        data = {
            'name': self.name
        }

        response = s.post(self.url,data=data).json()
        print(response)
        assert response['code'] == 0
        assert response['message'] == 'OK'

if __name__ == '__main__':
#    test_data.init_data() # 初始化接口测试数据
    unittest.main()