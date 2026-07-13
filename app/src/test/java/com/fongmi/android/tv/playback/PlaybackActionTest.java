package com.fongmi.android.tv.playback;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class PlaybackActionTest {
    @Test
    public void aiSubtitleMakesTextActionVisibleWithoutMediaTrack() {
        assertTrue(PlaybackAction.shouldShowTextAction(false, false, true));
        assertTrue(PlaybackAction.isAiOnlySubtitle(false, false, true));
    }

    @Test
    public void liveWithoutAnySubtitleKeepsTextActionHidden() {
        assertFalse(PlaybackAction.shouldShowTextAction(false, false, false));
        assertFalse(PlaybackAction.isAiOnlySubtitle(false, false, false));
    }

    @Test
    public void mediaTrackAndVodKeepTheirExistingBehavior() {
        assertTrue(PlaybackAction.shouldShowTextAction(true, false, false));
        assertTrue(PlaybackAction.shouldShowTextAction(false, true, false));
        assertFalse(PlaybackAction.isAiOnlySubtitle(true, false, true));
        assertFalse(PlaybackAction.isAiOnlySubtitle(false, true, true));
    }
}
