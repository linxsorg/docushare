#!/usr/bin/env python2.6
# vim: fileencoding=cp932 fileformat=dos

"""weblog  -  DochShare Weblog object

Copyright (C) 2012 HAYASI Hideki <linxs@linxs.org>  All rights reserved.

This software is subject to the provisions of the Zope Public License,
Version 2.1 (ZPL). A copy of the ZPL should accompany this distribution.
THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
FOR A PARTICULAR PURPOSE.
"""

from . import dsclient
from .object import DSObject, DSIterable, register


__all__ = ("WeblogEntry", "Weblog")


@register
class WeblogEntry(DSObject):
    pass


@register
class Weblog(DSIterable):

    subobject_types = dsclient.DSCONTF_CHILDREN
