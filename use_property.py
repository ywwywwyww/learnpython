# -*- coding: utf-8 -*-

class Screen(object):
    def __init__(self):
    	self._resolution = 0
    	self._width = 0
    	self._height = 0
    
    @property
    def width(self):
    	return self._width
    
    @width.setter
    def width(self, w):
    	self._width = w
    	self._resolution = self._width * self._height
    	
    @property
    def height(self):
    	return self._height
    
    @height.setter
    def height(self, h):
    	self._height = h
    	self._resolution = self._width * self._height
    	
    @property
    def resolution(self):
    	return self._resolution

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
