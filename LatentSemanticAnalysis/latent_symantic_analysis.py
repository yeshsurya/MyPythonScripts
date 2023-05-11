from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, num_sentences=3):
    # Create a parser and tokenize the text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Create an LSA summarizer
    summarizer = LsaSummarizer()

    # Summarize the text
    summary = summarizer(parser.document, num_sentences)

    # Join the summarized sentences into a single string
    summarized_text = " ".join(str(sentence) for sentence in summary)

    return summarized_text

# Example usage
input_text = """
The quick brown fox jumps over the lazy dog.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed vitae metus sit amet nunc pellentesque sodales vitae ac enim.
"""

summarized_text = summarize_text(input_text, num_sentences=2)
print(summarized_text)
