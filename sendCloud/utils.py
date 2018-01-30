# coding:utf-8
import re
import functools
from voluptuous import Schema, ALLOW_EXTRA, All, Optional, Required, Invalid
email_regex = re.compile(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$")

# 这里做校验等


def check_email(email):
    email_list = email.split(";")
    check_func = lambda x: email_regex.match(x)
    reduce_func = lambda x, y: x and y

    is_valid = reduce(reduce_func, map(check_func, email_list))
    if is_valid:
        return email
    raise Invalid('email error')

send_email_schema = Schema({
    Required("apiUser", msg='params apiUser must exist'):
        All(basestring, msg='params apiUser must basestring'),
    Required("apiKey", msg='params apiKey must exist'):
        All(basestring, msg='params apiKey must basestring'),
    Required("from", msg='params from must exist'):
        All(check_email, msg='params from error'),
    Required("to", msg='params to must exist'):
        All(check_email, msg='params to error, use ; split'),
    Required("subject", msg='params subject must exist'):
        All(basestring, msg='prams subject must basestring'),
    Required("html", msg='params html must exist'):
        All(basestring, msg='params htmll must exist'),
    "fromName": All(basestring, msg='params fromName error'),
    "labelId": All(int, msg='params labelId is int'),
    "cc": All(basestring, check_email, msg='params cc email error'),
    "bcc": All(basestring, check_email, msg='params bcc email error'),
    "replyTo": All(basestring, check_email, msg='params replyTo email error'),
    "contentSummary": All(basestring, msg='params contentSummary error'),
    "plain": All(basestring, msg='params plain error'),
    Optional("useAddressList", default=False):
        All(bool, msg='params useAddressList is bool'),
}, extra=ALLOW_EXTRA)


def decorator(func):
    @functools.wraps(func)
    def wrapper(self, **kwargs):
        try:
            data = send_email_schema(kwargs)
        except Invalid as e:
            raise Exception(e.msg)
        return func(self, **data)
    return wrapper
