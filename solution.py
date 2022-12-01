import csv

with open('log.csv', newline='\n') as csvfile:
	food_frequency = {}
	food_eaters = {}

	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		eater_id = row[0]
		foodmenu_id = row[1]

		if foodmenu_id in food_eaters:
			if eater_id in food_eaters[foodmenu_id]:
				raise Exception("eater already exists")
			food_eaters[foodmenu_id].append(eater_id)
			food_frequency[foodmenu_id] = food_frequency[foodmenu_id] + 1
		else:
			food_eaters[foodmenu_id] = [eater_id]
			food_frequency[foodmenu_id] = 1

	food_order = []
	# Sort dict values by key: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
	sorted_food_frequency = dict(sorted(food_frequency.items(), key=lambda item: item[1], reverse=True))
	first_three = list(food_frequency.keys())[0:3]
	print(f"Top 3 eaten foods: {first_three[0]} {first_three[1]} {first_three[2]}")
