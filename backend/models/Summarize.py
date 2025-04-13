
import nltk
import torch
from transformers import MarianMTModel, MarianTokenizer
from transformers import BartTokenizer, BartForConditionalGeneration
from nltk.tokenize import sent_tokenize
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


nltk.download('punkt')


LLM_SAFE_CONTEXT_LENGTH = 8192


def summarize_transcript(transcript_path, model_name="facebook/bart-large-cnn", max_chunk_length=1024, min_length=30, max_length=150, use_path=False):
    """
    Summarize a podcast transcript using a Hugging Face model.
    
    Args:
        transcript_path: Path to the transcript text file
        model_name: Name of the Hugging Face model to use
        max_chunk_length: Maximum token length for each chunk
        min_length: Minimum length of the summary
        max_length: Maximum length of the summary
        
    Returns:
        A summary of the transcript
    """
    # device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Load model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.to(device)
    
    # Create summarization pipeline
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    
    # Read transcript
    if use_path:
        with open(transcript_path, 'r', encoding='utf-8') as file:
            transcript = file.read()
    else:
        transcript = transcript_path
        
    # For very long transcripts, we need to chunk the text
    if len(tokenizer.encode(transcript)) > max_chunk_length:
        # Split into chunks and summarize each
        chunks = split_into_chunks(transcript, tokenizer, max_chunk_length)
        safe_max_length = LLM_SAFE_CONTEXT_LENGTH // len(chunks)
        chunk_summaries = []
        print(f"generating with max_length: {safe_max_length}")
        
        
        for i, chunk in enumerate(chunks):
            print(f"Summarizing chunk {i+1}/{len(chunks)}...")
            summary = summarizer(chunk, max_length=safe_max_length , min_length=min_length, do_sample=False)[0]['summary_text']
            chunk_summaries.append(f"{summary}")
            print(i+1, summary)
        
        return "\n".join(chunk_summaries)
    else:
        return summarizer(transcript, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']

def split_into_chunks(text, tokenizer, max_length):
    """Split text into chunks of max_length tokens."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        word_tokens = len(tokenizer.encode(word))
        if current_length + word_tokens > max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = word_tokens
        else:
            current_chunk.append(word)
            current_length += word_tokens
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

