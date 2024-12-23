#Declaration of variables
a = input('Type an input to test: ')
defaultOutput1 = "Your input: '{}'".format(a) 
defaultOutput2 = "Info about your input: '{}'".format(a)

print("The type of input '{}' is {}".format(a, type(a)))
#If we have no input print that it's empty
if a == '':
    print(' {} is empty!'.format(defaultOutput1))

#If we have only spaces
elif a.isspace():
    print(' {} has only spaces!'.format(defaultOutput1))

#Output of input test
else:
    print('{}, is a text? > {}'.format(defaultOutput2, a.isalpha()))
    print('{}, is numeric? > {}'.format(defaultOutput2, a.isnumeric()))
    print('{}, is alphanumeric? > {}'.format(defaultOutput2, a.isalnum()))
    print('{}, is uppercase? > {}'.format(defaultOutput2, a.isupper()))
    print('{}, is lowercase? > {}'.format(defaultOutput2, a.islower()))

#Using variables to configure outputs makes your code dinamic and easy to update. '.format() is sending a information, in this case a variable to '{}'.

#Declaração de variáveis 
# a = input('Digite uma entrada para testar: ') 
# defaultOutput1 = "Sua entrada: '{}'".format(a) 
# defaultOutput2 = "Informações sobre a sua entrada: '{}'".format(a) 

# print("O tipo de entrada '{}' é {}".formato(a, tipo(a))) 

##Se não temos input que é vazio 

# if a == '': 
    # print(' {} is empity!'.format(defaultOutput1 )) 

##Se tivermos apenas espaços 
# elif a.isspace() 
    # print(' {} tem apenas espaços!'.format(defaultOutput1)) 
##Output do teste de input: 
# print('{}, é um texto? > {}'.format(defaultOutput2, a.isalpha())) 
# print('{}, é numérico? > {}'.format(defaultOutput2, a.isnumeric())) 
# print('{}, é alfanumérico? > {}'.format(defaultOutput2, a.isalnum())) 
# print('{}, está em maiúsculas? > {}'.format(defaultOutput2, a.isupper())) 
# print('{}, é minúsculo? > {}'.format(defaultOutput2, a.islower())) 

##Usar variáveis para configurar saídas torna seu código dinâmico e fácil de atualizar. '.format() está a enviar uma informação, neste caso uma variável para '{}'.