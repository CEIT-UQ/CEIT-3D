'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_NV_fog_distance'
_p.unpack_constants( """GL_FOG_DISTANCE_MODE_NV 0x855A
GL_EYE_RADIAL_NV 0x855B
GL_EYE_PLANE_ABSOLUTE_NV 0x855C""", globals())
glget.addGLGetConstant( GL_FOG_DISTANCE_MODE_NV, (1,) )


def glInitFogDistanceNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
