from pygal_maps_world.maps import World


mm = World()
mm.title = 'População dos Países da América do Norte'
mm.add('América do Norte', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
mm.render_to_file('an_populacoes.svg')
