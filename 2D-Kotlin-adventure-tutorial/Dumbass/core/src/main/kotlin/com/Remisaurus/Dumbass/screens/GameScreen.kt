@file:Suppress("PackageName")

package com.Remisaurus.Dumbass.screens

import com.Remisaurus.Dumbass.systems.RenderSystem
import com.badlogic.gdx.graphics.Texture
import com.badlogic.gdx.scenes.scene2d.Stage
import com.badlogic.gdx.scenes.scene2d.ui.Image
import com.badlogic.gdx.utils.Scaling
import com.badlogic.gdx.utils.viewport.ExtendViewport
import com.github.quillraven.fleks.World
import ktx.app.KtxScreen
import ktx.assets.disposeSafely
import ktx.log.logger

class GameScreen : KtxScreen {
    private val stage: Stage = Stage(ExtendViewport(16f, 9f ))
    private val texture: Texture = Texture("assets/images/player.png")

    private val world: World = World {
        inject(stage)
        system<RenderSystem>()

    }

    override fun show() {
        log.debug {"GameScreen get shown"}
        stage.addActor(
            Image(texture).apply {
                setPosition(1f, 1f)
                setSize(1f,1f)
                setScaling(Scaling.fill)
            }
        )
    }

    override fun resize(width: Int, height: Int) {
        stage.viewport.update(width, height, true)
    }

    override fun render(delta: Float) {
        world.update(delta)
    }

    override fun dispose() {
        stage.disposeSafely()
        texture.disposeSafely()
        world.dispose()
    }

    companion object {
        val log = logger<GameScreen>()
    }

}
