# CUDA_VISIBLE_DEVICES="0,1,2,3,4,5" deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path data/train_data_preprocessed \
#     --fp16 True \
#     --output_dir checkpoints/vicuna-7b-toolalpaca/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed oolAlpaca/configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path ToolAlpaca/data/train_data_cleaned_v1_preprocessed \
#     --fp16 True \
#     --output_dir ToolAlpaca/checkpoints/vicuna-7b-toolalpaca_cleaned_train_v1/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# train 13B on cleaned_train 
# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna_13B \
#     --data_path data/train_data_preprocessed \
#     --fp16 True \
#     --output_dir checkpoints/vicuna-7b-toolalpaca/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 6 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# train 7B on correctly cleaned train
# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path ata/train_data_cleaned_v2_preprocessed \
#     --fp16 True \
#     --output_dir checkpoints/vicuna-7b-toolalpaca_cleaned_train_v2/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# train 7B on full train + error corrections + hallucinations
# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path data/train_data_correction_examples_wrong_params_hallucinations \
#     --fp16 True \
#     --output_dir checkpoints/vicuna-7b-toolalpaca_correction_examples_wrong_params_hallucinations/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# train 7B on train part of train splitted to train and validation
# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path data/train_data_train_part \
#     --fp16 True \
#     --output_dir vicuna-7b-toolalpaca_train_on_train_part/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# self correction experiment train from scratch on train + corrections on val
# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path data/train_new_corrections_val\
#     --fp16 True \
#     --output_dir vicuna-7b-toolalpaca_train_on_train_part_corrections_val/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# train from scratch on data without parameter errors
# CUDA_VISIBLE_DEVICES="0,1,2,3,4,5" deepspeed --num_gpus=6 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path data/train_data_train_part_no_invalid_params_errors \
#     --fp16 True \
#     --output_dir vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors_v2/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# # postfinetune on data without parameter errors (500 examples) + correction examples
# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors/ \
#     --data_path data/train_new_part_corrections_val_no_invalid_params_errors \
#     --fp16 True \
#     --output_dir vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# train from scratch on data without parameter errors + correction examples with internal thoughts

# postfinetune on data without parameter errors (500 examples) + correction examples with internal thoughts
# deepspeed --num_gpus=8 --master_port=12345 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors/ \
#     --data_path data/train_new_part_corrections_val_no_invalid_params_errors_internal_thoughts \
#     --fp16 True \
#     --output_dir vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_internal_thoughts/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# # postfinetune on data without parameter errors (500 examples) + correction examples, 26 07 
# deepspeed --num_gpus=8 --master_port=17817 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors/ \
#     --data_path data/train_new_part_corrections_val_no_invalid_params_errors_v26_07 \
#     --fp16 True \
#     --output_dir checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# # postfinetune on data without parameter errors (500 examples) + correction examples on val, 26 07 
# # --deepspeed configs/dc_config.json \
# DS_SKIP_CUDA_CHECK=1 python -m torch.distributed.run  --nproc_per_node=6 --master_port=17817 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path checkpoints/vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors_v2/checkpoint-46-hf \
#     --data_path data/train_new_part_corrections_val_no_invalid_params_errors_v26_07 \
#     --fp16 True \
#     --output_dir checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_val_v26_07_v3_lower_lr/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 2 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 1e-5 \
#     --weight_decay 0. \
#     --warmup_steps 0. \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# # postfinetune on data without parameter errors (500 examples) + correction examples on train val, 26 07 
# deepspeed --num_gpus=6 --master_port=17817 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path vicuna-7b-toolalpaca_train_on_train_part_no_invalid_params_errors/ \
#     --data_path data/train_new_part_corrections_train_val_no_invalid_params_errors_v26_07 \
#     --fp16 True \
#     --output_dir checkpoints/vicuna-7b-toolalpaca_retrain_on_train_part_500_no_invalid_params_errors_corrections_train_val_v26_07/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 1 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# # fine tune from scratch on full train data without parameter errors + correction examples on val, 04 09 
# CUDA_VISIBLE_DEVICES="0,1,2,3,4,6" deepspeed --num_gpus=6 --master_port=17817 train.py \
#     --deepspeed configs/dc_config.json \
#     --model_name_or_path /data5/about/vicuna-7b-v1.1 \
#     --data_path data/train_new_corrections_val_no_invalid_params_errors_v26_07 \
#     --fp16 True \
#     --output_dir vicuna-7b-toolalpaca_from_scratch_on_full_train_no_invalid_params_errors_corrections_val_v26_07/ \
#     --num_train_epochs 3 \
#     --per_device_train_batch_size 8 \
#     --per_device_eval_batch_size 1 \
#     --gradient_accumulation_steps 1 \
#     --evaluation_strategy "no" \
#     --save_strategy "epoch" \
#     --save_total_limit 10 \
#     --learning_rate 2e-5 \
#     --weight_decay 0. \
#     --warmup_ratio 0.03 \
#     --lr_scheduler_type "cosine" \
#     --logging_steps 1 \
#     --model_max_length 2048 \
#     --gradient_checkpointing True \
#     --lazy_preprocess True

# fine tune from scratch on full train data without parameter errors + correction examples on val, 04 09 
CUDA_VISIBLE_DEVICES="0,1,2,3,4,6" deepspeed --num_gpus=6 --master_port=17817 train.py \
    --deepspeed configs/dc_config.json \
    --model_name_or_path /data5/about/vicuna-7b-v1.1 \
    --data_path data/train_new_corrections_train_val_no_invalid_params_errors_v26_07 \
    --fp16 True \
    --output_dir vicuna-7b-toolalpaca_from_scratch_on_full_train_no_invalid_params_errors_corrections_train_val_v26_07/ \
    --num_train_epochs 3 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "epoch" \
    --save_total_limit 10 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --lazy_preprocess True




