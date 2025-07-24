from langchain.prompts import SystemMessagePromptTemplate

TEMPLATE = """Make the following text more concise, ensuring the final output is no more than {filter_threshold} characters long.

Simplify the language used. Replace long phrases with shorter synonyms, remove unnecessary adverbs and adjectives, or rephrase sentences to make them more concise.
 
Remove redundancies, especially those written informally or conversationally, using repetitive information or phrases.

Flatten text that includes nested hierarchical information that isn't crucial for understanding.

Extract text content out of HTML tags.

Retain key details such as file names, IDs, people, places, and important events:

{long_text}"""


def summarization_prompt_template(
    filter_threshold: int = 2000,
) -> SystemMessagePromptTemplate:
    template = TEMPLATE.format(filter_threshold=filter_threshold)
    return SystemMessagePromptTemplate.from_template(template)
