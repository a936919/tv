package com.fongmi.android.tv.player.mpv;

/** Source-build fallback for the optional MPV Media3 extension. */
public final class MpvUtil {

    private MpvUtil() {
    }

    public static boolean isAvailable() {
        return false;
    }
}
