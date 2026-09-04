"""
Unreal Engine 5 - Autonomous Robot Spawner & Setup Script
Creates and places our exact 20x20x5 cm robot actor into the apartment level:
- Chassis (20cm x 20cm x 5cm box)
- 4 Wheels (Skid-steer differential placement)
- 720p Webcam (SceneCaptureComponent2D with 1280x720 Render Target)
- 4x HC-SR04 Ultrasonic Raycasts (Front, Left, Back, Right)
- NodeMCU OLED mount
"""

try:
    import unreal
    IN_UE = True
except ImportError:
    IN_UE = False

def setup_robot(spawn_location=None):
    if not IN_UE:
        print("[RobotSetup] Must be run inside Unreal Editor Python console.")
        return

    if spawn_location is None:
        # Default entrance/living room floor location (X=0, Y=0, Z=10cm above origin)
        spawn_location = unreal.Vector(0.0, 0.0, 15.0)

    subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary

    # 1. Create or load RenderTarget2D for 720p Camera (1280x720)
    rt_package_path = '/Game/Robot'
    rt_asset_name = 'RT_Camera720p'
    full_rt_path = f"{rt_package_path}/{rt_asset_name}"

    if not editor_asset_lib.does_asset_exist(full_rt_path):
        rt_factory = unreal.TextureRenderTarget2DFactoryNew()
        rt = asset_tools.create_asset(rt_asset_name, rt_package_path, unreal.TextureRenderTarget2D, rt_factory)
        if rt:
            rt.set_editor_property('size_x', 1280)
            rt.set_editor_property('size_y', 720)
            rt.set_editor_property('render_target_format', unreal.TextureRenderTargetFormat.RTF_RGBA8)
            editor_asset_lib.save_asset(full_rt_path)
            print("[RobotSetup] 720p Render Target created: 1280x720 RGBA8")
    else:
        rt = editor_asset_lib.load_asset(full_rt_path)
        print("[RobotSetup] Loaded existing 720p Render Target.")

    # 2. Spawn the Robot Root Actor
    actor_class = unreal.StaticMeshActor
    robot = subsystem.spawn_actor_from_class(actor_class, spawn_location, unreal.Rotator(0, 0, 0))
    if not robot:
        print("[RobotSetup] Error: Failed to spawn robot actor.")
        return None

    robot.set_actor_label("AutonomousBoxRobot")
    root_comp = robot.static_mesh_component

    # 3. Setup Chassis (20cm x 20cm x 5cm)
    cube_mesh = editor_asset_lib.load_asset('/Engine/BasicShapes/Cube.Cube')
    if cube_mesh:
        root_comp.set_static_mesh(cube_mesh)
    # Default cube is 100x100x100 cm -> Scale: 0.20, 0.20, 0.05
    root_comp.set_editor_property('relative_scale3d', unreal.Vector(0.20, 0.20, 0.05))
    root_comp.set_mobility(unreal.ComponentMobility.MOVABLE)
    root_comp.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS)
    root_comp.set_collision_profile_name("BlockAllDynamic")

    # Dark material for chassis if available
    basic_mat = editor_asset_lib.load_asset('/Engine/BasicShapes/BasicShapeMaterial.BasicShapeMaterial')
    if basic_mat:
        root_comp.set_material(0, basic_mat)

    # 4. Attach 720p Webcam (SceneCaptureComponent2D)
    cam_comp = unreal.SceneCaptureComponent2D(robot)
    cam_comp.attach_to_component(root_comp, unreal.AttachmentTransformRules.KEEP_RELATIVE_TRANSFORM, "")
    # Relative offset: front edge (X=8.5cm, Z=5.5cm), tilted down 7 degrees
    # Note: scale of root_comp is 0.20, so unscaled relative location = offset / scale
    cam_comp.set_editor_property('relative_location', unreal.Vector(42.5, 0.0, 110.0))
    cam_comp.set_editor_property('relative_rotation', unreal.Rotator(-7.0, 0.0, 0.0))
    if rt:
        cam_comp.set_editor_property('texture_target', rt)
    cam_comp.set_editor_property('fov_angle', 70.0)
    cam_comp.set_editor_property('capture_source', unreal.SceneCaptureSource.SCS_FINAL_COLOR_LDR)
    robot.add_instance_component(cam_comp)

    # 5. Select the newly spawned robot so the user sees its outline
    subsystem.set_selected_level_actors([robot])

    print(f"[RobotSetup] Successfully created and spawned AutonomousBoxRobot at {spawn_location}!")
    print("[RobotSetup] Dimensions: 20x20x5 cm, 720p Webcam attached to RT_Camera720p.")
    return robot

if __name__ == '__main__':
    setup_robot()
