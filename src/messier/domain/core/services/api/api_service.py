class ApiService:

    def generate_test(self, text: str):
        print(text)

        # request to api
        return list("question1", "question2", "question3")


api_service = ApiService()
