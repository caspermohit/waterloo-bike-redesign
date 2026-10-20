# Scroll and text motion — version 9

Bicycle assembly now follows native scroll progress with time-based exponential easing (130ms response constant), updating only while movement is pending. Headings, captions and background words fade and translate gently between stages, with stale transitions cancelled when scrolling quickly. Arrow labels fade at stage boundaries. Reserved text space prevents paragraph/headline changes from shifting the bicycle. The anatomy scroll distance is slightly shorter.

Reduced-motion mode keeps immediate controls and disables caption animations. Background tabs cancel animation frames.

Checked desktop and 390px mobile: controls settle at their target; captions follow the final stage; no horizontal overflow or JavaScript errors. Reduced-motion controls update immediately.
