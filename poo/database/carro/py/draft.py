class Carro:
    def __init__(self, pas: int, gas: int, km: int):
        self.pas: int = 0
        self.km: int = 0
        self.gas: int = 0
    
    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def entrada(self):
        if self.pas < 2:
              self.pas += 1
        else:
             print("fail: limite de pessoas atingido")

    def saida(self):
         if self.pas == 0:
              print("fail: nao ha ninguem no carro")
         else:
              self.pas -= 1

    def receba(self, increment: int):
         self.gas += increment
         if self.gas > 100:
              self.gas = 100

    def digirador(self, distance: int):
        if self.pas == 0:
              print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
             print('fail: tanque vazio')
        else:
            if distance > self.gas:
                  print(f"fail: tanque vazio apos andar {self.gas} km")
                  self.km += self.gas
                  self.gas = 0
            else:
                self.km += distance
                self.gas -= distance      

        
              



def main():
     carro: Carro = Carro("", "", "")
     while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        
        if args[0] == "end":
                 break
        elif args[0] == "show":
             print(carro)
        elif args[0] == "enter":
             carro.entrada()
        elif args[0] == "leave":
             carro.saida()
        elif args[0] == "fuel":
             increment = int(args[1])
             carro.receba(increment)
        elif args[0] == "drive":
             increment = int(args[1])
             carro.digirador(increment)
        

main()