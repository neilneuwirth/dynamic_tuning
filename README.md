# Few-Shot Prompt Augmentation (FSPA)

## Overview

Few-Shot Prompt Augmentation (FSPA) dynamically augments prompts in language models by using context derived from information retrieval systems. The primary goal of this repository is to optimize the process of generating contextually relevant outputs without the need for exhaustive fine-tuning or manual preparation of prompts.

## How It Works

1. **Dataset Curation**: Datasets are curated and processed to be upserted into a vector database.
2. **Vector Database**: Data from the curated datasets is embedded into vectors and stored in a data store (e.g. vector database).
3. **User Query Processing**: Upon receiving a user's query, an information retrieval search combined with dynamic filtering is performed across the data store (e.g. semantic search across a vector database).
4. **Context Retrieval**: The top relevant contexts are retrieved based on the user's query.
5. **Prompt Augmentation**: The retrieved context is injected into the prompt along with the initial user query and few-shot examples.
6. **Model Generation**: The augmented prompt is then fed into the large language model (LLM) to generate an appropriate output response.

## Use Cases
- **Custom Tasks**: Tailor the model's behavior for niche tasks using domain-specific examples from the database.
