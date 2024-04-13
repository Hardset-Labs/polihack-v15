from datetime import timedelta

import chatgpt_comunication
import json
import pdf_parser
from datetime import timedelta
import json


def generate_flashcards_and_chapters(subject_name, learning_minutes_per_day, materials_text, start_date, end_date):

    # Prompt the chat to generate flashcards and chapters based on the PDF text and learning minutes per day
    prompt = (f"Generate a lot of flashcards and each flashcards should be in chapters for the following subject '{subject_name}' from {start_date} to {end_date}. "
              f"\n\nStudy Material Content to use in making the questions: \n{materials_text}\n\n")
    prompt += "Learning minutes per day:\n"
    for date, minutes in learning_minutes_per_day.items():
        prompt += f"- {date}: {minutes}\n"

    prompt += "\nFormat for chapters, questions, and answers: DO NOT WRITE ANYTHING ELSE BESIDES THIS. YOU SHOULD GENERATE DUMMY WRONG ANSWERS. YOU SHOULD COVER THE ENTIRE STUDY MATERIAL WITH YOUR QUESTIONS\n"
    for i in range(1, 6):
        prompt += f"chapter{i}: \"Chapter {i} name\"\n"
        for j in range(1, 6):
            prompt += (f"question{j}: \"Question {j}\", answer{j}: \"Answer {j}\", dummy_answer1_{j}: \"Dummy Answer 1\", "
                       f"dummy_answer2_{j}: \"Dummy Answer 2\", dummy_answer3_{j}: \"Dummy Answer 3\", explanation{j}: \"Explanation {j}\"\n")

    # Add more examples as needed

    # Chat with GPT to generate flashcards and chapters
    chat_response = chatgpt_comunication.chat_with_gpt(prompt)

    return chat_response.replace("```\n\n```yaml", "").replace("```yaml\n", "").replace("```", "")


if __name__ == '__main__':
    # Example usage
    learning_minutes_per_day = {
        '2022-11-01': 30,
        '2022-11-02': 30,
        '2022-11-03': 30,
        '2022-11-04': 30,
        '2022-11-05': 30,
    }
    print(generate_flashcards_and_chapters('Math', learning_minutes_per_day,
                                           pdf_parser.extract_text_from_pdf('C6_slides_rom.pdf'), '2022-11-01', '2022-11-05'))
