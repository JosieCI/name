input.onButtonPressed(Button.A, function () {
    player.move(-1)
})
input.onPinPressed(TouchPin.P2, function () {
    game.resume()
})
input.onButtonPressed(Button.AB, function () {
    game.pause()
})
input.onButtonPressed(Button.B, function () {
    player.move(1)
})
let coin: game.LedSprite = null
let Enemy: game.LedSprite = null
let player: game.LedSprite = null
for (let index = 0; index < 3; index++) {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . # . # .
        . # # # .
        . . # . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . # .
        . # # # .
        . . # . .
        . . . . .
        `)
}
basic.clearScreen()
basic.showLeds(`
    . # # # .
    # . . . #
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . # # # .
    # . . . #
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . # # # .
    # . . . #
    # . . . #
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . # . .
    . # . # .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . # . .
    `)
basic.pause(100)
player = game.createSprite(2, 4)
basic.forever(function () {
    Enemy = game.createSprite(randint(0, 4), 0)
    Enemy.set(LedSpriteProperty.Brightness, 100)
    basic.pause(100)
    Enemy.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        Enemy.move(1)
        basic.pause(500)
    }
    if (Enemy.isTouchingEdge()) {
        Enemy.delete()
    }
})
basic.forever(function () {
    coin = game.createSprite(randint(0, 4), 0)
    coin.set(LedSpriteProperty.Brightness, 250)
    basic.pause(200)
    coin.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        coin.move(1)
        basic.pause(1000)
    }
    if (coin.isTouchingEdge()) {
        coin.delete()
        game.gameOver()
    }
})
basic.forever(function () {
    if (game.isPaused()) {
        Enemy.delete()
        coin.delete()
    }
})
basic.forever(function () {
    if (Enemy.isTouching(player)) {
        player.delete()
        game.gameOver()
    }
})
basic.forever(function () {
    if (coin.isTouching(player)) {
        Enemy.delete()
    }
})
basic.forever(function () {
    if (coin.isTouching(player)) {
        coin.delete()
        game.addScore(1)
    }
})
