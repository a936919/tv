package com.fongmi.android.tv.player.exo;

import androidx.media3.common.MediaItem;
import androidx.media3.exoplayer.ExoPlayer;

/** Source-build fallback when the unpublished disk preloader extension isn't bundled. */
public class PreCache {

    public void start(ExoPlayer player, MediaItem mediaItem) {
    }

    public void stop() {
    }

    public void release() {
        stop();
    }
}
