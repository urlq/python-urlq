# -*- coding: utf-8 -*-

from urlq.utils import *

class BaseError(Exception):
    '''
    Base exception for urlq sdk
    '''
    def __init__(self, errcode, errmsg):
        '''
        :param errcode: Error code
        :param errmsg: Error message
        '''
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        _repr = 'Error code: {code}, message: {msg}'.format(
            code=self.errcode,
            msg=self.errmsg
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)

    def __repr__(self):
        _repr = '{klass}({code}, {msg})'.format(
            klass=self.__class__.__name__,
            code=self.errcode,
            msg=self.errmsg
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)


class ResourceNotExistsError(BaseError):
    '''
    raised when request a resource that does not exist.
    '''
    def __init__(self, service_name):
        errcode = '001'
        errmsg = "The '%s' resource does not exist." % service_name
        super(ResourceNotExistsError, self).__init__(errcode, errmsg)


class DataNotFoundError(BaseError):
    '''
    raised when no data returned
    '''

    def __init__(self, service_name, request):
        errcode = '002'
        errmsg = (
            "The '%s' resource return nothing."
            "Request:\n"
            "%s" % (service_name, str(request))
        )
        super(DataNotFoundError, self).__init__(errcode, errmsg)


class OperateFailedError(BaseError):
    '''
    raised when operate failed
    '''

    def __init__(self, service_name, request):
        errcode = '003'
        errmsg = (
            "Failed operation on resource  '%s'."
            "Request:\n"
            "%s" % (service_name, str(request))
        )
        super(OperateFailedError, self).__init__(errcode, errmsg)

