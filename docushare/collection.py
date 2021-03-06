#!/usr/bin/env python2.7
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

from . import dsclient
from .object import DSContainer, register


__all__ = ("Collection",)


@register
class Collection(DSContainer):
    """DocuShare Collection"""

    typenum = dsclient.DSXITEMTYPE_COLLECTION
    subobject_types = dsclient.DSCONTF_CHILDREN
    subobject_typenames = ("Collection", "File", "BulletinBoard", "Weblog",
                           "Wiki")
    upload_attributes = ("Title", "Summary", "Description", "Keywords",
                         "Logo", "BackgroundImage", "SortOrder")
