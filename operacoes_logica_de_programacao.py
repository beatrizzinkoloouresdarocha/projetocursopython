primeiro_numero = 5
segundo_numero = 1
terceiro_numero = 3

condicao_verdadeira_simples = primeiro_numero > segundo_numero

condicao_falsa_simples = primeiro_numero < segundo_numero 

condicao_negacao_falsa_simples = not primeiro_numero > segundo_numero

condicao_negacao_verdadeira_simples = not primeiro_numero < segundo_numero 

# que o not(não) inverte o resultado da expressao 

condicao_verdadeira_composta = primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero 

condicao_falsa_composta = primeiro_numero > segundo_numero and primeiro_numero < terceiro_numero

#quando pelo menos uma das expressoes é falsa o resultado é falso

condicao_ou_verdadeira = primeiro_numero > segundo_numero or primeiro_numero < terceiro_numero
condicao_ou_falsa = primeiro_numero < segundo_numero or primeiro_numero < terceiro_numero

#and (e) :
#verdadeiro e verdadeiro = verdadeiro
#verdadeiro e falso = falso 
#falso e verdadeiro = falso 
#falso e falso = falso 

#or (ou) : 
#verdadeiro ou verdadeiro =verdadeiro
#verdadeiro ou falso = verdadeiro
#falso ou verdadeiro =verdadeiro
#falso ou falso = falso 

#>  maior 
#<  menor 