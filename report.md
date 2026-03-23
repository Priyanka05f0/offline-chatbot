# Offline Customer Support Chatbot using Ollama

## Introduction
This project focuses on building an offline customer support chatbot using Ollama and the Llama 3.2 (3B) model. The chatbot is designed to handle e-commerce queries locally without sending any data to external servers, ensuring privacy.

## Objective
The objective of this project is to compare the performance of Zero-shot and One-shot prompting techniques in generating customer support responses.

## Methodology
- A set of 20 e-commerce-related customer queries was used.
- Two prompt templates were created:
  - Zero-shot prompt (no example)
  - One-shot prompt (with one example)
- Each query was sent to the Llama 3.2 model using Ollama.
- Responses were collected and stored in a results file.
- Each response was evaluated manually using three criteria: Relevance, Coherence, and Helpfulness (scored from 1 to 5).

## Results and Analysis

### Quantitative Results (Average Scores)

Zero-Shot:
- Relevance: 4.5
- Coherence: 4.6
- Helpfulness: 4.4

One-Shot:
- Relevance: 4.8
- Coherence: 4.8
- Helpfulness: 4.7

### Qualitative Analysis
- One-shot responses were more structured and consistent.
- Zero-shot responses were sometimes too long or asked unnecessary follow-up questions.
- One-shot prompting helped the model understand the expected format better.
- In cases like "cancel order" and "discount code issues", one-shot responses were more accurate and direct.

## Conclusion
The results show that One-shot prompting performs better than Zero-shot prompting in terms of relevance, coherence, and helpfulness. Providing an example helps the model generate more accurate and user-friendly responses.

## Limitations
- The Llama 3.2 (3B) model has limited understanding compared to larger models.
- Responses may not always be accurate due to lack of real-time data.
- The system runs on CPU, which makes it slower.

## Future Improvements
- Use larger and more powerful models
- Integrate with real-time databases for order tracking
- Improve prompt design for better responses