import bpy
from bpy.props import IntProperty, FloatProperty



class Tool_WallCube(bpy.types.Operator):
    bl_idname = "tool.wall_cube"
    bl_label = "WALL CUBE"
    # bl_options = {"REGISTER","UNDO"}

    polygon : IntProperty(name="면의 갯수", default=4, min=1, max=10)
    height : FloatProperty(name="벽 높이", default=2, min=1, max=50)
    thickness : FloatProperty(name="벽 두께", default = 0.1, min=0.1, max=10)

    length1 : FloatProperty(name="1번 벽 길이", default=2, min=1, max=50)
    angle1 : IntProperty(name="각도", default=0, min=1, max=365)
    length2 : FloatProperty(name="2번 벽 길이", default=2, min=1, max=50)
    angle2 : IntProperty(name="각도", default=90, min=1, max=365)
    length3 : FloatProperty(name="3번 벽 길이", default=2, min=1, max=50)
    angle3 : IntProperty(name="각도", default=90, min=1, max=365)
    length4 : FloatProperty(name="4번 벽 길이", default=2, min=1, max=50)
    angle4 : IntProperty(name="각도", default=90, min=1, max=365)





    # def draw(self,context):
    #     layout = self.layout
    #     layout.prop(self,'polygon')
    #     layout.prop(self,'height')
    #     layout.prop(self,'thickness')

    #     layout.prop(self,'length1')
    #     layout.prop(self,'angle1')
    #     layout.prop(self,'length2')
    #     layout.prop(self,'angle2')
    #     layout.prop(self,'length3')
    #     layout.prop(self,'angle3')
    #     layout.prop(self,'length4')
    #     layout.prop(self,'angle4')


    def execute(self,context):

        bpy.ops.archipack.wall2()  # 벽체 생성 
        o = bpy.context.active_object
        m = o.data
        prop = m.archipack_wall2[0]  # 벽체를 불러온다.
        prop.n_parts = self.polygon

        oned = 0.0174533
        w = bpy.context.object.data.archipack_wall2[0]
        w.z = self.height

        bpy.context.object.data.archipack_wall2[0].z = self.height # Z
        bpy.context.object.data.archipack_wall2[0].width = self.thickness
        bpy.context.object.data.archipack_wall2[0].parts[0].a0 = (self.angle1 * oned)
        bpy.context.object.data.archipack_wall2[0].parts[0].length = self.length1
        bpy.context.object.data.archipack_wall2[0].parts[0].height = self.height
        bpy.context.object.data.archipack_wall2[0].parts[1].a0 = (self.angle2 * oned)
        bpy.context.object.data.archipack_wall2[0].parts[1].length = self.length2
        bpy.context.object.data.archipack_wall2[0].parts[2].a0 = (self.angle3 * oned)
        bpy.context.object.data.archipack_wall2[0].parts[2].length = self.length3
        bpy.context.object.data.archipack_wall2[0].parts[3].a0 = (self.angle4 * oned)
        bpy.context.object.data.archipack_wall2[0].parts[3].length = self.length4

        return{'FINISHED'}

    #def createWall(self,context):