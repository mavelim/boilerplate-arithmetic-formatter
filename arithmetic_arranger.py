def arithmetic_arranger(problems, solver=False):
	#arranged_problems= []
	# definimos espacio entre cada problem
	between_pro = "    "
	operand1=""
	operand2=""
	solucion=""
	total=""
	#definiendo los errores

	#demasiados problemas
	if len(problems)>5:
		arranged_problems= 'Error: Too many problems.'
	else:
		for problem in problems:
			igual=""
			terms=problem.split()
			if len(terms)==3:
				if '+' not in terms and '-'not in terms:
					arranged_problems="Error: Operator must be '+' or '-'."
					break
				elif not terms[0].isdigit() or not terms[2].isdigit():
					arranged_problems="Error: Numbers must only contain digits."
					break
				elif len(terms[0])>4 or len(terms[2])>4:
					arranged_problems="Error: Numbers cannot be more than four digits."
					break
				spaces=len(terms[0]) - len(terms[2])
				if spaces >=0:
					add_spaces= 2
					same=0
				else:
					add_spaces= 0
					same=2
				#añadir espacio en blanco por delante
				terms[add_spaces]=terms[add_spaces].rjust(len(terms[add_spaces])+abs(spaces)+1)
				terms[same]=terms[same].rjust(len(terms[same])+1)
				#formamos los problemas añadiendo los respectivos signos
				#ponenmos los operandos en orden en un solo string
				operand1=operand1+" "+terms[0]+between_pro
				operand2=operand2+terms[1]+terms[2]+between_pro
				igual=igual.rjust(len(terms[0])+1,"-")
				total=total+igual+between_pro
				arranged_problems=operand1.rstrip()+"\n"+operand2.rstrip()+"\n"+total.rstrip()
				if solver==True:
					if terms[1]=='+':
						solu=int(terms[0]) + int(terms[2])
					else:
						solu=int(terms[0]) - int(terms[2])
					solucion=solucion+str(solu).rjust(len(igual))+between_pro
					arranged_problems=arranged_problems+"\n"+solucion.rstrip()

			else: print("faltan operandos")

	#arranged_problems=problems+[solver]
	return arranged_problems

