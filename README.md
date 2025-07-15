# ToolReflection

This repository contains supplementary materials for the paper:

### **[ToolReflection: Improving Large Language Models for Real-World API Calls with Self-Generated Data](https://aclanthology.org/2025.realm-1.14/)**
Gregory Polyakov, Ilseyar Alimova, Dmitry Abulkhanov, Ivan Sedykh, Andrey Bout, Sergey Nikolenko, Irina Piontkovskaya
<br>_To appear at the REALM Workshop @ ACL 2025_

---

We are currently preparing the public release. The repository will be updated soon with more specific instructions on how to reproduce the experiments.

---

In this paper, we conduct experiments using the following frameworks: `GPT4Tools`, `ToolAlpaca`, and `ToolBench`.

The repository provides our code, including generation prompts, error generation scripts, and augmented datasets for each framework. These materials are organized into separate folders, each containing:
- The original code for fine-tuning and evaluating the models.
- Our modifications and enhancements.x
- Code for generating tool invocation chains with errors and their corrections (the **ToolReflection** approach).

Additionally, we introduce specific improvements for each framework. For example:
- In the `GPT4Tools` folder, we include:
  - Code for augmenting the dataset with additional data, such as `GPT4FakeTools`.
  - Additional benchmarks for more realistic evaluations, specifically `GPT4Tools-OOD` and `GPT4Tools-OOD-Hard`.