# Copy this helper into game/everyday_weather/ beside weather_manifest.json
# and PNG/native/. No start label, settings override or required UI companion.
init -20 python:
    if not hasattr(store, "el_weather_root"):
        el_weather_root = "everyday_weather"

init -10 python:
    import json
    def el_weather_path(path):
        return (el_weather_root + "/" if el_weather_root else "") + path

    with renpy.file(el_weather_path("weather_manifest.json")) as _el_weather_stream:
        el_weather_manifest = json.load(_el_weather_stream)
    el_weather_effects = {effect["id"]: effect for effect in el_weather_manifest["effects"]}

    def el_weather(effect, animated=True, mask=None):
        """Native frames keep texture memory lower at every virtual resolution.
        mask: optional PNG or displayable at the game's virtual canvas size.
        Use the same show tag when switching effects. Keep dialogue above it.
        """
        item = el_weather_effects[effect]
        template = item["exports"]["native"]["template"]
        if animated:
            args = []
            for index in range(item["frames"]):
                args.extend((Image(el_weather_path(template.format(frame=index)), mipmap=False), item["frame_duration_seconds"]))
            child = Animation(*args)
        else:
            child = Image(el_weather_path(template.format(frame=0)), mipmap=False)
        child = Transform(child, xysize=(config.screen_width, config.screen_height), nearest=True,
                          xpos=0, ypos=0, xanchor=0.0, yanchor=0.0)
        return AlphaMask(child, mask) if mask is not None else child

# ------------------------------------------------------------
# IMAGE DEFINITIONS UNTUK ANIMASI CUACA
# Bisa dipanggil di script:
#   show weather petals / show weather gerimis / hide weather
# ------------------------------------------------------------
image weather petals = el_weather("petals")
image weather falling_leaves = el_weather("falling_leaves")
image weather light_rain = el_weather("light_rain")
image weather heavy_rain = el_weather("heavy_rain")
image weather drifting_fog = el_weather("drifting_fog")
image weather snow = el_weather("snow")

# Alias dalam bahasa Indonesia
image weather kelopak = el_weather("petals")
image weather daun = el_weather("falling_leaves")
image weather gerimis = el_weather("light_rain")
image weather hujan = el_weather("heavy_rain")
image weather kabut = el_weather("drifting_fog")
