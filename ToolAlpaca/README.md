Here, we present the code for obtaining the results of ToolAlpaca. This repository includes the original code from [ToolAlpaca](https://github.com/tangqiaoyu/ToolAlpaca), along with our enhancements. The most notable additions are:

- **Hyperparameter Checker**: Tracks and identifies parameter errors when interacting with tools simulated by the external LLM.  
- **ToolReflection Pipeline**: Enhances the model’s robustness by improving its ability to handle and correct errors in tool usage.

### Added and Updated Components

- **`notebooks/`**:  
  Contains Jupyter notebooks that demonstrate the generation of tool invocation paths, showcasing errors and their subsequent corrections.  

- **`ToolAlpaca/agent/convert_request.py`**:  
  Includes a custom parameter checker that identifies and reports issues related to tool parameter usage.  

- **`scripts/`**:  
  Provides custom scripts for:  
  - Training both versions of the ToolAlpaca model (with and without the ToolReflection pipeline).  
  - Evaluating the performance of both model variants.