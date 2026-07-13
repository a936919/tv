package com.fongmi.android.tv.playback;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class PlaybackActionTest {
    @Test
    public void aiSubtitleMakesTextActionVisibleWithoutMediaTrack() {
        assertEquals(PlaybackAction.SubtitleEntry.STYLE, PlaybackAction.getSubtitleEntry(false, false, true));
        assertTrue(PlaybackAction.shouldShowSubtitleStyle(false, true));
    }

    @Test
    public void liveWithoutAnySubtitleKeepsTextActionHidden() {
        assertEquals(PlaybackAction.SubtitleEntry.HIDDEN, PlaybackAction.getSubtitleEntry(false, false, false));
        assertFalse(PlaybackAction.shouldShowSubtitleStyle(false, false));
    }

    @Test
    public void mediaTrackUsesTrackDialogAndAllowsStyle() {
        assertEquals(PlaybackAction.SubtitleEntry.TRACKS, PlaybackAction.getSubtitleEntry(true, false, false));
        assertEquals(PlaybackAction.SubtitleEntry.TRACKS, PlaybackAction.getSubtitleEntry(true, false, true));
        assertTrue(PlaybackAction.shouldShowSubtitleStyle(true, false));
    }

    @Test
    public void vodWithoutMediaTrackRetainsLocalChoiceAndAddsAiStyle() {
        assertEquals(PlaybackAction.SubtitleEntry.TRACKS, PlaybackAction.getSubtitleEntry(false, true, false));
        assertEquals(PlaybackAction.SubtitleEntry.TRACKS, PlaybackAction.getSubtitleEntry(false, true, true));
        assertFalse(PlaybackAction.shouldShowSubtitleStyle(false, false));
        assertTrue(PlaybackAction.shouldShowSubtitleStyle(false, true));
    }
}
