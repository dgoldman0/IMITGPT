# IMITGPT - Iterative Multiphasic Ideation Through GPT

IMIT is a content creation system which utilizes repeated revisal of content generation based on a set of criteria. The idea behind the system is that content generation created through multiple rounds of ideation will be superior to a single run of an LLM prompt-completion.

## Thought Process

The current system uses OpenAI's recent gpt-3.5-turbo model, which is much less expensive and much faster than previous models. The system maintains an internal conscious dialogue and multiple subconscious dialogues, all of which work towards creating a single finalized piece.

## Settings

You can set the desired various parameters by editing the variables in [parameters.py](/parameters.py). The most utilized setting should be the plot variable. The plot can be fairly vague and the system will still generate decent content. Other parameters should be changed with more care. Not much testing has been done with changing these parameters. The content limits should be adjusted carefully, as alterations can easily lead to going over the token limit for a completion, causing the system to hang.

## Limitations

While gpt-3.5-turbo is much faster, it is still limited. The token capacity is 4,096 tokens, the same as the davinci models. This limitation makes the persistent memory limited in what it can store.

This system is designed specifically to generate fictional stories and may not work as well with non-fiction content. LLMs are known to "hallucinate" by generating fake content that only seems reasonable, and none of the features present in IMIT  
