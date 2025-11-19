# Modern AI Fine-Tuning with Unsloth.ai

Practical implementations of fine-tuning and reinforcement learning techniques using Unsloth.ai - the fastest library for training LLMs with 2x speed and 70% less VRAM.

## What You'll Learn

Master full fine-tuning vs LoRA, reinforcement learning (DPO/GRPO), reasoning models, continued pre-training, and model deployment to GGUF/Ollama/vLLM formats.

Video Walkthrough: [Watch on YouTube](https://youtu.be/AKRfA0vQpwc)

---

## A. Full Fine-Tuning with SmolLM2-135M

Full parameter fine-tuning on SmolLM2-135M (135M params, trained on 2T tokens). Demonstrates complete model updates with chat templates on coding/chat datasets.

Colab Notebook: [Open in Colab](https://colab.research.google.com/github/pruthvik-sheth/CMPE-297/blob/main/Assignments/5_Modern_AI_Unsloth/Notebooks/Colab1.ipynb)

---

## B. LoRA Fine-Tuning with SmolLM2-135M

Parameter-efficient fine-tuning using LoRA on SmolLM2-135M. QLoRA 4-bit quantization for minimal memory usage with same dataset as Task A for comparison.

Colab Notebook: [Open in Colab](https://colab.research.google.com/github/pruthvik-sheth/CMPE-297/blob/main/Assignments/5_Modern_AI_Unsloth/Notebooks/Colab2.ipynb)

---

## C. Reinforcement Learning with DPO/ORPO/KTO

Preference-based RL using datasets with preferred/rejected outputs. Implements DPO, ORPO, and KTO for model alignment with human preferences.

Colab Notebook: [Open in Colab](https://colab.research.google.com/github/pruthvik-sheth/CMPE-297/blob/main/Assignments/5_Modern_AI_Unsloth/Notebooks/Colab3.ipynb)

---

## D. Reasoning Model Training with GRPO

Train reasoning models using GRPO (Group Relative Policy Optimization) - the algorithm behind DeepSeek-R1. Develops chain-of-thought reasoning with custom reward functions.

**Note:** Use 1.5B+ parameter models, train for 300+ steps to see improvements, 12+ hours for production quality.

Colab Notebook: [Open in Colab](https://colab.research.google.com/github/pruthvik-sheth/CMPE-297/blob/main/Assignments/5_Modern_AI_Unsloth/Notebooks/Colab4.ipynb)

---

## E. Continued Pre-Training

Teach LLMs new languages or expand knowledge domains using raw text data. Demonstrates knowledge injection and vocabulary expansion.

Colab Notebook: [Open in Colab](https://colab.research.google.com/github/pruthvik-sheth/CMPE-297/blob/main/Assignments/5_Modern_AI_Unsloth/Notebooks/Colab5.ipynb)

---

## Resources

- [Unsloth GitHub](https://github.com/unslothai/unsloth)
- [Documentation](https://docs.unsloth.ai)
- [GRPO Tutorial](https://docs.unsloth.ai/get-started/reinforcement-learning-rl-guide/tutorial-train-your-own-reasoning-model-with-grpo)
- [Export to Ollama](https://docs.unsloth.ai/tutorials/how-to-finetune-llama-3-and-export-to-ollama)

---