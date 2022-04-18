import re
def unidas_(string,palabra1,palabra2):
    return bool(re.search(palabra1 + "_" + palabra2, string))
print(unidas_("maia", "carroll", "18 anos"))
print(unidas_("maia carroll_capa", "carroll", "18 anos"))