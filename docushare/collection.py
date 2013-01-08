#!/usr/bin/env python2.6
# vim: fileencoding=cp932 fileformat=dos

"""collection  -  DochShare Collection

Copyright (C) 2012 HAYASI Hideki <linxs@linxs.org>  All rights reserved.

This software is subject to the provisions of the Zope Public License,
Version 2.1 (ZPL). A copy of the ZPL should accompany this distribution.
THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
FOR A PARTICULAR PURPOSE.
"""

from .dsclient import *
from .object import DSObject, register, getclass


__all__ = ("Collection",)


@register
class Collection(DSObject):
    """DocuShare Collection"""

    def __iter__(self):
        status = self.DSLoadChildren()
        chain = self._dsobject.EnumObjects(DSCONTF_CHILDREN)
        chain.Reset()
        while chain.NextPos:
            obj = chain.NextItem
            yield getclass(obj.Type)(obj)