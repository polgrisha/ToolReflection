# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES=0,1

# torchrun --nproc_per_node=2 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path huggyllama/llama-7b  \
#     --data_path  data/toolllama_G123_dfs_train.json \
#     --eval_data_path  data/toolllama_G123_dfs_eval.json \
#     --conv_template tool-llama-single-round \
#     --bf16 True \
#     --output_dir toolllama \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 2 \
#     --per_device_eval_batch_size 2 \
#     --gradient_accumulation_steps 8 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "epoch" \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --tf32 True \
#     --source_model_max_length 2048 \
#     --model_max_length 8192 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to none

# train toolllama from scratch on data cleaned from errors with Llama-2-7B-chat
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path data/llama-7b \
#     --data_path  data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_splitted.json \
#     --eval_data_path  data/toolllama_G123_dfs_eval.json \
#     --output_dir toollama_7B_trained_on_data_cleaned_with_llama_2_v2/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 100 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 2048 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"


# train toolllama-2 from scratch on data cleaned from errors with Llama-2-7B-chat
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path /data5/about/llama2/llama-2-7b-hf \
#     --data_path  data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_splitted.json \
#     --eval_data_path  data/toolllama_G123_dfs_eval.json \
#     --output_dir toollama_2_7B_trained_on_data_cleaned_with_llama_2/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 300 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 2048 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"

# # train toollama fro scratch on data cleaned from errors with Llama-2-7B-chat
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path /data5/about/llama-7b/ \
#     --data_path  data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_train.json \
#     --eval_data_path data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_val.json \
#     --output_dir toollama_7B_trained_on_data_cleaned_with_llama_2_train_part/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 300 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 2048 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"

# train toollama 2 fro scratch on data cleaned from errors with Llama-2-7B-chat
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path /data5/about/llama2/llama-2-7b-hf \
#     --data_path  data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_train.json \
#     --eval_data_path data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_val.json \
#     --output_dir toollama_2_7B_trained_on_data_cleaned_with_llama_2_train_part/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 300 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 4096 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"

# post train toollama on validation with errors (full validation, error corrections)
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path toollama_7B_trained_on_data_cleaned_with_llama_2_train_part/checkpoint-900 \
#     --data_path  data/toolbench_new_1311/self_correction_postfinetune/new_train_full_val_full_corrections.json \
#     --eval_data_path data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_val.json \
#     --output_dir toollama_7B_post_finetuned_full_val_error_correction/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 50 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 2048 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"


# post train toollama on validation with errors (validation of size error corrections, error corrections)
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path toollama_7B_trained_on_data_cleaned_with_llama_2_train_part/checkpoint-900 \
#     --data_path  data/toolbench_new_1311/self_correction_postfinetune/new_train_half_val_full_corrections.json \
#     --eval_data_path data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_val.json \
#     --output_dir toollama_7B_post_finetuned_half_val_error_correction/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 50 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 2048 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"

# post train toollama on train with errors (train of size error corrections, error corrections)
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path toollama_7B_trained_on_data_cleaned_with_llama_2_train_part/checkpoint-900 \
#     --data_path  data/toolbench_new_1311/self_correction_postfinetune/new_train_half_train_full_corrections.json \
#     --eval_data_path data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_val.json \
#     --output_dir toollama_7B_post_finetuned_half_train_error_correction/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 50 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 2048 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"

# # train from scratch on train + val + error corrections
# export PYTHONPATH=./
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

# python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
#     --model_name_or_path /data5/about/llama-7b/ \
#     --data_path  data/toolbench_new_1311/self_correction_postfinetune/from_scratch_full_train_val_corrections.json \
#     --eval_data_path data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_val.json \
#     --output_dir data/toollama_7B_from_scratch_full_train_full_val_corrections_v2/ \
#     --conv_template tool-llama-single-round \
#     --bf16 False \
#     --fp16 True \
#     --num_train_epochs 2 \
#     --per_device_train_batch_size 1 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 7 \
#     --evaluation_strategy "epoch" \
#     --prediction_loss_only \
#     --save_strategy "steps" \
#     --save_steps 300 \
#     --save_total_limit 8 \
#     --learning_rate 5e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.04 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --fsdp "full_shard auto_wrap" \
#     --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
#     --source_model_max_length 2048 \
#     --model_max_length 4096 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True \
#     --report_to "tensorboard"


# post train toollama on validation with errors (full validation, error corrections)
export PYTHONPATH=./
export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"

python -m torch.distributed.run --nproc_per_node=8 --master_port=20001 toolbench/train/train_mem.py \
    --model_name_or_path toollama_7B_trained_on_data_cleaned_with_llama_2_train_part/checkpoint-900 \
    --data_path data/toolbench_new_1311/self_correction_postfinetune/new_train_full_val_full_corrections_readable_correct.json \
    --eval_data_path data/toolbench_new_1311/cleaned_toolllama_G123_dfs_train_downloaded1311_no_undetectable_errors_final_train_val.json \
    --output_dir data/toollama_7B_post_finetuned_full_val_error_correction_attempt_2_12_06_2024_corrected/ \
    --conv_template tool-llama-single-round \
    --bf16 False \
    --fp16 True \
    --num_train_epochs 2 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 7 \
    --evaluation_strategy "epoch" \
    --prediction_loss_only \
    --save_strategy "steps" \
    --save_steps 50 \
    --save_total_limit 8 \
    --learning_rate 5e-6 \
    --weight_decay 0. \
    --warmup_ratio 0.04 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
    --source_model_max_length 2048 \
    --model_max_length 4096 \
    --gradient_checkpointing True \
    --lazy_preprocess True \
    --report_to "tensorboard"