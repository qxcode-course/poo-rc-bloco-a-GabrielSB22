class Towel: 
 def __init__(self, color: str, size: str): #construção do obj
  self.color: str = color #atributos do obj
  self.size: str = size
  self.wetness: int = 0


print("Qual é a cor e o tamanho da sua toalha? :")
color = input()
size = input()
towel: Towel = Towel(color, size)
print(f"Sua toalha é {towel.color} e {towel.size}")