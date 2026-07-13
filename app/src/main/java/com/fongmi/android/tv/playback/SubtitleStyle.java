package com.fongmi.android.tv.playback;

public final class SubtitleStyle {
    public static final float MIN_TEXT_SIZE = 0.030f;
    public static final float MAX_TEXT_SIZE = 0.090f;
    public static final float MIN_POSITION = -0.050f;
    public static final float MAX_POSITION = 0.450f;

    private SubtitleStyle() {
    }

    public static float clampTextSize(float value) {
        return Math.clamp(value, MIN_TEXT_SIZE, MAX_TEXT_SIZE);
    }

    public static float clampPosition(float value) {
        return Math.clamp(value, MIN_POSITION, MAX_POSITION);
    }
}
