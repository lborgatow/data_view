from pygal_maps_world.i18n import COUNTRIES


def obter_codigo_pais(nome_pais):
    """Devolve o código de duas letras do Pygal para
    um país, dado o seu nome"""
    for codigo, nome in COUNTRIES.items():
        if nome == nome_pais:
            return codigo
    # Se o país não foi encontrado, devolve None
    return None