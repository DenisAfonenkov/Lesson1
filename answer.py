def get_answer(question):
	answers = {"привет":"И тебе привет!","как дела": "Лучше всех", "пока": "Увидимся"}
	return answers[question.lower()]
question = input()
print(get_answer(a))

