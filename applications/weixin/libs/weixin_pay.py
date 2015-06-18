# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function

from applications.weixin.weixin.utils import to_weixin_xml
from libs.hashs import md5
import requests
import string
import random
import time


class WeixinPay(object):
    def __init__(self, app_id, app_secret, mch_id="", mch_secret_key=""):
        # 注意几个id之间的区别
        # app_id 公共号app_id
        # mch_id 支付商户id
        # mch_secret_key 支付商户key
        self.app_id = app_id
        self.app_secret = app_secret
        self.mch_id = mch_id
        self.mch_secret_key = mch_secret_key

    @classmethod
    def __create_nonce_str(cls):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    @classmethod
    def __create_timestamp(cls):
        return int(time.time())

    @classmethod
    def __sign(cls, secret_key, **kwargs):
        s = []
        for key in sorted(kwargs):
            if kwargs[key]:
                s.append('%s=%s' % (key, kwargs[key]))
        s.append("key=%s" % secret_key)
        temp_s = "&".join(s)
        md5_s = md5(temp_s.encode("utf-8"))
        return md5_s.upper()

    def unified_order(self, body, out_trade_no, total_fee, notify_url, detail="", attach="",
                      trade_type="JSAPI",  device_info="", spbill_create_ip="127.0.0.1", openid="", product_id="",
                      **kwargs):
        # 文档：http://pay.weixin.qq.com/wiki/doc/api/index.php?chapter=9_1
        url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
        params = {
            "appid": self.app_id,
            "mch_id": self.mch_id,
            "body": body,
            "attach": attach,
            "out_trade_no": out_trade_no,
            "total_fee": total_fee,
            "notify_url": notify_url,
            "trade_type": trade_type,
            "device_info": device_info,
            "spbill_create_ip": spbill_create_ip,
            "openid": openid,
            "product_id": product_id,
            "nonce_str": self.__create_nonce_str(),
            "detail": detail,
        }
        params.update(kwargs)
        sign = self.__sign(self.mch_secret_key, **params)
        params["sign"] = sign
        params['notify_url'] = notify_url

        post_data = to_weixin_xml(params)
        response = requests.post(url, data=post_data.encode("utf-8")).content
        return response

    def create_js_pay_params(self, prepay_id="", sign_type="MD5"):
        params = {
            "appId": self.app_id,
            "timeStamp": unicode(int(time.time())),
            "nonceStr": self.__create_nonce_str(),
            "package": "prepay_id=%s" % prepay_id,
            "signType": sign_type,
        }
        sign = self.__sign(self.mch_secret_key, **params)
        params['paySign'] = sign
        return params