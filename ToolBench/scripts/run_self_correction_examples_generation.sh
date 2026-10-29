export CUDA_VISIBLE_DEVICES="6,7"
export TOOLBENCH_KEY="2TLxGfLkzebcy7trDP4RzqcbnuAFypTHbKlRNvYCGuVsn5Svv3"
export OUTPUT_DIR="data/answer/toolllama_dfs"
export TOOL_ROOT_DIR="data/toolenv/tools"
export PYTHONPATH=./

python toolbench/inference/generate_self_correction_examples.py \
    --model_path data/model/ToolLLaMA-2-7b \
    --ground_truth_examples_path data/self_correction/train_data_cleaned_g1.json \
    --tool_descriptions_path data/self_correction/train_data_cleaned_g1_api_list.json \
    --tool_root_dir $TOOL_ROOT_DIR \
    --toolbench_key $TOOLBENCH_KEY