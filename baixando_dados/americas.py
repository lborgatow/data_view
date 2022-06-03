from pygal_maps_world.maps import World

mm = World()
mm.title = 'América do Norte, Central e Sul'
mm.add('América do Norte', ['ca', 'mx', 'us'])
mm.add('América Central', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
mm.add('América do Sul', ['ar', 'bo', 'br', 'cl', 'co',
                          'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

mm.render_to_file('americas.svg')
