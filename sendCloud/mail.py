# coding:utf-8
import json

import requests

from utils import decorator


class Mail(object):

    def __init__(self):
        self.send_mail = 'http://api.sendcloud.net/apiv2/mail/send'

    def _post_data(self, url, **kwargs):
        resp = requests.post(url, data=kwargs)
        return resp

    @decorator
    def send_email_simple(self, **kwargs):
        """
        * apiUser: API_USER
        * apiKey; API_KEY
        * from: send email addr
        * to: send to email, split by ';' eg: a@123.com;b@123.com
        * subject: email title
        * html: email content, format:text/html
        * contentSummary: email summary
        * fromName:send name
        * cc: copy to,split by ";" eg:a@123.com;b@123.com
        * bcc: secret copy to, split by ; eg:a@123.com;b@123.com
        * replyTo: default reply to, less than 3
        * useAddressList: default False, if to is list than set this True
        :param kwargs: 
        :return: 
        """

        resp = self._post_data(self.send_mail, **kwargs)
        if resp.status_code == 200:
            try:
                content = json.loads(resp.content)
                content = {
                    "result": content.get("result"),
                    "message": content.get("message")
                }
            except ValueError:
                content = {"result": False, "message": "return is not json"}
        else:
            content = {
                "result": False,
                "message": "send email error http code %s" % resp.status_code
            }
        return content
