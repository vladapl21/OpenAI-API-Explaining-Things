import openai

# Set the API key
openai.api_key = "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"

x = input("explanation or general?:  ")

if x == "explanation":
    a, b, c = [input('Explanation Level: '), input('Subject: '), input('What do you need explained?: ')]

    # Define the prompt
    prompt = (f"Explain {c}, at a {a} level in the context of the subject: {b}")

    # Generate text
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)

    # Print the generated text
    print(completions.choices[0].text)

elif x == "general":
    # Define the prompt
    prompt = input("Enter question: ")

    # Generate text
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)

    # Print the generated text
    print(completions.choices[0].text)
