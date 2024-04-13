from openai import OpenAI


def chat_with_gpt(text):
    client = OpenAI(api_key='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')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
        ])
    return response.choices[0].message.content


if __name__ == '__main__':
    print(chat_with_gpt("Hello, how are you?"))  # Output: "I'm doing well, thank you. How can I help you today?"
