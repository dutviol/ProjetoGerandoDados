# import pygal_maps_world
# import pygal

# wm = pygal.WorldMaps()

from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'

wm.title="Map of Central America"
wm.add('North America',{'ca': 84949494949,'mx': 494794164,'us': 99794616})

wm.render_to_file('map.svg')