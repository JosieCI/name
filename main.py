def on_pin_pressed_p2():
    game.resume()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    game.pause()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

coin: game.LedSprite = None
Enemy: game.LedSprite = None
for index in range(3):
    basic.show_leds("""
        . # . # .
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . # # # .
                . . # . .
                . . . . .
    """)
basic.clear_screen()
basic.show_leds("""
    . # # # .
        # . . . #
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . # # # .
        # . . . #
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . # # # .
        # . . . #
        # . . . #
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . # . .
        . # . # .
""")
basic.pause(100)
player = game.create_sprite(2, 4)

def on_forever():
    if input.is_gesture(Gesture.TILT_RIGHT):
        player.move(1)
        basic.pause(200)
basic.forever(on_forever)

def on_forever2():
    if input.is_gesture(Gesture.TILT_LEFT):
        player.move(-1)
        basic.pause(200)
basic.forever(on_forever2)

def on_forever3():
    global Enemy
    Enemy = game.create_sprite(randint(0, 4), 0)
    Enemy.set(LedSpriteProperty.BRIGHTNESS, 100)
    basic.pause(100)
    Enemy.turn(Direction.RIGHT, 90)
    for index2 in range(4):
        Enemy.move(1)
        basic.pause(500)
    if Enemy.is_touching_edge():
        Enemy.delete()
basic.forever(on_forever3)

def on_forever4():
    global coin
    coin = game.create_sprite(randint(0, 4), 0)
    coin.set(LedSpriteProperty.BRIGHTNESS, 200)
    basic.pause(200)
    coin.turn(Direction.RIGHT, 90)
    for index3 in range(4):
        coin.move(1)
        basic.pause(1000)
    if coin.is_touching_edge():
        coin.delete()
        game.game_over()
basic.forever(on_forever4)

def on_forever5():
    if game.is_paused():
        Enemy.delete()
        coin.delete()
basic.forever(on_forever5)

def on_forever6():
    if Enemy.is_touching(player):
        player.delete()
        game.game_over()
basic.forever(on_forever6)

def on_forever7():
    if coin.is_touching(player):
        Enemy.delete()
basic.forever(on_forever7)

def on_forever8():
    if coin.is_touching(player):
        coin.delete()
        game.add_score(1)
basic.forever(on_forever8)
