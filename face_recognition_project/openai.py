import openai
openai.api_key = "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"

def generate_message(emotion):
    prompt = f"I'm feeling {emotion}. Can you give me some words of encouragement?"
    model = "text-davinci-002"
    response = openai.Completion.create(
      engine=model,
      prompt=prompt,
      max_tokens=60,
      n=1,
      stop=None,
      temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Example usage:
message = generate_message("sad")
print(message)