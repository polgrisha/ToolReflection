 #!/bin/bash

EVAL_SEQUENTIALLY_ON_DEVICE="0" 

BASE_MODEL=""
ADAPTER_NAME=""
PROMPT_TEMPLATE_PATH=""

# Thitry-Tools:
TEST_DATA_DIR=""
TTS=""
DATASET_LIST=()

LORA_WEIGHTS=
LOG_DIR=


mkdir -p $LOG_DIR
mkdir -p $LOG_DIR/$TTS

for i in ${!DATASET_LIST[@]}
do
    TEST_DATA_PATH="$TEST_DATA_DIR/${DATASET_LIST[i]}_data.json"
    LOG_PATH="$LOG_DIR/${DATASET_LIST[i]}.json"
    SCRIPT_ARGS="--test_data_path $TEST_DATA_PATH --lora_weights $LORA_WEIGHTS --base_model $BASE_MODEL --output_path $LOG_PATH --prompt_template_path $PROMPT_TEMPLATE_PATH"

    echo "run sequentially on device $EVAL_SEQUENTIALLY_ON_DEVICE: $TEST_DATA_PATH"
    CUDA_VISIBLE_DEVICES=$EVAL_SEQUENTIALLY_ON_DEVICE python evaluation/generate.py $SCRIPT_ARGS
done
