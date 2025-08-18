from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

model_name = "meta-llama/Meta-Llama-3-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.From_pretrained(model_name)

training_args = TrainingArguments(
    output_dir=".result",
    evaluation_strategy="steps",
    eval_steps=500,
    save_steps=500,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=3,
    learning_rate=5e-5,
    logging_dir="./logs",
    fp16=True
)

# 현재 데이터셋이 없어서 동작못함.
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

trainer.train()