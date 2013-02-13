'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_5'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_1_5',True)
_p.unpack_constants( """GL_VERTEX_ARRAY_BUFFER_BINDING 0x8896
GL_NORMAL_ARRAY_BUFFER_BINDING 0x8897
GL_COLOR_ARRAY_BUFFER_BINDING 0x8898
GL_INDEX_ARRAY_BUFFER_BINDING 0x8899
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING 0x889A
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING 0x889B
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING 0x889C
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING 0x889D
GL_WEIGHT_ARRAY_BUFFER_BINDING 0x889E
GL_FOG_COORD_SRC 0x8450
GL_FOG_COORD 0x8451
GL_CURRENT_FOG_COORD 0x8453
GL_FOG_COORD_ARRAY_TYPE 0x8454
GL_FOG_COORD_ARRAY_STRIDE 0x8455
GL_FOG_COORD_ARRAY_POINTER 0x8456
GL_FOG_COORD_ARRAY 0x8457
GL_FOG_COORD_ARRAY_BUFFER_BINDING 0x889D
GL_SRC0_RGB 0x8580
GL_SRC1_RGB 0x8581
GL_SRC2_RGB 0x8582
GL_SRC0_ALPHA 0x8588
GL_SRC1_ALPHA 0x8589
GL_SRC2_ALPHA 0x858A""", globals())
glget.addGLGetConstant( GL_VERTEX_ARRAY_BUFFER_BINDING, (1,) )
glget.addGLGetConstant( GL_NORMAL_ARRAY_BUFFER_BINDING, (1,) )
glget.addGLGetConstant( GL_COLOR_ARRAY_BUFFER_BINDING, (1,) )
glget.addGLGetConstant( GL_INDEX_ARRAY_BUFFER_BINDING, (1,) )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING, (1,) )
glget.addGLGetConstant( GL_EDGE_FLAG_ARRAY_BUFFER_BINDING, (1,) )
glget.addGLGetConstant( GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING, (1,) )
glget.addGLGetConstant( GL_FOG_COORD_SRC, (1,) )
glget.addGLGetConstant( GL_FOG_COORD_ARRAY_TYPE, (1,) )
glget.addGLGetConstant( GL_FOG_COORD_ARRAY_STRIDE, (1,) )
glget.addGLGetConstant( GL_FOG_COORD_ARRAY, (1,) )
glget.addGLGetConstant( GL_FOG_COORD_ARRAY_BUFFER_BINDING, (1,) )

