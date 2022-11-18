import bpy

key = []

def reg_keymap():
    print("키맵")
    kca = bpy.context.window_manager.keyconfigs.addon

    km = kca.keymaps.new(name="3D View", space_type="VIEW_3D")
    kmItem =  km.keymap_items.new("wm.call_menu","Y","PRESS",ctrl=True, shift=True)
    kmItem.properties.name = "MY_MT_Main_Menu"
    key.append((km,kmItem))

def unreg_keymap():
    for km,kmItem in key:
        km.keymap_items.remove(kmItem)
    key.clear()