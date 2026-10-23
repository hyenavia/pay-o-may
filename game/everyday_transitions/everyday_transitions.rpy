# Everyday Life Scene Transitions - Ren'Py 8.x
# Copy this file and masks/ into your game's game/ folder.
# Masks are technical grayscale control images, not visible artwork.
# Change _720p to _1080p for 1920x1080 games, or remove it for 640x360.
# Usage: scene your_next_background; with el_shoreline_sweep

define el_shoreline_sweep = ImageDissolve("everyday_transitions/masks/el_transition_shoreline_sweep_1080p.png", 0.64, ramplen=1)
define el_sunset_horizon = ImageDissolve("everyday_transitions/masks/el_transition_sunset_horizon_1080p.png", 0.64, ramplen=1)
define el_train_doors = ImageDissolve("everyday_transitions/masks/el_transition_train_doors_1080p.png", 0.64, ramplen=1)
define el_lantern_glow = ImageDissolve("everyday_transitions/masks/el_transition_lantern_glow_1080p.png", 0.64, ramplen=1)
define el_mosaic_tiles = ImageDissolve("everyday_transitions/masks/el_transition_mosaic_tiles_1080p.png", 0.64, ramplen=1)
define el_diamond_iris = ImageDissolve("everyday_transitions/masks/el_transition_diamond_iris_1080p.png", 0.64, ramplen=1)
define el_crosswalk = ImageDissolve("everyday_transitions/masks/el_transition_crosswalk_1080p.png", 0.64, ramplen=1)
define el_postcard_diagonal = ImageDissolve("everyday_transitions/masks/el_transition_postcard_diagonal_1080p.png", 0.64, ramplen=1)

# Faster alternatives for frequent room changes.
define el_quick_cut = None
define el_soft_fade = Fade(0.16, 0.02, 0.16, color="#25243e")
