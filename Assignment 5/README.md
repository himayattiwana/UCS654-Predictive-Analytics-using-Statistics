# Multi-Criteria Ranking of Conversational AI Models Using TOPSIS

## Project Context

Recent advances in Natural Language Processing have led to the rapid adoption of conversational AI systems in domains such as customer service automation, digital assistants, educational platforms, and recommendation engines. Selecting the most appropriate conversational model is not straightforward because performance depends on multiple factors, including response quality, semantic accuracy, inference efficiency, and resource consumption.

This project develops a structured evaluation framework to compare several pre-trained dialogue models using a multi-criteria decision-making technique known as TOPSIS (Technique for Order Preference by Similarity to Ideal Solution). The approach enables objective ranking by simultaneously considering quality-related and efficiency-related metrics.

---

## Aim of the Study

The work focuses on systematically assessing conversational models rather than relying on a single performance indicator.

Key goals include:

- Assess dialogue-generation capability across multiple models  
- Measure performance using both linguistic quality and computational efficiency indicators  
- Apply a structured ranking mechanism using TOPSIS  
- Determine the most suitable conversational model based on combined criteria  

---

## Conversational Models Considered

The evaluation includes a mix of generative and retrieval-based architectures to capture a wide design spectrum:

- DialoGPT  
- BlenderBot  
- FLAN-T5  
- BERT-based Retrieval Conversational System  
- LLaMA-2 Chat  

These models differ in terms of architecture, response fluency, contextual reasoning ability, and hardware requirements.

---

## Evaluation Dataset

A subset of prompts was curated from the DailyDialog corpus, which contains realistic, human-like conversational exchanges across common scenarios such as greetings, discussions, requests, and opinions.

Using a fixed set of prompts ensured that each model was evaluated under identical conditions, allowing fair comparison.

---

## Performance Indicators

To enable balanced comparison, evaluation criteria were divided into benefit and cost dimensions.

### Quality-Oriented Indicators (Higher Preferred)

- BLEU score  
- ROUGE-L score  
- BERTScore  
- Human judgement score (fluency and relevance)

### Efficiency-Oriented Indicators (Lower Preferred)

- Inference time  
- Model size  

---

## Weight Assignment Strategy

Different criteria contribute unequally to overall conversational performance. Therefore, weighted importance was assigned based on relevance to dialogue quality and deployment feasibility.

| Criterion | Weight |
|----------|--------|
| BLEU | 0.15 |
| ROUGE-L | 0.15 |
| BERTScore | 0.20 |
| Human Evaluation | 0.25 |
| Inference Time | 0.15 |
| Model Size | 0.10 |

Human evaluation and semantic similarity metrics were prioritized because they directly reflect conversational effectiveness.

---

## Ranking Framework

The ranking process was carried out using the TOPSIS method, which identifies alternatives closest to an ideal solution and farthest from the worst-case solution.

The procedure followed these stages:

1. Construct a decision matrix using evaluation metrics  
2. Normalize metric values to remove scale differences  
3. Apply criterion weights  
4. Identify ideal best and worst reference points  
5. Compute Euclidean distance from both reference points  
6. Derive TOPSIS closeness coefficient  
7. Rank models based on coefficient values  

Higher closeness scores indicate better overall suitability.

---

## Project Components

### Data Files
- `model_metrics_conversational.csv` — compiled evaluation metrics for each model  
- `topsis_conversational_results.csv` — final ranking scores after TOPSIS computation  

### Notebook
- Implementation of TOPSIS workflow and visual analysis  

### Visualization
- `topsis_graph.png` — graphical representation of TOPSIS scores  

---

## Comparative Findings

The final ranking derived from the multi-criteria evaluation is summarized below:

| Rank | Model | TOPSIS Score |
|------|------|--------------|
| 1 | LLaMA-2 Chat | 0.8125 |
| 2 | BlenderBot | 0.7452 |
| 3 | FLAN-T5 | 0.5984 |
| 4 | DialoGPT | 0.4321 |
| 5 | BERT Retrieval Model | 0.2876 |

---

## Visual Representation of Rankings

The figure below presents a comparative view of TOPSIS scores across all evaluated conversational systems.

![TOPSIS Ranking](topsis_graph.png)

---

## Interpretation of Results

The ranking indicates a clear performance gradient among the evaluated models.

- LLaMA-2 Chat demonstrates strong contextual reasoning and language generation capability, leading to superior overall performance.  
- BlenderBot shows high coherence and semantic consistency across responses.  
- FLAN-T5 maintains balanced performance across linguistic and computational metrics.  
- DialoGPT performs reasonably well but falls short in semantic similarity measures.  
- Retrieval-based BERT systems show efficiency advantages but limited generative flexibility.

The analysis suggests that modern generative architectures outperform earlier conversational systems when evaluated holistically.

---

## Key Takeaways

- Multi-metric evaluation provides more reliable insights than single-metric comparison  
- Human judgement plays a critical role in assessing conversational effectiveness  
- Efficiency factors such as inference time significantly impact deployment feasibility  
- Ensemble evaluation techniques like TOPSIS support objective decision-making  

---

## Concluding Remarks

This study highlights the importance of structured decision frameworks for selecting conversational AI models. Instead of prioritizing a single metric, the TOPSIS method enables a balanced comparison between linguistic quality and operational efficiency.

Based on the multi-criteria analysis, LLaMA-2 Chat emerges as the most suitable conversational model among the alternatives considered in this study.

---

## Potential Extensions

Future work may explore:

- Adaptive weighting strategies depending on deployment scenarios  
- Evaluation using domain-specific conversational datasets  
- Inclusion of latency stability and memory footprint as additional metrics  
- Assessment of multilingual conversational systems  
- Comparative analysis between fine-tuned and base pre-trained models  

---

## Author

**Name:** Himayat Singh Tiwana  
**Roll No:** 102313049
