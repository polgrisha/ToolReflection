#!/bin/bash

# original evaluation
# python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out ./eval_generations/eval_7b_testv1 \
#   -llm "/data5/about/ToolAlpaca/ToolAlpaca-7B" \
#   --agent_prompt test_v1 \
#   --real

# evaluation of reproduced 13B (2 epochs out of 3)
# mkdir ./eval_generations/eval_13b_2_epochs_reproduced_real_test_v1
# CUDA_VISIBLE_DEVICES=1 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out ./eval_generations/eval_13b_2_epochs_reproduced_real_test_v1 \
#   -llm checkpoints/vicuna-13b-toolalpaca/checkpoint-99 \
#   --agent_prompt test_v1 \
#   --real

# evaluation of reproduced 7B (3 epochs out of 3)
# mkdir ./eval_generations/eval_7b_reproduced_real_test_v1
# CUDA_VISIBLE_DEVICES=1 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out ./eval_generations/eval_7b_reproduced_real_test_v1 \
#   -llm checkpoints/vicuna-7b-toolalpaca/checkpoint-93 \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api ./eval_generations/eval_7b_reproduced_real_test_v1/api_data_0_11.json  -out ./eval_results/eval_7b_reproduced_real

# evaluation of 7B trained on cleaned train (3 epochs out of 3)
# mkdir ./eval_generations/eval_7b_cleaned_train_real_test_v1
# CUDA_VISIBLE_DEVICES=1 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out ./eval_generations/eval_7b_cleaned_train_real_test_v1 \
#   -llm checkpoints/vicuna-7b-toolalpaca_cleaned_train_v1/checkpoint-75 \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api ./eval_generations/eval_7b_cleaned_train_real_test_v1/api_data_0_11.json  -out ./eval_results/eval_7b_cleaned_train_real

# evaluation of 7B trained on cleaned train v2
# mkdir ./eval_generations/eval_7b_cleaned_train_real_test_v2
# CUDA_VISIBLE_DEVICES=1 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out ./eval_generations/eval_7b_cleaned_train_real_test_v2 \
#   -llm checkpoints/vicuna-7b-toolalpaca_cleaned_train_v2/checkpoint-90 \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api ./eval_generations/eval_7b_cleaned_train_real_test_v2/api_data_0_11.json  -out ./eval_results/eval_7b_cleaned_train_v2_real

# evaluation of 7B trained on train with corrections (hallucinations + errors with parameters)
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_full_train_hallucinations_parameters_correction_real
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_correction_examples_wrong_params_hallucinations/checkpoint-93
# RESULTS_PATH="./eval_results/eval_7b_full_train_wrong_params_hallucinations_real"
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=1 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B trained on train part of the train
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_train_part_of_train_real_correct_eval
# CHECKPOINT_PATH="vicuna-7b-toolalpaca_train_on_train_part/checkpoint-54"
# RESULTS_PATH=./eval_results/eval_7b_train_part_of_train_real_correct_eval
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B trained on train part of the train + corrections on val (from scratch)
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_train_on_train_part_correctons_val_real
# CHECKPOINT_PATH="vicuna-7b-toolalpaca_train_on_train_part_correctons_val"
# RESULTS_PATH=./eval_results/eval_7b_train_on_train_part_correctons_val_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B trained on train part of train + corrections on train + corrections on val (from scratch)
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_train_on_train_part_correctons_train_val_real
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_train_on_train_part_correctons_train_val
# RESULTS_PATH=./eval_results/eval_7b_train_on_train_part_correctons_train_val_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B trained on train part of train (500 examples) + corrections on val
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_retrain_on_train_part_500_corrections_val_real
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_retrain_on_train_part_500_correctons_val/checkpoint-6
# RESULTS_PATH=./eval_results/eval_7b_retrain_on_train_part_500_correctons_val_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B trained on train part of train (500 examples) + corrections on train + corrections on val
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_retrain_on_train_part_500_corrections_train_val_real
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_retrain_on_train_part_500_correctons_train_val/checkpoint-8
# RESULTS_PATH=./eval_results/eval_7b_train_on_train_part_500_correctons_train_val_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B trained on train part of train without parameter errors
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_train_part_of_train_no_parameter_errors_real
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors/checkpoint-51
# RESULTS_PATH=./eval_results/eval_7b_train_on_train_part_no_invalid_params_errors_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# evaluation of 7B postfinetuned on 500 examples of train part of train (no parameter errors) + correction examples on val
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_val_real
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val/checkpoint-5
# RESULTS_PATH=./eval_results/eval_7b_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# evaluation of 7B postfinetuned on 500 examples of train part of train (no parameter errors) + correction examples on val with thoughts
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_val_internal_thoughts_real
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_internal_thoughts/checkpoint-5
# RESULTS_PATH=./eval_results/eval_7b_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_internal_thoughts_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# # evaluation of 7B postfinetuned on 500 examples of train part of train (no parameter errors) + correction examples on val with thoughts
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_val_real_v26_07
# CHECKPOINT_PATH=checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07/checkpoint-5
# RESULTS_PATH=./eval_results/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_val_real_v26_07
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# # evaluation of 7B postfinetuned on 500 examples of train part of train (no parameter errors) + correction examples on val with thoughts
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_val_real_v26_07
# CHECKPOINT_PATH=checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07/checkpoint-5
# RESULTS_PATH=./eval_results/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_val_real_v26_07
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# # evaluation of 7B finetuned on train part of train (no parameter errors)
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_train_on_train_part_no_invalid_params_errors_real_v26_07
# CHECKPOINT_PATH=checkpoints/vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors_v2/checkpoint-46
# RESULTS_PATH=./eval_results/eval_7b_train_on_train_part_no_invalid_params_errors_real_v26_07
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH


# # evaluation of 7B postfinetuned on 500 examples of train part of train (no parameter errors) + correction examples on val with thoughts
# # we postfinetune the latest checkpoint with smaller lr and warmup
# OUTPUT_FOLDER_PATH=./eval_generations/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07_v2_lower_lr_real
# CHECKPOINT_PATH=checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07_v2_lower_lrwe/checkpoint-21
# RESULTS_PATH=./eval_results/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07_v2_lower_lr_real
# mkdir $OUTPUT_FOLDER_PATH
# # CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
# #   -api ./data/eval_real.json \
# #   -out $OUTPUT_FOLDER_PATH \
# #   -llm $CHECKPOINT_PATH \
# #   --agent_prompt test_v1 \
# #   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B postfinetuned on 500 examples of train part of train (no parameter errors) + correction examples on train + val
# we postfinetune the latest checkpoint with smaller lr and warmup
# OUTPUT_FOLDER_PATH=./eval_generations/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07_v2_lower_lr_real
# CHECKPOINT_PATH=checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07_v2_lower_lrwe/checkpoint-21
# RESULTS_PATH=./eval_results/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07_v2_lower_lr_real
# mkdir $OUTPUT_FOLDER_PATH
# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# # evaluation of 7B postfinetuned on 500 examples of train part of train (no parameter errors) + correction examples on train and val
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_train_val_real_v26_07
# CHECKPOINT_PATH=checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_train_val_v26_07/checkpoint-40
# RESULTS_PATH=./eval_results/eval_7b_retrain_on_train_part_500_no_parameter_errors_corrections_train_val_real_v26_07

# mkdir $OUTPUT_FOLDER_PATH

# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# # evaluation of 7B trained from scratch on train part of train (no parameter errors) + correction examples on val
# OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_train_from_scratch_on_train_no_parameter_errors_corrections_val_real_v26_07
# CHECKPOINT_PATH=vicuna-7b-toolalpaca_from_scratch_on_full_train_no_invalid_params_errors_corrections_val_v26_07/checkpoint-150
# RESULTS_PATH=./eval_results/eval_7b_train_from_scratch_on_train_no_parameter_errors_corrections_val_real_v26_07

# mkdir $OUTPUT_FOLDER_PATH

# CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
#   -api ./data/eval_real.json \
#   -out $OUTPUT_FOLDER_PATH \
#   -llm $CHECKPOINT_PATH \
#   --agent_prompt test_v1 \
#   --real

# python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH

# evaluation of 7B trained from scratch on train part of train (no parameter errors) + correction examples on train and val
OUTPUT_FOLDER_PATH=./eval_generations/eval_7b_train_from_scratch_on_train_no_parameter_errors_corrections_train_val_real_v26_07
CHECKPOINT_PATH=vicuna-7b-toolalpaca_from_scratch_on_full_train_no_invalid_params_errors_corrections_train_val_v26_07/checkpoint-165
RESULTS_PATH=./eval_results/eval_7b_train_from_scratch_on_train_no_parameter_errors_corrections_train_val_real_v26_07

mkdir $OUTPUT_FOLDER_PATH

CUDA_VISIBLE_DEVICES=6 python instance_generation/generation.py \
  -api ./data/eval_real.json \
  -out $OUTPUT_FOLDER_PATH \
  -llm $CHECKPOINT_PATH \
  --agent_prompt test_v1 \
  --real

python evaluation.py -api $OUTPUT_FOLDER_PATH/api_data_0_11.json  -out $RESULTS_PATH