#!/usr/bin/env python
#coding=utf-8

import json

def buildString(instance) :
    _str = ''
    if isinstance(instance, (list, tuple)) :
        f = False
        _str += '['
        for now in instance :
            if not f :
                f = True
            else :
                _str += ', '
            _str += "%s" % buildString(now)

        _str += ']'
    elif isinstance(instance, set) :
       f = False
       _str += '{'
       for now in instance :
           if not f :
               f = True
           else :
               _str += ', '
           _str += '%s' % (buildString(now))
       _str += '}'
    elif isinstance(instance, dict) :
       f = False
       _str += '{'
       for now in instance :
           x = instance[now]
           if not f :
               f = True
           else :
               _str += ', '
           _str += '%s:%s' % (now, buildString(x))
       _str += '}'
    elif isinstance(instance, Object) :
        f = False
        _str += '{'
        for item in instance.__dict__ :
            if not f :
                f = True
            else :
                _str += ', '
            now = instance.__dict__[item]
            _str += "%s:%s" % (item, buildString(now))
        _str += '}'
    else :
        _str += str(instance)
    return _str

class Object(object) :
    def __init__(self) :
        #super(Object, self).__init__() # no need to call object.__init__
        self.name = self.__module__
        self.name += '.' + self.__class__.__name__

    def toString(self) :
        return buildString(self)

    def __str__(self) :
        return self.toString()

class Entity(Object) :
    def __init__(self) :
        super(Entity, self).__init__()

    def object2dict(self, obj):
        #convert object to a dict
        d = {}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d

    def dict2object(self, d):
        #convert dict to object
        if'__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            inst = class_()
            inst.__dict__ = dict((key.encode('gbk'), value) for key, value in d.items())
        else:
            inst = d
        return inst

    def toJson(self) :
        return json.dumps(self, default = self.object2dict)

    def fromJson(self, dump) :
        return json.loads(dump, object_hook = self.dict2object)
