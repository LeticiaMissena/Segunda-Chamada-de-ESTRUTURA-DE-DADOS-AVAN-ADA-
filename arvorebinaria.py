import json
valores_json = """ { "values": [50, 30, 20, 40, 70, 60, 80] } """
values = json.loads(valores_json)

class No:
     
     def __init__(self, key, dir, esq):
          self.item = key
          self.dir = dir
          self.esq = esq

class Tree:

    def __init__(self):
        self.root = No(None,None,None)
        self.root = None

    def inserir(self, v):
        novo = No(v,None,None)
        if self.root == None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item:
                        atual = atual.esq
                        if atual == None:
                            anterior.esq = novo
                            return                   
                else:
                        atual = atual.dir
                        if atual == None:
                                anterior.dir = novo
                                return

    def altura(self, atual):
        if atual == None or atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
              return  1 + self.altura(atual.esq) 
            else:
              return  1 + self.altura(atual.dir) 

    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esq == None and atual.dir == None:
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)


    def contarNos(self, atual):
        if atual == None:
            return 0
        else:
            return  1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(atual.item,end=" ")
            self.inOrder(atual.dir)

    def preOrder(self, atual):
        if atual != None:
            print(atual.item,end=" ")
            self.preOrder(atual.esq)
            self.preOrder(atual.dir)
    
    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esq)
            self.posOrder(atual.dir)
            print(atual.item,end=" ")

    def caminhar(self):
          print(" Exibindo em ordem: ",end="")
          self.inOrder(self.root)
          print("\n Exibindo em pos-ordem: ",end="")
          self.posOrder(self.root)
          print("\n Exibindo em pre-ordem: ",end="")
          self.preOrder(self.root)
          print("\n Altura da arvore: %d" %(self.altura(self.root)))
          print(" Quantidade de folhas: %d"  %(self.folhas(self.root)))
          print(" Quantidade de Nós: %d" %(self.contarNos(self.root)))

arvore = Tree()
for i in values['values']:
    arvore.inserir(i)

print(arvore.caminhar())