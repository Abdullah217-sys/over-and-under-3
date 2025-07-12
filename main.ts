scene.onOverlapTile(SpriteKind.Player, assets.tile`
        empty cave
        `, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.over(true)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    truck.vy = -200
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        spikes
        `, function on_overlap_tile2(sprite2: Sprite, location2: tiles.Location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        acid
        `, function on_overlap_tile3(sprite3: Sprite, location3: tiles.Location) {
    game.over(false)
})
let truck : Sprite = null
truck = sprites.create(assets.image`
    truck2
    `, SpriteKind.Player)
truck.ay = 500
truck.vx = 100
scene.cameraFollowSprite(truck)
