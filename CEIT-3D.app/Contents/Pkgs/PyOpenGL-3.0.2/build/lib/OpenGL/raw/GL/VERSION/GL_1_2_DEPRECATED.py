'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_2'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_1_2',True)
_p.unpack_constants( """GL_RESCALE_NORMAL 0x803A
GL_LIGHT_MODEL_COLOR_CONTROL 0x81F8
GL_SINGLE_COLOR 0x81F9
GL_SEPARATE_SPECULAR_COLOR 0x81FA
GL_ALIASED_POINT_SIZE_RANGE 0x846D""", globals())
glget.addGLGetConstant( GL_RESCALE_NORMAL, (1,) )
glget.addGLGetConstant( GL_LIGHT_MODEL_COLOR_CONTROL, (1,) )
glget.addGLGetConstant( GL_ALIASED_POINT_SIZE_RANGE, (2,) )
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glColorTable( target,internalformat,width,format,type,table ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glColorTableParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glColorTableParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyColorTable( target,internalformat,x,y,width ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetColorTable( target,format,type,table ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetColorTableParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetColorTableParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glColorSubTable( target,start,count,format,type,data ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyColorSubTable( target,start,x,y,width ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter1D( target,internalformat,width,format,type,image ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glConvolutionFilter2D( target,internalformat,width,height,format,type,image ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glConvolutionParameterf( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glConvolutionParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glConvolutionParameteri( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glConvolutionParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyConvolutionFilter1D( target,internalformat,x,y,width ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyConvolutionFilter2D( target,internalformat,x,y,width,height ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetConvolutionFilter( target,format,type,image ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetConvolutionParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetConvolutionParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p)
def glGetSeparableFilter( target,format,type,row,column,span ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,ctypes.c_void_p)
def glSeparableFilter2D( target,internalformat,width,height,format,type,row,column ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetHistogram( target,reset,format,type,values ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetHistogramParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetHistogramParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetMinmax( target,reset,format,type,values ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMinmaxParameterfv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMinmaxParameteriv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLboolean)
def glHistogram( target,width,internalformat,sink ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLboolean)
def glMinmax( target,internalformat,sink ):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetHistogram( target ):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetMinmax( target ):pass

