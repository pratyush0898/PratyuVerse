from transformers import GPT2LMHeadModel, GPT2Tokenizer

def chat():
    tokenizer = GPT2Tokenizer.from_pretrained("../model/fine_tuned")
    model = GPT2LMHeadModel.from_pretrained("../model/fine_tuned")

    print("Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        input_ids = tokenizer.encode(user_input, return_tensors="pt")
        outputs = model.generate(input_ids, max_length=50, num_return_sequences=1)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
