@file:Suppress("PackageName")

package com.Remisaurus.Dumbass.systems

import com.Remisaurus.Dumbass.component.ImageComponent
import com.badlogic.gdx.scenes.scene2d.Stage
import com.github.quillraven.fleks.*

@AllOf([ImageComponent::class])
class RenderSystem(
    private val stage:Stage
) : IteratingSystem()  {
    override fun onTick() {
        super.onTick()
        with(stage){
            viewport.apply()
            act(deltaTime)
            draw()
        }
    }
    override fun onTickEntity(entity: Entity) {
        TODO("Not yet implemented")
    }

    override fun onDispose() {
        super.onDispose()
    }
}
