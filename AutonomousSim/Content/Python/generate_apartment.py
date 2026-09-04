"""
Unreal Engine 5 - Multi-Room Apartment Environment Generator
Generates a realistic multi-room indoor environment (Living Room, Corridor, Bedroom, Kitchen)
with walls, doorways, floor, lighting, and navigation obstacles.
Run this script inside Unreal Engine:
In Unreal Editor -> Output Log -> switch command line to Python -> run:
import generate_apartment; generate_apartment.build_apartment()
"""

try:
    import unreal
    IN_UE = True
except ImportError:
    IN_UE = False

def spawn_box_actor(subsystem, location, extent, name, color_mat=None):
    """Spawns a scaled static mesh cube as a wall, floor or obstacle"""
    actor_class = unreal.StaticMeshActor
    actor = subsystem.spawn_actor_from_class(actor_class, location, unreal.Rotator(0, 0, 0))
    if actor:
        actor.set_actor_label(name)
        mesh_comp = actor.static_mesh_component
        # Load engine basic cube mesh
        cube_mesh = unreal.EditorAssetLibrary.load_asset('/Engine/BasicShapes/Cube.Cube')
        if cube_mesh:
            mesh_comp.set_static_mesh(cube_mesh)
        # Cube is 100x100x100 cm by default, scale accordingly
        scale = unreal.Vector(extent[0] / 100.0, extent[1] / 100.0, extent[2] / 100.0)
        actor.set_actor_scale3d(scale)
        # Enable collision
        mesh_comp.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS)
        mesh_comp.set_collision_response_to_all_channels(unreal.CollisionResponse.ECR_BLOCK)
    return actor

def build_apartment():
    if not IN_UE:
        print("[ApartmentGen] Please run inside Unreal Engine Python console.")
        return

    subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    wall_height = 250.0  # 2.5 meters
    wall_thick = 15.0    # 15 cm

    print("[ApartmentGen] Starting generation of 4-room apartment...")

    # 1. Main Floor (14m x 10m)
    spawn_box_actor(subsystem, unreal.Vector(0, 0, -10), (1400.0, 1000.0, 20.0), "Floor_Main")

    # 2. Outer Perimeter Walls
    # North & South outer walls (14m)
    spawn_box_actor(subsystem, unreal.Vector(0, 500, wall_height/2), (1400.0, wall_thick, wall_height), "Wall_Outer_North")
    spawn_box_actor(subsystem, unreal.Vector(0, -500, wall_height/2), (1400.0, wall_thick, wall_height), "Wall_Outer_South")
    # East & West outer walls (10m)
    spawn_box_actor(subsystem, unreal.Vector(700, 0, wall_height/2), (wall_thick, 1000.0, wall_height), "Wall_Outer_East")
    spawn_box_actor(subsystem, unreal.Vector(-700, 0, wall_height/2), (wall_thick, 1000.0, wall_height), "Wall_Outer_West")

    # 3. Central Corridor (X from -700 to +700, Y between -75 and +75, width 150cm)
    # Corridor Wall North with 2 door openings (90cm wide each)
    # North room 1 (Salon: X: -700 to 0), North room 2 (Kitchen: X: 0 to +700)
    spawn_box_actor(subsystem, unreal.Vector(-450, 75, wall_height/2), (400.0, wall_thick, wall_height), "Wall_Corridor_N1")
    # Door 1 opening at X=-200 (width 100cm)
    spawn_box_actor(subsystem, unreal.Vector(50, 75, wall_height/2), (400.0, wall_thick, wall_height), "Wall_Corridor_N2")
    # Door 2 opening at X=+300 (width 100cm)
    spawn_box_actor(subsystem, unreal.Vector(550, 75, wall_height/2), (300.0, wall_thick, wall_height), "Wall_Corridor_N3")

    # Corridor Wall South with 2 door openings
    # South room 1 (Bedroom: X: -700 to 0), South room 2 (Office: X: 0 to +700)
    spawn_box_actor(subsystem, unreal.Vector(-450, -75, wall_height/2), (400.0, wall_thick, wall_height), "Wall_Corridor_S1")
    # Door 3 opening at X=-200
    spawn_box_actor(subsystem, unreal.Vector(50, -75, wall_height/2), (400.0, wall_thick, wall_height), "Wall_Corridor_S2")
    # Door 4 opening at X=+300
    spawn_box_actor(subsystem, unreal.Vector(550, -75, wall_height/2), (300.0, wall_thick, wall_height), "Wall_Corridor_S3")

    # 4. Room Divider Walls
    # Between Salon and Kitchen (X=0, Y from 75 to 500)
    spawn_box_actor(subsystem, unreal.Vector(0, 287.5, wall_height/2), (wall_thick, 425.0, wall_height), "Wall_Divider_North")
    # Between Bedroom and Office (X=0, Y from -75 to -500)
    spawn_box_actor(subsystem, unreal.Vector(0, -287.5, wall_height/2), (wall_thick, 425.0, wall_height), "Wall_Divider_South")

    # 5. Obstacles & Furniture for SLAM & Sonar Testing
    # Living room coffee table (80x60x40 cm)
    spawn_box_actor(subsystem, unreal.Vector(-350, 300, 20), (80.0, 60.0, 40.0), "Obstacle_Table")
    # Living room sofa block (200x80x70 cm)
    spawn_box_actor(subsystem, unreal.Vector(-350, 450, 35), (200.0, 80.0, 70.0), "Obstacle_Sofa")
    # Kitchen Counter (L-Shape / bar: 180x60x90 cm)
    spawn_box_actor(subsystem, unreal.Vector(350, 400, 45), (180.0, 60.0, 90.0), "Obstacle_Counter")
    # Bedroom Bed (200x160x50 cm)
    spawn_box_actor(subsystem, unreal.Vector(-350, -320, 25), (200.0, 160.0, 50.0), "Obstacle_Bed")
    # Office Desk (140x70x75 cm)
    spawn_box_actor(subsystem, unreal.Vector(350, -320, 37.5), (140.0, 70.0, 75.0), "Obstacle_Desk")

    # 6. Basic Lighting
    light_class = unreal.PointLight
    # Living room light
    subsystem.spawn_actor_from_class(light_class, unreal.Vector(-350, 300, 220), unreal.Rotator(0,0,0))
    # Kitchen light
    subsystem.spawn_actor_from_class(light_class, unreal.Vector(350, 300, 220), unreal.Rotator(0,0,0))
    # Corridor light
    subsystem.spawn_actor_from_class(light_class, unreal.Vector(0, 0, 220), unreal.Rotator(0,0,0))
    # Bedroom light
    subsystem.spawn_actor_from_class(light_class, unreal.Vector(-350, -300, 220), unreal.Rotator(0,0,0))
    # Office light
    subsystem.spawn_actor_from_class(light_class, unreal.Vector(350, -300, 220), unreal.Rotator(0,0,0))

    print("[ApartmentGen] Successfully generated 4-room apartment with doors and obstacle furniture!")

if __name__ == '__main__':
    build_apartment()
