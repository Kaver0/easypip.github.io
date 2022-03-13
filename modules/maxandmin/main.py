while True == True:
	try:
		print("\n")
		f = int(input("Введите способ получения макимального числа и минимального числа.\n(Через max() или min() - 1, через вложеные операторы - 2, через and - 3): "))
	except Exception as _ex:
		print("Пожалйста введите число(1, 2, 3) а не строку!")
		while True == True:
			input()

	one = int(input("Введите первое число: "))
	two = int(input("Введите второе число: "))
	three = int(input("Введите третье число: "))
	print("\n")

	if f == 1:
		print("Максимальное число: " + str(max(one, two, three)) + ".\nМинимальное число: " + str(min(one, two, three)) + ".")
	elif f == 2:
		if one > two:
			if one > three:
				print("Максимальное число: " + str(one) + ".")
				if one < two:
					if one < three:
						print("Минимальное число: " + str(one) + ".")
					elif three < one:
						print("Минимальное число: " + str(three) + ".")
				elif two < one:
					if two < three:
						print("Минимальное число: " + str(two) + ".")
					elif three < two:
						print("Минимальное число: " + str(three) + ".")
			elif three > one:
				print("Максимальное число: " + str(three) + ".")
				if one < two:
					if one < three:
						print("Минимальное число: " + str(one) + ".")
					elif three < one:
						print("Минимальное число: " + str(three) + ".")
				elif two < one:
					if two < three:
						print("Минимальное число: " + str(two) + ".")
					elif three < two:
						print("Минимальное число: " + str(three) + ".")
		elif two > one:
			if two > three:
				print("Максимальное число: " + str(two) + ".")
				if one < two:
					if one < three:
						print("Минимальное число: " + str(one) + ".")
					elif three < one:
						print("Минимальное число: " + str(three) + ".")
				elif two < one:
					if two < three:
						print("Минимальное число: " + str(two) + ".")
					elif three < two:
						print("Минимальное число: " + str(three) + ".")
			elif three > two:
				print("Максимальное число: " + str(three) + ".")
				if one < two:
					if one < three:
						print("Минимальное число: " + str(one) + ".")
					elif three < one:
						print("Минимальное число: " + str(three) + ".")
				elif two < one:
					if two < three:
						print("Минимальное число: " + str(two) + ".")
					elif three < two:
						print("Минимальное число: " + str(three) + ".")
		elif one == two:
			if one > three:
				print("Максимальные числа: " + str(one) + ", " + str(two) + ".")
				print("Минимальное число: " + str(three) + ".")
			elif one < three:
				print("Максимальное число: " + str(three) + ".")
				print("Минимальные числа: " + str(one) + ", " + str(two) + ".")
			elif three == two:
				print("Числа " + str(one) + ", " + str(two) + ", " + str(three) + " равны.")
		elif one == three:
			if one > two:
				print("Максимальные числа: " + str(one) + ", " + str(three) + ".")
				print("Минимальное число: " + str(two) + ".")
			elif one < two:
				print("Максимальное число: " + str(two) + ".")
				print("Минимальные числа: " + str(one) + ", " + str(three) + ".")
			elif three == two:
				print("Числа " + str(one) + ", " + str(two) + ", " + str(three) + " равны.")
		elif three == two:
			if three > one:
				print("Максимальные числа: " + str(two) + ", " + str(three) + ".")
				print("Минимальное число: " + str(one) + ".")
			elif three < one:
				print("Макимальное число: " + str(one) + ".")
				print("Минимальные числа: " + str(two) + ", " + str(three) + ".")
			elif three == two:
				print("Числа " + str(one) + ", " + str(two) + ", " + str(three) + " равны.")
	elif f == 3:
		if one > two and one > three and two == three:
			print("Максимальное число: " + str(one) + ".")
			print("Минимальные числа: " + str(two) + ", " + str(three) + ".")
		elif one > two and one > three and two > three:
			print("Максимальное число: " + str(one) + ".")
			print("Минимальное число: " + str(three) + ".")
		elif one > two and one > three and three > two:
			print("Максимальное число: " + str(one) + ".")
			print("Минимальное число: " + str(two) + ".")

		elif two > one and two > three and one == three:
			print("Максимальное число: " + str(two) + ".")
			print("Минимальные числа: " + str(one) + ", " + str(three) + ".")
		elif two > one and two > three and one > three:
			print("Максимальное число: " + str(two) + ".")
			print("Минимальное число: " + str(three) + ".")
		elif two > one and two > three and three > one:
			print("Максимальное число: " + str(two) + ".")
			print("Минимальное число: " + str(one) + ".")

		elif three > one and three > two and one == two:
			print("Максимальное число: " + str(three) + ".")
			print("Минимальные числа: " + str(one) + ", " + str(two) + ".")
		elif three > one and three > two and one > two:
			print("Максимальное число: " + str(three) + ".")
			print("Минимальное число: " + str(two) + ".")
		elif three > one and three > two and two > one:
			print("Максимальное число: " + str(three) + ".")
			print("Минимальное число: " + str(one) + ".")

		elif one == two and two == three:
			print("Числа " + str(one) + ", " + str(two) + ", " + str(three) + " равны.")