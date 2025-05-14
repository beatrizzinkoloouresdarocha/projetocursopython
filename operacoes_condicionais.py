import random

aluno_1_media_primeiro_trimestre = 7.2
aluno_1_media_segundo_trimestre = 8.0
aluno_1_media_terceiro_trimestre = 6.0

aluno_2_media_primeiro_trimestre =2.5
aluno_2_media_segundo_trimestre =3.5
aluno_2_media_terceiro_trimestre =4.5

aluno_3_media_primeiro_trimestre =1.5
aluno_3_media_segundo_trimestre =8.5
aluno_3_media_terceiro_trimestre =9.5

aluno_4_media_primeiro_trimestre = round(random.uniform(0.0,10.0),2)
aluno_4_media_segundo_trimestre = round(random.uniform(0.0,10.0),2)
aluno_4_media_terceiro_trimestre = round(random.uniform(0.0,10.0),2)
 
total_media_aluno__1=( aluno_1_media_primeiro_trimestre + aluno_1_media_segundo_trimestre + aluno_1_media_terceiro_trimestre)/3

total_media_aluno2_= (aluno_2_media_primeiro_trimestre + aluno_2_media_segundo_trimestre + aluno_2_media_terceiro_trimestre)/4

total_media_aluno_3= (aluno_3_media_primeiro_trimestre + aluno_3_media_segundo_trimestre + aluno_3_media_terceiro_trimestre)/5

total_media_aluno_4= (aluno_4_media_primeiro_trimestre + aluno_4_media_segundo_trimestre + aluno_4_media_terceiro_trimestre)/7

if total_media_aluno__1>= 6:
    print(f"aluno1 aprovado. media: {total_media_aluno__1}")
elif total_media_aluno__1 >=4:
    print(f"aluno1 em recuperação.media:{total_media_aluno__1}")  
else: 
    print(f"aluno1 reprovado.media:{total_media_aluno__1}")  

if total_media_aluno2_>=6:    
    print(f"aluno2 aprovado.media: {total_media_aluno2_}")
elif total_media_aluno2_>=4:
    print(f"aluno2 em recuperação.media {total_media_aluno2_}")
else:
    print(f"aluno2 reprovado.media:{total_media_aluno2_}")

if total_media_aluno_3>= 6:
    print(f"aluno3 aprovado. media: {total_media_aluno_3}")
elif total_media_aluno_3 >=4:
    print(f"aluno3 aprovado.media:{total_media_aluno_3}")
else:
    print(f"aluno3 reprovado.media: {total_media_aluno_3}")

if total_media_aluno_4>=6:
    print(f"aluno4 aprovado.media: {total_media_aluno_4}")
elif total_media_aluno_3 >=4:
    print(f"aluno4 aprovado.media: {total_media_aluno_4}")
else:
    print(f"aluno4  reprovado.media: {total_media_aluno_4}")