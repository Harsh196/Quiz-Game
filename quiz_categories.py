import data


class QuizCategories:
    def get_quiz_categories(self):
        categories = ""
        for i in data.question_data:
            categories += f"{i}/"
        return categories

    def get_questions(self, category):
        for i in data.question_data:
            if category in i:
                return data.question_data[i]["Questions"]
        print("Sorry the category does not exists.")
        return False
