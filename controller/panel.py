import bpy
from bpy.props import StringProperty
import csv

subtypes = ['FILE_PATH', 'DIR_PATH', 'FILE_NAME']
print(getattr)
def print_value(subtype):
    def print_value(self, context):
        print(subtype, getattr(self, subtype))
    return print_value

for st in subtypes:
    setattr(bpy.types.WindowManager, st, 
            StringProperty(subtype=st, update=print_value(st)))

class btntest(bpy.types.Operator):
    bl_label = "btntest"
    bl_idname = "object.button_test"
    
    def execute(self, context):
        print("버튼 눌림")
        return {'FINISHED'}


class WallPanel(bpy.types.Panel):
    bl_label = "Wall Controll Panel"
    bl_idname = "OBJECT_PT_WALL"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        wm = context.window_manager

        row = layout.row() # 한줄 띄우기

        row.label(text="선택된 오브젝트는 : " + obj.name)
        row = layout.row()

        row.label(text="스캐너 파일을 선택해주세요")
        row = layout.row()

        layout.prop(wm, "FILE_PATH")
        row = layout.row()

        row.label(text="파일 저장 경로를 선택해주세요")
        row = layout.row()
        
        layout.prop(wm, "DIR_PATH")
        row = layout.row()

        row.label(text="저장할 파일 이름을 입력해주세요")
        row = layout.row()
        
        layout.prop(wm, "FILE_NAME")
        row = layout.row()


        col = layout.column()
        row = col.row(align=True)
        col.prop(obj, "location")

        col = layout.column()
        row = col.row(align=True)
        col.prop(obj, "rotation_euler")

        row = layout.row()
        row.operator("object.camera_add", text="카메라 추가")



    
