class Book(object):
    def __init__(self, titulo: str, autor: str, desc: str, preco: float):
        self.titulo = titulo
        self.autor = autor
        self.desc = desc
        self.preco = preco