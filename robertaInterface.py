from transformers import AutoTokenizer, AutoModel
import torch
def get_roberta_embeddings(text):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    # Load pre-trained RoBERTa model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("roberta-base")
    model = AutoModel.from_pretrained("roberta-base")

    # Move the model to the selected device
    model = model.to(device)

    # Tokenize the input text
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Move the tokens to the selected device
    tokens = {key: value.to(device) for key, value in tokens.items()}

    # Pass the tokens through the model
    output = model(**tokens)

    # Extract embeddings using the mean pooling approach
    embeddings = output.last_hidden_state.mean(dim=1).detach().cpu().numpy()

    return embeddings

print(get_roberta_embeddings("Yovel is a great guy!"))