import bpy

from .wall_cube import Tool_WallCube
from .getwall import SideBarMenu
from .new import (MyProperties, PANEL_CUSTOM_UI, BUTTON_CUSTOM, getm3c2, togglebtn, divide, getc2m, proportionalbtn, )


from bpy.props import (StringProperty, PointerProperty)


myclasses = {
    Tool_WallCube,
    SideBarMenu,
    MyProperties, PANEL_CUSTOM_UI, BUTTON_CUSTOM, getm3c2, togglebtn, divide, getc2m, proportionalbtn, 
}



def reg_controller():
    from bpy.utils import register_class
    for a in myclasses:
        register_class(a)
    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)
    

def unreg_controller():
    from bpy.utils import unregister_class
    for a in myclasses:
        unregister_class(a)
