class Produto:
    def __init__(self, nome, preco, categoria, fabricante, validade):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.fabricante = fabricante
        self.validade = validade
        
    def set_nome(self, nome):
        self.nome = nome
    
    def set_preco(self, preco):
        self.preco = preco
        
    def set_categoria(self, categoria):
        self.categoria = categoria
    
    def set_fabricante(self, fabricante):
        self.fabricante = fabricante
    
    def set_validade(self, validade):
        self.validade = validade
        
    def get_nome(self):
        return self.nome
    
    def get_preco(self):
        return self.preco
        
    def get_categoria(self):
        return self.categoria
    
    def get_fabricante(self):
        return self.fabricante
    
    def get_validade(self):
        return self.validade  
        
    