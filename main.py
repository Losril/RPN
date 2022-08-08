#HELENA KUCHINSKI FERREIRA
#FAZER UMA CALCULADORA ARITMETICA CAPAZ DE REALIZAR AS OPERACOES ADICAO, SUBTRACAO, DIVISAO E MULTIPLICACAO DIGITADAS NA SEGUINTE FORMA REVERSIVA
#(34+) (2(65+)+)

class Guarda:
  valores = None
  prox = None
  def __init__(self, valores):
    self.valores = valores

class Pilha:
  topo = None
  def __init__(self):
    self.topo = None
    
  def push(self, valor):
    auxiliador = Guarda(valor)
    if self.topo == None:
      self.topo = auxiliador
    else:
      auxiliador.prox = self.topo
      self.topo = auxiliador
    
  def pop(self):
    if self.topo != None:
      reserva = self.topo.valores
      self.topo = self.topo.prox
      return reserva
    else:
      return None

  def print_topo(self):
    if self.topo == None:
      return None
    else:
      return self.topo.valores

#PRINCIPAL
      
entrada = input("Insira o expressao desejada de acordo com o exemplo abaixo:\n\n(3 4+) | (2 (6 9*)-).\n\nExpressao: ")

pilhaHOT = Pilha()
pilhaSTANDBY = Pilha()

Findex = "("
Lindex = "("

Findex2 = "("
Lindex2 = "("

for i in entrada:
  if i in ["(", ")", "+", "-", "/", "*"]:
    pilhaHOT.push(i)
    
  else:
    if i in ["(", ")", "+", "-", "/", "*"," ", "."] or i in entrada[entrada.index(Findex):entrada.index(Lindex)]:
      pass
      
    else:
      string = ""
      Findex = i
      for j in (entrada[entrada.index(i):]):
        if j in ["(", ")", "+", "-", "/", "*"," ", "."]:
          Lindex = j
          break
          
        else:
          string += j
      pilhaHOT.push(string)  

while True:
  while pilhaHOT.print_topo() != "(":
    pilhaSTANDBY.push(pilhaHOT.pop())

  num1 = pilhaSTANDBY.pop()
  num2 = pilhaSTANDBY.pop()
  operacao = pilhaSTANDBY.pop()
  
  pilhaSTANDBY.pop()
  
  if operacao == "+":
    n1 = float(num1)
    n2 = float(num2)
    resultado = n1 + n2
    
  elif operacao == "-":
    n1 = float(num1)
    n2 = float(num2)
    resultado = n1 - n2
    
  elif operacao == "/":
    n1 = float(num1)
    n2 = float(num2)
    resultado = n1 / n2

  elif operacao == "*":
    n1 = float(num1)
    n2 = float(num2)
    resultado = n1 * n2
    
  pilhaHOT.pop()
  
  if pilhaHOT.print_topo() == None:
    break
    
  pilhaHOT.push(resultado)
  
  while pilhaSTANDBY.print_topo() != None:
    pilhaHOT.push(pilhaSTANDBY.pop())

print("O resultado de sua expressao é: ", resultado)
        





  

