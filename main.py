import random
import numpy as np
import builtins

population_size=1000

population=[None]*(population_size*16*4)
population=np.array(population).reshape(population_size,16,4)

gates=['and','or','buffer','nor','nand','xor','xnor']
fitness=[]
answer=[]

def Binary(decimal_number):
  binary_array=[0]*4
  for i in range(3,-1,-1):
    binary_array[i]=int(decimal_number%2)
    decimal_number=decimal_number//2
  return binary_array

inputs = []
output = []
in_out = []

for i in range(16):

    inputs.append(Binary(i))
    output.append(int(builtins.input(f"Write the output for input {i}: ")))

in_out.append(inputs)
in_out.append(output)


# for i in range(16):
#   output.append(int(input(f" write the output for input {i},: ")))
  # if i<4 and i>12:
  #   output.append(0)
  # else:
  #   output.append(1)
  # input.append(Binary(i))

  # output.append(random.randint(0,1))
  # input.append(Binary(i))

inputs=np.array(inputs).reshape(16,4)
output=np.array(output).reshape(16,1)
for p in range(population_size):
  for i in range(4):
    population[p][i][0]=random.randint(0,3)
    population[p][i][1]=random.randint(0,3)
    population[p][i][2]=random.choice(gates)
  for i in range(4,8):
    population[p][i][0]=random.randint(0,3)
    population[p][i][1]=random.randint(0,3)
    population[p][i][2]=random.choice(gates)
  for i in range(8,12):
    population[p][i][0]=random.randint(4,7)
    population[p][i][1]=random.randint(4,7)
    population[p][i][2]=random.choice(gates)
  for i in range(12,16):
    population[p][i][0]=random.randint(8,11)
    population[p][i][1]=random.randint(8,11)
    population[p][i][2]=random.choice(gates)


def AND(x,y):
  return int(x and y)

def OR(x,y):
  return int(x or y)

def NAND(x,y):
  if x==y==1 :
    k=0
  else:
    k=1
  return int(k)

def NOR(x,y):
  if x==y==0 :
    k=1
  else:
    k=0
  return int(k)

def NOT(x):
  return int(not x)

def XOR(x,y):
  if x==y:
    return int(0)
  elif x!=y:
    return int(1)

def XNOR(x,y):
  if x==y:
    return int(1)
  elif x!=y:
    return int(0)

def findcelloutput(population,inputs):

  for i in range(len(population)):

    for j0 in range(4):
      v1=population[i][j0][0]
      v2=population[i][j0][1]
      if population[i][j0][2]=='and':
        population[i][j0][3]=AND(inputs[v1],inputs[v2])
      elif population[i][j0][2]=='or':
        population[i][j0][3]=OR(inputs[v1],inputs[v2])
      elif population[i][j0][2]=='nand':
        population[i][j0][3]=NAND(inputs[v1],inputs[v2])
      elif population[i][j0][2]=='nor':
        population[i][j0][3]=NOR(inputs[v1],inputs[v2])
      elif population[i][j0][2]=='not':
        population[i][j0][3]=NOT(inputs[v1])
      elif population[i][j0][2]=='buffer':
        population[i][j0][3]=inputs[v1]
      elif population[i][j0][2]=='xor':
        population[i][j0][3]=XOR(inputs[v1],inputs[v2])
      elif population[i][j0][2]=='xnor':
        population[i][j0][3]=XNOR(inputs[v1],inputs[v2])


    for j1 in range(4,8):
      v1=population[i][j1][0]
      v2=population[i][j1][1]
      if population[i][j1][2]=='and':
        population[i][j1][3]=AND(population[i][v1][3],population[i][v2][3])
      elif population[i][j1][2]=='or':
        population[i][j1][3]=OR(population[i][v1][3],population[i][v2][3])
      elif population[i][j1][2]=='nand':
        population[i][j1][3]=NAND(population[i][v1][3],population[i][v2][3])
      elif population[i][j1][2]=='nor':
        population[i][j1][3]=NOR(population[i][v1][3],population[i][v2][3])
      elif population[i][j1][2]=='not':
        population[i][j1][3]=NOT(population[i][v1][3])
      elif population[i][j1][2]=='buffer':
        population[i][j1][3]=population[i][v1][3]
      elif population[i][j1][2]=='xor':
        population[i][j1][3]=XOR(population[i][v1][3],population[i][v2][3])
      elif population[i][j1][2]=='xnor':
        population[i][j1][3]=XNOR(population[i][v1][3],population[i][v2][3])


    for j2 in range(8,12):
      v1=population[i][j2][0]
      v2=population[i][j2][1]
      if population[i][j2][2]=='and':
        population[i][j2][3]=AND(population[i][v1][3],population[i][v2][3])
      elif population[i][j2][2]=='or':
        population[i][j2][3]=OR(population[i][v1][3],population[i][v2][3])
      elif population[i][j2][2]=='nand':
        population[i][j2][3]=NAND(population[i][v1][3],population[i][v2][3])
      elif population[i][j2][2]=='nor':
        population[i][j2][3]=NOR(population[i][v1][3],population[i][v2][3])
      elif population[i][j2][2]=='not':
        population[i][j2][3]=NOT(population[i][v1][3])
      elif population[i][j2][2]=='buffer':
        population[i][j2][3]=population[i][v1][3]
      elif population[i][j2][2]=='xor':
        population[i][j2][3]=XOR(population[i][v1][3],population[i][v2][3])
      elif population[i][j2][2]=='xnor':
        population[i][j2][3]=XNOR(population[i][v1][3],population[i][v2][3])

    for j3 in range(12,16):
      v1=population[i][j3][0]
      v2=population[i][j3][1]
      if population[i][j3][2]=='and':
        population[i][j3][3]=AND(population[i][v1][3],population[i][v2][3])
      elif population[i][j3][2]=='or':
        population[i][j3][3]=OR(population[i][v1][3],population[i][v2][3])
      elif population[i][j3][2]=='nand':
        population[i][j3][3]=NAND(population[i][v1][3],population[i][v2][3])
      elif population[i][j3][2]=='nor':
        population[i][j3][3]=NOR(population[i][v1][3],population[i][v2][3])
      elif population[i][j3][2]=='not':
        population[i][j3][3]=NOT(population[i][v1][3])
      elif population[i][j3][2]=='buffer':
        population[i][j3][3]=population[i][v1][3]
      elif population[i][j3][2]=='xor':
        population[i][j3][3]=XOR(population[i][v1][3],population[i][v2][3])
      elif population[i][j3][2]=='xnor':
        population[i][j3][3]=XNOR(population[i][v1][3],population[i][v2][3])


  return population

def findfitness(population):
   global inputs
   global answer
   fitness1=[0]*len(population)
   for i in range(16):
      findcelloutput(population,inputs[i])
      for circuit in range(len(population)):
        if population[circuit][15][3]==output[i]:
          fitness1[circuit]+=1
          if fitness1[circuit]==16:
            answer.append(population[circuit])
   return fitness1

fitness=findfitness(population)






def elitism(population,fitness):
  elitism1=[None]*100
  top200=np.argsort(fitness)[-100:]
  for i in range(100):
    elitism1[i]=population[top200[i]]
  elitism1=np.array(elitism1).reshape(100,16,4)
  return elitism1
def selection(population,fitness):
  pop2=[]
  for i in range(900):
    s=random.randint(0,999)
    if fitness[i]>=fitness[s]:
      pop2.append(population[i])
    else:
      pop2.append(population[s])
  pop2=np.array(pop2).reshape(900,16,4)
  return pop2

def crossover(population):
  for i in range(len(population)):
      c=random.randint(0,len(population)-1)
      g=random.randint(0,15)
      swap1=population[i][g][0:2]
      population[i][g][0:2]=population[c][g][0:2]
      population[c][g][0:2]=swap1

      # swap2=population[i][g][1]
      # population[i][g][1]=population[c][g][1]
      # population[c][g][1]=swap2

      # swap3=population[i][g][0]
      # population[i][g][0]=population[c][g][0]
      # population[c][g][0]=swap2

  return population

def mutation(population):
  for i in range(30):
    c=random.randint(0,len(population)-1)
    g=random.randint(0,12)

    new_gates=[x for x in gates if x!= population[c][g][2]]
    population[c][g][2]=random.choice(new_gates)
  return population






final_result=[]

dict={
   'and':6
   ,'or':6
   ,'buffer':0
   ,'nor':4
   ,'nand':4
   ,'xnor':14 
   , 'xor':12
}


def find_score(crom):

    score=0
    for i in range(16):
      score=score+dict[crom[i][2]]
    return score


for epoch in range(1000):
  elitism1=elitism(population,fitness)
  population=selection(population,fitness)
  population=crossover(population)
  population=mutation(population)
  population=np.concatenate((population,elitism1))

  fitness=findfitness(population)
  print("max fitness: ",max(fitness))
  if len(answer)>=100 :
    break



for i,crom in enumerate(answer):
  score=find_score(crom)
  final_result.append([crom,score])
 


# print(in_out)
# print(answer)
print(final_result)
