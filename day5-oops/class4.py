
# static method , class method
class Product:
    id=10
    address='hyd'
    def __init__(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
        #instance method
    def ishow(self):
        print(self.name,self.qty,self.price)
    @classmethod  
    def show(cls):
        cls.mname='sony'
        cls.id=15
        print(cls.mname)
        print(cls.address)
        Product.id=Product.id+20
        print(cls.id)
    @staticmethod
    def disp():
        print(Product.mname)
        print(Product.address)
        Product.id=Product.id+20
        print(Product.id)
        
p=Product('box',90,999)
print(p.price,p.name,p.qty)

p1=Product('table',80,9934)
print(Product.id)
p.ishow()
p.show()
p.disp()
Product.disp()
Product.show()



