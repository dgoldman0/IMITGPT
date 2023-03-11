# IMITGPT - Iterative Multiphasic Ideation Through GPT

IMIT is a content creation system which utilizes repeated revisal of content generation based on a set of criteria. The idea behind the system is that content generation created through multiple rounds of ideation will be superior to a single run of an LLM prompt-completion.

## Thought Process

The current system uses OpenAI's recent gpt-3.5-turbo model, which is much less expensive and much faster than previous models. The system maintains an internal conscious dialogue and multiple subconscious dialogues, all of which work towards creating a single finalized piece.

## Editing Files

The [membootstrap.txt](prompts/membootstrap.txt) and the [integrate.txt](prompts/internal/integrate.txt) files can be edited to alter the desired plot of the story to generate different content.

## Limitations

While gpt-3.5-turbo is much faster, it is still limited. The token capacity is 4,096 tokens, the same as the davinci models. This limitation makes the persistent memory limited in what it can store.

This system is desigend specifically to generate fictional stories and may not work as well with non-fiction content. LLMs are known to "hallucinate" by generating fake content that only seems reasonable, and none of the features present in IMIT  
