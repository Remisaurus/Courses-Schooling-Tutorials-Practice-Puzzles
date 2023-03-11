import openai

openai.api_key_path = 'C:\Temp\OpenAI_API_KEY_.txt'

def ask_computer(prompt):
    # prompt = "What is your favorite color?"
    res = openai.Completion.create(
        engine="text-ada-001",
        prompt=prompt,
        max_tokens= 30
    )
    # print(res)
    return res["choices"][0]["text"]

print(ask_computer('write an essay on temperature'))
print(' ')