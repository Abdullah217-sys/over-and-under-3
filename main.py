def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        empty cave
        """),
    on_overlap_tile)

def on_a_pressed():
    truck.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        spikes
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        acid
        """),
    on_overlap_tile3)

truck: Sprite = None
truck = sprites.create(assets.image("""
    truck2
    """), SpriteKind.player)
truck.ay = 500
truck.vx = 100
scene.camera_follow_sprite(truck)