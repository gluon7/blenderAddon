import bpy
import bpy.types
import csv
import range_scanner
from bpy.props import (StringProperty, PointerProperty)
from bpy.types import (Panel, PropertyGroup)
import subprocess

subtypes = ['FILE_PATH', 'DIR_PATH', 'FILE_NAME']
print(getattr)
def print_value(subtype):
    def print_value(self, context):
        print(subtype, getattr(self, subtype))
    return print_value

for st in subtypes:
    setattr(bpy.types.WindowManager, st, 
            StringProperty(subtype=st, update=print_value(st)))

class togglebtn(bpy.types.Operator):
    bl_label = "ToggleButton"
    bl_idname = "object.button_toggle"

    def execute(self, context):
        print('Toggle Button Push')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class proportionalbtn(bpy.types.Operator):
    bl_label = "pbtn"
    bl_idname = "object.button_propotion"

    def execute(self, context):
        print('비례편집 버튼 눌림')
        

        obj = bpy.context.active_object
        object_mode = 'OBJECT' if obj is None else obj.mode

        if(object_mode == 'OBJECT'):
            if(bpy.context.scene.tool_settings.use_proportional_edit_objects == True):
                bpy.context.scene.tool_settings.use_proportional_edit_objects = False
            else:
                bpy.context.scene.tool_settings.use_proportional_edit_objects = True
        
        if(object_mode == 'EDIT'):
            if(bpy.context.scene.tool_settings.use_proportional_edit == True):
                bpy.context.scene.tool_settings.use_proportional_edit = False
            else:
                bpy.context.scene.tool_settings.use_proportional_edit = True

        print(bpy.context.scene.tool_settings.use_proportional_edit_objects)

        return {'FINISHED'}



class divide(bpy.types.Operator):
    bl_label = "subdivide"
    bl_idname = "object.button_divide"

    def execute(self, context):
        print('Toggle Button Push')
        bpy.ops.mesh.subdivide(number_cuts=1)
        return {'FINISHED'}

class MyProperties(PropertyGroup):

    first: StringProperty(
        name="first",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    last: StringProperty(
        name="last",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )
    
    folder: StringProperty(
        name="folder",
        description=":",
        default="",
        maxlen=1024,
        subtype='DIR_PATH',
        )
    
    CloudCompare: StringProperty(
        name="CloudCompare",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )
    
    m3c2: StringProperty(
        name="m3c2",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )
    
    c2m: StringProperty(
        name="c2m",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    LAS: StringProperty(
        name="LAS",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    STL:StringProperty(
        name="STL",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    spath:StringProperty(
        name="파일 저장 경로",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    filename: StringProperty(
        name="파일 이름.확장자 입력",
        description=":",
        default="",
        maxlen=1024,
        subtype='FILE_NAME',
        )


class getc2m(bpy.types.Operator):
    bl_label = "C2M analyse"
    bl_idname = "object.button_c2m"

    def execute(self,context):
        print("C2C 분석")

        cloud = bpy.context.scene.my_tool.CloudCompare
        input_PC = bpy.context.scene.my_tool.LAS
        input_Mesh = bpy.context.scene.my_tool.STL
        spath = bpy.context.scene.my_tool.spath
        file = bpy.context.scene.my_tool.filename     
        
        C2M=subprocess.Popen([cloud,"-O",input_PC,"-O",input_Mesh,"-c2m_dist","-C_EXPORT_FMT","LAS","-AUTO_SAVE","OFF","-SAVE_CLOUDS","FILE", spath+file])
        return {'FINISHED'}


class getm3c2(bpy.types.Operator):
    bl_label = "m3c2 analyse"
    bl_idname = "object.button_m3c2"
    
    def execute(self,context):
        print("분석버튼 클릭")
        
        cloud = bpy.context.scene.my_tool.CloudCompare
        txt = bpy.context.scene.my_tool.m3c2
        input1 = bpy.context.scene.my_tool.first
        input2 = bpy.context.scene.my_tool.last
        M3C2 = subprocess.Popen([cloud,"-O",input1,"-O",input2,"-m3c2",txt])
        return {'FINISHED'}

class BUTTON_CUSTOM(bpy.types.Operator):
    bl_label = "BUTTON CUSTOM"
    bl_idname = "object.button_custom"

    def execute(self,context):
        print("button pushed")
        filePath = bpy.data.window_managers["WinMan"].FILE_PATH
        dirPath = bpy.data.window_managers["WinMan"].DIR_PATH
        FILENAME = bpy.data.window_managers["WinMan"].FILE_NAME

        def READCSV(filePath):
            result = dict()

            with open(filePath, newline='', encoding = 'cp949') as csvFile:
                reader = csv.reader(csvFile)
                    
                for i, r in enumerate(reader):
                    
                    if i == 0:
                        continue
                    if i == 1:
                        result[0] = {'min' : r[1], 'max' : r[2]} 
                    if i == 2:
                        del result[1]
                        continue
                    if i == 3:
                        continue
                    
                    result[i] = {
                        'price': r[0],
                        'type' : r[1],
                        'Name' : r[2],
                        'Horizontal FOV' : r[3], 
                        'Resolution horizontal' : r[4], 
                        'Vertical FOV' : r[5],
                        'Resolution vertical' : r[6],
                        'Lwer reflectivity' : r[7],
                        'Lwer distance' : r[8],
                        'Upper reflectivity' : r[9], 
                        'Upper distance' : r[10],
                        'Noise Mu' : r[11],
                        'Noise sigma' : r[12],
                    }
                    
            k = list(result.keys())
            v = list(result.values())

            newkey = []

            for i in range(len(v)):
                newkey.append(i)
            print(newkey)

            newdict = {}

            for i in range(len(v)):
                newdict[newkey[i]] = v[i]
                
            max = int(newdict[0].get('max'))
            min = int(newdict[0].get('min'))

            print(min , max)

            for j in newdict:
                if j == 0:
                    continue
                
                scname = str(newdict[j].get('Name'))
                p = int(newdict[j].get('price'))
                
                Hf = float(newdict[j].get('Horizontal FOV'))
                Rx = float(newdict[j].get('Resolution horizontal'))
                Vf = float(newdict[j].get('Vertical FOV'))
                Ry = float(newdict[j].get('Resolution vertical'))
                Lr = float(newdict[j].get('Lwer reflectivity'))
                Ld = float(newdict[j].get('Lwer distance'))
                Ur = float(newdict[j].get('Upper reflectivity'))
                Ud = float(newdict[j].get('Upper distance'))
                Nm = float(newdict[j].get('Noise Mu'))
                Ns = float(newdict[j].get('Noise sigma'))
                
                if min <= p and max >= p:
                    print('price : ', p)
                    print(newdict[j])
                    
                    obj = bpy.context.scene.objects
                    camera = bpy.context.scene.scannerProperties.scannerObject

                    range_scanner.ui.user_interface.scan_rotating(
                bpy.context, 
                #bpy.context.scene.objects["Camera"]
                scannerObject=camera,
                xStepDegree=Rx, fovX=Hf, yStepDegree=Ry, fovY=Vf, rotationsPerSecond=20,
                reflectivityLower=Lr, distanceLower=Ld, reflectivityUpper=Ur, distanceUpper=Ud, maxReflectionDepth=10,    
                enableAnimation=False, frameStart=1, frameEnd=1, frameStep=1, frameRate=1,
                addNoise=True, noiseType='gaussian', mu=Nm, sigma=Ns, noiseAbsoluteOffset=0.0, noiseRelativeOffset=0.0, 
                simulateRain=False, rainfallRate=0.0,
                addMesh=True,
                exportLAS=True, exportHDF=False, exportCSV=False, exportSingleFrames=False,
                dataFilePath=dirPath, dataFileName= FILENAME+'_'+scname + str(j),
                debugLines=False, debugOutput=False, outputProgress=False, measureTime=False, singleRay=False, destinationObject=None, targetObject=None)

        READCSV(filePath)
        return {'FINISHED'}
    # execute end

class PANEL_CUSTOM_UI(bpy.types.Panel):
    bl_label = "벽체 관리 시스템"
    bl_idname = "OBJECT_PT_Panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    def draw(self,context):
        layout = self.layout
        wm = context.window_manager
        properties = context.scene.scannerProperties
        obj = context.object

        row = layout.row()
        row.label(text = "카메라 위치를 조정해주세요")
        
        row = layout.row()
        row.label(text="선택된 오브젝트는 : " + obj.name)

        row = layout.row()

        col = layout.column()
        row = col.row(align=True)
        col.prop(obj, "location")

        col = layout.column()
        row = col.row(align=True)
        col.prop(obj, "rotation_euler")

        row = layout.row()
        row.operator("object.camera_add", text="카메라 추가")

        row = layout.row()
        row = layout.row()
        row = layout.row()

        row.label(text="벽체를 편집해주세요")
        row = layout.row()
        row.operator("object.button_toggle", text="토글버튼")
        row = layout.row()
        row.operator("object.button_propotion", text="비례편집")


        if(bpy.context.object.mode == "EDIT"):
            row = layout.row()
            row.label(text = "EDIT 모드 활성화")

            row = layout.row()
            row.operator("object.button_divide", text="나누기")


        row = layout.row()
        row.label(text="스캐너 CSV 파일을 선택해주세요")
        row = layout.row()
        row.prop(wm, "FILE_PATH")
        

        row = layout.row()
        row.label(text="파일 저장 경로를 선택해주세요")
        row = layout.row()
        row.prop(wm, "DIR_PATH")
        

        row = layout.row()
        row.label(text="저장할 파일 이름을 입력해주세요")
        row = layout.row()
        row.prop(wm, "FILE_NAME")
        
        row = layout.row()
        row.prop(properties, "scannerObject")

        row = layout.row()
        row.operator("object.button_custom", text="포인트 클라우드 데이터 추출")


        scene = context.scene
        mytool = scene.my_tool
        layout.prop(mytool, "m3c2")
        layout.prop(mytool, "CloudCompare")
        layout.prop(mytool, "first")
        layout.prop(mytool, "last")
        layout.prop(mytool, "folder")
        layout.separator()
        
        row = layout.row()
        row.operator("object.button_m3c2", text="Analysis M3C2")


        
        row = layout.row()
        row.operator("export_mesh.stl", text="STL 추출")

        row = layout.row()
        layout.prop(mytool, "CloudCompare")

        layout.prop(mytool, "LAS")
        row = layout.row()
        layout.prop(mytool, "STL")
        row = layout.row()
        layout.prop(mytool, "spath")
        row = layout.row()
        row.label(text = "확장자 명을 LAS로 입력해주세요")
        row = layout.row()
        layout.prop(mytool, "filename")

        row = layout.row()
        row.operator("object.button_c2m", text="Analysis C2M")