from unicodedata import normalize

class TextUtil :
    """
	Classe com métodos para tratamento de texto
	"""
    def removerCaracteresEspeciais (self, text):
        text=text.replace("\\n"," ")
        text=text.replace("\\r"," ")
        text=text[:150]
        return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
