import bpy

class MY_MT_Main_Menu(bpy.types.Menu):
    bl_idname = "MY_MT_Main_Menu"
    bl_label = "Wall Creater"

    def draw(self,context):
        layout = self.layout
        layout.operator_context = "INVOKE_DEFAULT"
        layout.label(text='wall Create tool')
        layout.operator("tool.getwall",text="벽 메뉴 추가",icon="FILE_VOLUME")
        layout.operator("tool.wall_cube",text="벽 생성",icon="FILE_VOLUME")