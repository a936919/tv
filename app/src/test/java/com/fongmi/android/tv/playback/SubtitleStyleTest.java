package com.fongmi.android.tv.playback;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SubtitleStyleTest {
    @Test
    public void textSizeIsClampedToReadableRange() {
        assertEquals(SubtitleStyle.MIN_TEXT_SIZE, SubtitleStyle.clampTextSize(0.001f), 0.0001f);
        assertEquals(0.0533f, SubtitleStyle.clampTextSize(0.0533f), 0.0001f);
        assertEquals(SubtitleStyle.MAX_TEXT_SIZE, SubtitleStyle.clampTextSize(1.0f), 0.0001f);
    }

    @Test
    public void positionStaysInsidePlayerSafeArea() {
        assertEquals(SubtitleStyle.MIN_POSITION, SubtitleStyle.clampPosition(-1.0f), 0.0001f);
        assertEquals(0.0f, SubtitleStyle.clampPosition(0.0f), 0.0001f);
        assertEquals(SubtitleStyle.MAX_POSITION, SubtitleStyle.clampPosition(1.0f), 0.0001f);
    }
}
