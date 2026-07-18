class Tulip:
    def __init__(self,name,fragrance):
        self.n=name
        self.fra=fragrance
    def appearance(self):
       print("Name of flower:",self.n,"\n","Scent:",self.fra)



class Dahlia(Tulip):
    def __init__(self,name,fragrance):
        self.n=name
        self.fra=fragrance
    def appear(self):
       print("Name of flower:",self.n,"\n","Scent:",self.fra)



class merigold(Dahlia):
    def __init__(self,name,fragrance):
        self.n=name
        self.fra=fragrance
    def show(self):
       print("Name of flower:",self.n,"\n","Scent:",self.fra)

        


t=Tulip("tulip","subtle and airy")
d=Dahlia("Dahlia","Most dahlias are scentless")
m=merigold("Merigold","Soft and fent")


t.appearance()
d.appear()
m.show()