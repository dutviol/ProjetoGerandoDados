from pygal_maps_world.maps import COUNTRIES
import code

def get_country_code(country_name):
    """Devolver o código de duas letras do Pygal para um país, dado o seu nome """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        
    # Se o país não for encontrado retornar none
    return None
        
# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))