# STL 파일 경로와 이름 설정
output_path = "./"
output_filename = "modeling"

# 모든 모델 객체를 선택하고 변환 모드로 전환
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.mode_set(mode='OBJECT')

# 선택된 모델들을 순회하며 STL 파일로 내보내기
for obj in bpy.context.selected_objects:
    if obj.type == 'MESH':
        stl_path = f"{output_path}{obj.name}_{output_filename}.stl"
        bpy.ops.export_mesh.stl(filepath=stl_path, use_selection=True)

# 모든 모델 선택 해제
bpy.ops.object.select_all(action='DESELECT')
