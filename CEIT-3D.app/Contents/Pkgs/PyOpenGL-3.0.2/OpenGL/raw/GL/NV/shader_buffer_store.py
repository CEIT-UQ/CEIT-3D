'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_NV_shader_buffer_store'
_p.unpack_constants( """GL_SHADER_GLOBAL_ACCESS_BARRIER_BIT_NV 0x10""", globals())


def glInitShaderBufferStoreNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
