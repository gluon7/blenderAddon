bl_info = {
    "name":"My tool",
    "description":"Create Wall2",
    "author":"hyunUk",
    "version":(1,1),
    "blender":(2,93,0),
    "location":"View3D",
    "category":"3D View"
}

def register():
    print("블랜더 실행")

    from .menu import reg_menus
    reg_menus()
    from .util import reg_keymap
    reg_keymap()
    from .controller import reg_controller
    reg_controller()


def unregister():
    print("블랜더 종료")
    from .menu import unreg_menus
    unreg_menus()
    from .util import unreg_keymap
    unreg_keymap()
    from .controller import unreg_controller
    unreg_controller()




