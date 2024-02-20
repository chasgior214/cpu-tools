from openai import OpenAI

with open('credentials.txt') as f:
    api_key = f.readline().split('=')[1].strip()

def open_chat(askAI, model='gpt4'): # gpt-4-turbo-preview, gpt-3.5-turbo	
    client = OpenAI(
        api_key = api_key,
    )

    if model == 'gpt4':
        model = "gpt-4-turbo-preview"
    elif model == 'gpt3.5':
        model = "gpt-3.5-turbo"

    print("Begin script\n") 

    response = client.chat.completions.create(
    model = model, 
    messages = [
            {"role": "user", 
             "content": askAI}
        ])

    print(response)

    print("\nEnd script")
    return response