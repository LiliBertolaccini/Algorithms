def study_schedule(permanence_period, target_time):
#1.1 - Retorne a quantidade de estudantes presentes para uma entrada específica;
# estudante             1       2       3       4       5       6
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), 5]

    if not permanence_period or not target_time:
        return None
    
    if not all(isinstance(time, tuple) and len(time) == 2 and all(isinstance(t, int) and t > 0 for t in time) for time in permanence_period):
        return None
    
    students_present = []

    for i, (start, end) in enumerate(permanence_period):
        if start <= target_time <= end:
            students_present.append(i + 1)
    
    return students_present
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 2

print(study_schedule(permanence_period, target_time))  # Saída: [1, 2, 3]
#permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), 5]

#print(study_schedule(permanence_period, 5))  # Saída: [4, 5, 6]


#    for i, time in enumerate(permanence_period):
#        if time >= target_time:  # Verifica se o estudante estava presente no horário alvo
#                return None
        
#        students_present.append(i + 1)  # Adiciona o número do estudante à lista
#        if not permanence_period or not target_time:
#                return None  # 1.3 - Verifica se há valores vazios
            
#        students_present = []  # Lista para armazenar os estudantes presentes no horário alvo            target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
#        target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
#        target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
#        target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
#        target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.
#            # Nos arrays temos 6 estudantes
##1.2 - Retorne None se em permanence_period houver alguma entrada inválida;
#    if not all(isinstance(time, int) and time > 0 for time in permanence_period):  # 1.2 - Verifica entradas inválidas
#        return None

##Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
##O melhor horário será aquele no qual o contador retornado pela função for o maior


##1.3 - Retorne None se target_time recebe um valor vazio;
#    if permanence_period == 1:
#        return None
##1.4 - A função deverá, por meio de análise empírica, como no máximo O(n), com complexidade assintótica linear.
#permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), 5]
#print(study_schedule(permanence_period, 5))  # Saída: 3