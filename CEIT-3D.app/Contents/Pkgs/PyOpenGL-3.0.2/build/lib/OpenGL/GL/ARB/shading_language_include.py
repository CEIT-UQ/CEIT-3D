'''OpenGL extension ARB.shading_language_include

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shading_language_include to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces a #include GLSL directive to allow reusing
	the same shader text in multiple shaders and defines the semantics
	and syntax of the names allowed in #include directives. It also
	defines API mechanisms to define the named string backing a
	#include.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shading_language_include.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.shading_language_include import *
### END AUTOGENERATED SECTION