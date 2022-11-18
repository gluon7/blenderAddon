import bpy

class SideBarMenu(bpy.types.Panel):
    bl_label = "벽체 수정"
    bl_idname = "OBJECT_PT_SIDEBAR"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_category = "WALL"

    def draw(self, context):
        layout = self.layout

        o = bpy.context.active_object
        m = o.data
        prop = m.archipack_wall2[0]


        row = layout.row(align=True)
        
        row.operator("archipack.wall2_manipulate", icon='VIEW_PAN')

        box = layout.box()
        box.prop(prop, 'n_parts')
        box.prop(prop, 'step_angle')
        box.prop(prop, 'width')
        box.prop(prop, 'z')
        row = layout.row()

        row = layout.row(align=True)
        n_parts = prop.n_parts
        if prop.closed:
            n_parts += 1
        for i, part in enumerate(prop.parts):
            if i < n_parts:
                box = layout.box()
                part.draw(box, context, i)

# def register():
#     bpy.utils.register_class(SideBarMenu)


# def unregister():
#     bpy.utils.unregister_class(SideBarMenu)


# if __name__ == "__main__":
#     register()
