from OpenGL.GL import *
import glfw
import numpy as np
import math
import random
from PIL import Image
import imgui

import lab_utils as lu
from lab_utils import vec3, vec2
from terrain import TerrainInfo
from ObjModel import ObjModel

class Props:
    position = vec3(0,0,0)
    heading = vec3(1,0,0)
    ##Random Rotation for z variable
    randRot = random.uniform(0, 6.28)
    terrain = None
    model = None
    zOffset = 1.0


    def render(self, view, renderingSystem):
        getInfo = self.terrain.getInfoAt(self.position)
        self.position[2] = lu.mix(self.position[2], getInfo.height - self.zOffset,\
                                  1);
        rotation = lu.make_rotation_z(self.randRot)
        modelToWorldTransform = lu.make_mat4_from_zAxis(self.position, self.heading, \
                                                        vec3(0,0,1))
        renderingSystem.drawObjModel(self.model, rotation * modelToWorldTransform, view)

    def load(self, objModelName, terrain, position, renderingSystem):
        self.terrain = terrain
        self.model = ObjModel(objModelName)
        self.position = position
        self.randRot = random.uniform(0, 6.28) #0 to 2pi

    
        
                
