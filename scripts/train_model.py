from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import Dataset

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    return [{"text": data}]

def train_model(data_path, output_dir):
    # Load the tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Prepare the data for fine-tuning
    data = load_data(data_path)
    dataset = Dataset.from_dict(data).map(
        lambda e: tokenizer(e["text"], truncation=True, padding="max_length"),
        batched=True
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=10,
        save_total_limit=1,
    )

    # Fine-tuning the model
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )
    trainer.train()
    trainer.save_model(output_dir)

if __name__ == "__main__":
    data_path = "../data/preprocessed_data.txt"
    output_dir = "../model/fine_tuned"
    train_model(data_path, output_dir)
