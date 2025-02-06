from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Hello, how are you doing today?"

tokens = tokenizer.tokenize(text)

print(tokens)
