# -*- coding: utf-8 -*-
"""
These serializer mixinins and fields are used exclusively to import the file
``workdir/fixtures/products-meta.json``. They are not intended for general
purpose and can be deleted thereafter.
"""
from __future__ import unicode_literals

from parler_rest.serializers import TranslatedFieldsField, TranslatedField, TranslatableModelSerializerMixin

__all__ = ['TranslatedFieldsField', 'TranslatedField',
           'TranslatableModelSerializerMixin']
