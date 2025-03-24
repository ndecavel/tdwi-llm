# LLM Hands-On Labs: LLM, RAG, and Agent Systems Resources

![Last Updated](https://img.shields.io/github/last-commit/ndecavel/tdwi-llm?label=Last%20Updated)

This repository contains materials and resources from the TDWI workshop on using LLMs with your company data. It includes the data and the hands-on labs to help you implement these technologies in your own projects. This is a living repository and the code will occasionally update and improve as the common tooling used in production starts to standardize.

## Table of Contents

- [Repository Structure](#repository-structure)
- [Lab Overview](#lab-overview)
  - [Lab 1: The Art of Prompting LLMs](#lab-1-the-art-of-prompting-llms)
  - [Lab 2: Naive RAG Pipeline](#lab-2-naive-rag-pipeline)
  - [Lab 3: Improving RAG Systems](#lab-3-improving-rag-systems)
  - [Lab 4: Giskard Evaluation](#lab-4-giskard-evaluation)
- [Getting Started](#getting-started)
- [Resources & Further Learning](#resources--further-learning)
  - [Practical Applications of LLMs](#practical-applications-of-llms)
  - [Educational Materials](#educational-materials)
    - [Courses & Podcasts](#courses--podcasts)
    - [Reading I Go Back To](#reading-i-go-back-to)
    - [GitHub Resources](#github-resources)
- [Contact](#contact)

## Repository Structure

```
├── Labs
│   ├── Lab_1_LLM_Prompting.ipynb
│   ├── Lab_2_Naive_RAG.ipynb
│   ├── Lab_3_Improving_RAG.ipynb
│   ├── Lab_4_Giskard.ipynb
│   └── Text_Splitting_App.py
├── data
│   ├── Behr_all_products.xlsx
│   ├── Data_Resources_TDS.zip
│   └── Golden_Test_Data_DeepEval.csv
└── requirements.txt
```

## Lab Overview

### Lab 1: The Art of Prompting LLMs
An introduction to working with Large Language Models, covering:
- Basic and chat-based prompting techniques
- Creating prompt templates
- Understanding token mechanics
- Comparing different LLM models (OpenAI vs. Gemini)

### Lab 2: Naive RAG Pipeline
A basic implementation of Retrieval Augmented Generation using BEHR paint product data:
- Data visualization and understanding
- Document chunking and embedding strategies
- Building a vector database with Milvus
- Creating a query engine for information retrieval
- Generating answers with LLMs
- Basic evaluation using ragas metrics

### Lab 3: Improving RAG Systems
Advanced techniques to enhance RAG performance:
- Implementation of LlamaParse for better document processing
- Hybrid search using RFRanker for faster retrieval
- Input prompt optimization
- Metric-driven experimentation and evaluation

### Lab 4: Giskard Evaluation
Building and validating a robust question-answering system:
- Vulnerability scanning for hallucinations and other issues
- Test suite (and guardrail) generation and execution

## Getting Started
1. Clone this repository
```bash
git clone https://github.com/ndecavel/tdwi-llm.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Explore the labs in order for a progressive learning experience
4. Use the provided data files, but make sure to update any API keys referenced in the labs.


## Resources & Further Learning

### Practical Applications of LLMs
When considering practical applications for LLMs within your organization, I usually recommend exploring these options beyond the "Talk with your data" use case we discussed during the lab. The right application for you will depend on the data you have access to, the resources available, and your tolerance for errors in the final output.

- **Extracting Structured Information**: If your goal is to extract structured data from unstructured text, LLMs can help achieve a stable end-user experience. For instance, LLMs can extract key details from long documents or categorize large sets of text into predefined categories, which can streamline various workflows.
- **Document Drafting**: LLMs can assist in generating a first draft of a document or report, ensuring that you have well-referenced examples and accurate information. When integrated with RAG, this can significantly reduce the time spent on manual research and drafting.

Note: Prompt engineering combined with LLMs isn't always the best solution. Depending on your specific use case, you might benefit more from a specialized tool. For instance, when dealing with a review that expresses mixed sentiments, such as “I loved the service, but didn’t really like the food,” simple sentiment analysis models might struggle to provide accurate results. Instead of immediately turning to something like ChatGPT, you might find "Aspect-Based Sentiment Analysis" (ABSA) more effective for extracting sentiments on specific aspects within reviews. 

**Here is a useful resource I recommend for identifying state-of-the-art AI modeling techniques tailored to your use case: https://paperswithcode.com/methods**

### Educational Materials

#### Podcasts
- [SuperDataScience Podcast](https://www.superdatascience.com/podcast)
    - Technical intro to Transformers/LLMs:
        - https://www.superdatascience.com/podcast/technical-intro-to-transformers-and-llms-with-kirill-eremenko
        - https://www.superdatascience.com/podcast/full-encoder-decoder-transformers-fully-explained-with-kirill-eremenko

#### Reading I Go Back To
- [Critical Questions for RAG/LLM Implementation](https://learn.microsoft.com/en-us/azure/databricks/ai-cookbook/implementation/prerequisites)
- [Practical Insights from a Year of Building with LLMs](https://applied-llms.org/)
- [Hamal Husain's Blog](https://hamel.dev/)
- [Jason Liu's RAG Insights](https://jxnl.co/writing/#personal-stories)

#### GitHub Resources
- [Awesome LLMs](https://github.com/Hannibal046/Awesome-LLM)
- [Awesome Gen AI](https://github.com/aishwaryanr/awesome-generative-ai-guide)
- [Langfuse](https://github.com/langfuse/langfuse)

> **Note**: This repository will be periodically updated with new resources every 3 months to reflect the updates in the field as well as updates to what I am using in building systems to production.

## Contact
<div align="center">
  <img src="https://github.com/ndecavel.png" width="100px" style="border-radius:50%"><br>
  <strong>Nicolas Decavel-Bueff</strong><br>
  <a href="https://github.com/ndecavel"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
  <a href="https://linkedin.com/in/nicolas-decavel-bueff/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
</div>
