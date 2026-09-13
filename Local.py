from langchain_ollama import OllamaLLM
import ollama
import subprocess
result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
output = result.stdout
print("Here are your ollama models:")
files_list = output.split('\n')
y = len(files_list)
models = [line.split()[0] for line in result.stdout.strip().split('\n')[1:] if line.strip()]
for index, model in enumerate(models, start=1):
    print(index, model)
print(f"Which model would you like to talk to? (1-{len(models)-1})")
answer = (input(""))
if answer == "/bye":
    quit()
else:
    answer = int(answer)
    answer2 = models[answer-1]
    model = OllamaLLM(model=answer2)
    print(f"Chatting with {answer2}. write '/bye' to exit.")
    while True:
        prompt = input("")
        if prompt == "/bye":
            quit()
        else:
            result = model.invoke(prompt)
            print(f"{answer2}:{result}")
            