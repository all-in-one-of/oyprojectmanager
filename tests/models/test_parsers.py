# -*- coding: utf-8 -*-



import sys
import unittest
from oyProjectManager.models import project
from xml.dom import minidom






########################################################################
class DefaultSettingsParserTester(unittest.TestCase):
    """tests the DefaultSettingsParser class
    """
    
    
    
    #----------------------------------------------------------------------
    def setUp(self):
        """setup the test
        """
        
        minidom.xml
        
        self._settings_v1 = """<?xml version="1.0" ?>
        <root>
            <sequenceData shotPrefix="SH" shotPadding="3" revPrefix="r" revPadding="2" verPrefix="v" verPadding="3" timeUnit="pal">
                <structure>
                    <shotDependent>
                        ANIMATIONS
                        CAMERAS
                        COMPOSITING/OUTPUT
                        COMPOSITING/SHOTS
                        FX
                        LAYOUT
                        ONLINE
                        PREVIS
                        RENDERED_IMAGES/SHOTS
                        RENDER_SCENES
                    </shotDependent>
                    <shotIndependent>
                        COMPOSITING
                        EDIT_MOVIE
                        EDIT_MOVIE/EXPORT
                        ILLUSTRATION
                        ILLUSTRATION/CHARACTER_DESIGNS
                        MATTE_PAINT
                        MAKING_OF
                        MODELS
                        SHADING
                        OFFLINE
                        ONLINE/wholeMovie
                        OTHERS
                        OTHERS/assets
                        OTHERS/clips
                        OTHERS/data
                        OTHERS/fur
                        OTHERS/fur/furAttrMap
                        OTHERS/fur/furEqualMap
                        OTHERS/fur/furFiles
                        OTHERS/fur/furImages
                        OTHERS/fur/furShadowMap
                        OTHERS/mel
                        OTHERS/particles
                        OUTGOING_FILES
                        OUTGOING_FILES/IMAGES
                        OUTGOING_FILES/VIDEOS
                        OUTGOING_FILES/SOUNDS
                        RENDERED_IMAGES
                        RENDER_SCENES/renderData
                        RENDER_SCENES/renderData/depth
                        RENDER_SCENES/renderData/iprImages
                        RENDER_SCENES/renderData/mentalRay
                        RENDER_SCENES/renderData/mentalRay/finalgMap
                        RENDER_SCENES/renderData/mentalRay/lightMap
                        RENDER_SCENES/renderData/mentalRay/photonMap
                        RENDER_SCENES/renderData/mentalRay/shadowMap
                        RENDER_SCENES/renderData/shaders
                        RIGS
                        SOUND
                        STORYBOARD
                        STORYBOARD/ANIMATIC_STORYBOARD
                        TEXT
                        TEXT/SCENARIO
                        TEXTURES
                        TRACKING
                        VISUAL_REFERENCES
                        VISUAL_REFERENCES/ARTWORKS
                    </shotIndependent>
                </structure>
                <assetTypes>
                    <type name="ANIM"          path="ANIMATIONS"        shotDependent="1"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="CAMERA"        path="CAMERAS"           shotDependent="1"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="COMP"          path="COMPOSITING/SHOTS" shotDependent="1"  environments="NUKE"          output_path="COMPOSITING/OUTPUT"/>
                    <type name="LAYOUT"        path="LAYOUT"            shotDependent="1"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="MODEL"         path="MODELS"            shotDependent="0"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="OTHER"         path="OTHERS"            shotDependent="0"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="PREVIS"        path="PREVIS"            shotDependent="1"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="RENDER"        path="RENDER_SCENES"     shotDependent="1"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="RIG"           path="RIGS"              shotDependent="0"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="TEXTURE"       path="TEXTURES"          shotDependent="0"  environments="PHOTOSHOP"     output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="ILLUSTRATION"  path="ILLUSTRATION"      shotDependent="0"  environments="PHOTOSHOP"     output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="MATTE"         path="MATTE_PAINT"       shotDependent="0"  environments="PHOTOSHOP"     output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="SHADING"       path="SHADING"           shotDependent="0"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                    <type name="FX"            path="FX"                shotDependent="0"  environments="MAYA,HOUDINI"  output_path="RENDERED_IMAGES/SHOTS"/>
                </assetTypes>
                <shotData>
                </shotData>
            </sequenceData>
        </root>
        """
    
    
    
    #----------------------------------------------------------------------
    def test_default_settings(self):
        """
        """
        
    
    
    




