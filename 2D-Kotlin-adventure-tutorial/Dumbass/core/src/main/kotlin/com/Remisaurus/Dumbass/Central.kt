@file:Suppress("PackageName")

package com.Remisaurus.Dumbass

import com.Remisaurus.Dumbass.screens.GameScreen
import com.badlogic.gdx.Application
import com.badlogic.gdx.Gdx
import ktx.app.KtxGame
import ktx.app.KtxScreen

class Central : KtxGame<KtxScreen>() {
    override fun create() {
        Gdx.app.logLevel = Application.LOG_DEBUG
        addScreen(GameScreen())
        setScreen<GameScreen>()
    }
}
