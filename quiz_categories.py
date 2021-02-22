import data


class QuizCategories:
    def get_quiz_categories(self):
        categories = ""
        for i in data.question_data:
            categories += f"{i}/"
        return categories

    def get_questions(self, selected_category):
        for category in data.question_data:
            if selected_category.lower() in category.lower():
                return data.question_data[category]["Questions"]
        print("Sorry the category does not exists.")
        return False
