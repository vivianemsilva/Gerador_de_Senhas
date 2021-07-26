import random

carac = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*#<@.>_'
compr = 8
print("gerador de senhas")
print("senhas geradas:")
for i in range (compr):
    senha = "".join(random.sample(carac, compr))
    print(senha)