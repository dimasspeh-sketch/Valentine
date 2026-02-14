# 🎵 Music Setup Guide - Valentine's Day Website

## Overview
The website includes background music functionality. The music file needs to be placed in the root directory of the project.

## Setup Instructions

### Step 1: Prepare Your Music File
1. Choose a romantic music file or download one
2. Convert it to **MP3 format** (if not already)
3. Keep the file size reasonable (under 10MB for web use)

### Step 2: Place the Music File
- **Filename:** `song.mp3`
- **Location:** Place in the same directory as `index.html`
- **Path:** `d:\valentine vaniaa\music.mp3`

### Step 3: Test the Audio
1. Open the website in a browser
2. Click the 🔊 button in the top-right corner to toggle music
3. Music should start playing automatically (if autoplay is allowed by browser)

## Audio Files Recommendations

### Romantic Piano Pieces
- "Moonlight Sonata" by Beethoven
- "Claire de Lune" by Claude Debussy
- "River Flows in You" by Yiruma

### Soft Background Music
- Instrumental love songs
- Ambient romantic compilations
- Lo-fi romantic beats

## Browser Compatibility

### Autoplay Policy
- Modern browsers require user interaction before playing audio
- The `🔊` button allows users to control music playback
- First page automatically attempts to play music

### Supported Browsers
- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (with user interaction)

## Music Control Features

### Music Toggle Button
- **Location:** Top-right corner of the page
- **Shows:** 🔊 (music on) or 🔇 (music off)
- **Function:** Click to play/pause music
- **Responsive:** Works on mobile and desktop

### Audio Settings
- **Volume:** 30% (can be adjusted in code)
- **Loop:** Music loops continuously when enabled
- **Persistent:** User preference is saved in localStorage

## Technical Details

### HTML Audio Tag
```html
<audio id="bg-music" loop volume="0.3">
    <source src="music.mp3" type="audio/mpeg">
</audio>
```

### JavaScript Control
The music is controlled via JavaScript functions:
- `initializeMusic()` - Initializes music system on page load
- Click handler for play/pause toggling
- localStorage for user preference persistence

## Troubleshooting

### Music Not Playing?
1. **Check file location:** Ensure `music.mp3` is in the root directory
2. **Check file format:** Ensure file is valid MP3
3. **Browser settings:** Some browsers block autoplay without user interaction
4. **Click the 🔊 button:** User interaction may be required

### Audio Quality Issues?
1. Reduce file size by lowering bitrate (128 kbps is sufficient)
2. Use an audio converter if needed
3. Ensure original file is high quality

### Volume Too Loud/Quiet?
- Edit `script.js` and change: `bgMusic.volume = 0.3;`
- Use a value between 0 (silent) and 1 (maximum)

## Advanced Customization

### Change Volume
In `script.js`, find `initializeMusic()` function:
```javascript
bgMusic.volume = 0.3;  // Change 0.3 to desired level (0-1)
```

### Add Multiple Tracks
Modify the HTML audio element:
```html
<audio id="bg-music" loop>
    <source src="music1.mp3" type="audio/mpeg">
    <source src="music2.mp3" type="audio/mpeg">
    <source src="music3.mp3" type="audio/mpeg">
</audio>
```

### Disable on Mobile
Add this to prevent autoplay on mobile:
```javascript
const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
if (!isMobile) {
    bgMusic.autoplay = true;
}
```

## Copyright & Licensing
- Use royalty-free music or properly licensed tracks
- Recommended sources:
  - YouTube Audio Library
  - Incompetech
  - FreePM
  - Pixabay Music
  - Epidemic Sound

---

**Note:** Always respect copyright and licensing when using music files!
