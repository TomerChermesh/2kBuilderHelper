import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def chat_with_gpt():
    print('Insert 2k player name.\n')
    while True:
        prompt = input('Player: ')
        if prompt.lower() in ['exit']:
            break

        response = client.chat.completions.create(
            model='gpt-4.1-mini',
            messages=[
                {'role': 'system', 'content': 'You are a 2k players stats helper.'
                                              'use https://www.2kratings.com/ as your source for attributes, stats,'
                                              'hot zones, and badges. Badges must be mentioned with their color.'
                                              'For the General Info and Vitals - use wikipedia if needed.'},
                {'role': 'user', 'content': prompt}
            ]
        )

        answer = response.choices[0].message.content.strip()
        print(f'GPT: {answer}\n')


if __name__ == '__main__':
    print('///// Start /////')
    chat_with_gpt()
    print('///// End /////')
