import bpy
from .my_menu import MY_MT_Main_Menu

my_class = [
    MY_MT_Main_Menu
]

def reg_menus():
    from bpy.utils import register_class
    for a in my_class:
        register_class(a)

def unreg_menus():
    from bpy.utils import unregister_class
    for a in my_class:
        unregister_class(a)