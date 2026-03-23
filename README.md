# Offline Customer Support Chatbot using Ollama

##  Project Overview
This project implements an offline customer support chatbot using Ollama and the Llama 3.2 (3B) model. The chatbot is designed to handle e-commerce queries locally without relying on external APIs, ensuring data privacy and zero API costs.

---

##  Objective
- Build a chatbot that runs locally using Ollama
- Compare Zero-shot and One-shot prompting techniques
- Evaluate responses based on Relevance, Coherence, and Helpfulness

---

##  Tools & Technologies
- Python
- Ollama
- Llama 3.2 (3B)
- Requests Library

---

##  Project Structure
```
offline-chatbot/
│
├── chatbot.py
├── setup.md
├── report.md
├── README.md
│
├── prompts/
│ ├── zero_shot_template.txt
│ └── one_shot_template.txt
│
├── eval/
│ └── results.md
```

---

## ⚙️ How It Works
1. The chatbot reads customer queries
2. Applies Zero-shot and One-shot prompt templates
3. Sends requests to Ollama (local server)
4. Llama 3.2 model generates responses
5. Responses are saved in `eval/results.md`
6. Manual evaluation is done based on quality

---

## 📊 Evaluation Criteria
Each response is evaluated on:
- Relevance (1–5)
- Coherence (1–5)
- Helpfulness (1–5)

---

## 📈 Key Findings
- One-shot prompting produces more accurate and structured responses
- Zero-shot responses are sometimes less precise
- Local models ensure privacy but may be slower

---

## 🚀 How to Run
1. Install Ollama from https://ollama.com  
2. Pull the model:
```
ollama pull llama3.2:3b
```
3. Start Ollama:
```
ollama serve
```
4. Install Python dependencies:
```
pip install requests datasets
```
5. Run the chatbot:
```
python chatbot.py
```

---

##  Conclusion
This project demonstrates how local LLMs can be used for customer support while maintaining data privacy. One-shot prompting was found to be more effective than zero-shot prompting.

---

##  Limitations
- Smaller model (3B) has limited understanding
- No real-time data integration
- Slower performance on CPU

---

##  Future Improvements
- Use larger models
- Integrate with real customer databases
- Improve prompt engineering techniques