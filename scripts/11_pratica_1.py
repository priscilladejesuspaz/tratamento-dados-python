#salarios = [2500, 4800, 7200, 3100, 9500, 1800, 6300]

#for salario in salarios:
 #   if salario <= 3000:
  #      print(f"R$ {salario} — baixo")
   # elif salario <= 7000:
    #    print(f"R$ {salario} — médio")
    #else:
     #   print(f"R$ {salario} — alto")
     
# Cria uma função chamada analisar_transacao que recebe um valor e retorna:

#"bloqueada" se o valor for acima de 50000
#"suspeita" se estiver entre 10001 e 50000
#"normal" se for até 10000

#Depois testa com os valores: 500, 12000, 75000. 🚀

def analisar_transacao(transacao):
    if transacao < 10000:
        return "normal"
    elif transacao < 50000:
        return "suspeita"
    else:
        return "bloqueada"
    
print(analisar_transacao(500))    # normal
print(analisar_transacao(12000))  # suspeita
print(analisar_transacao(75000))  # bloqueada