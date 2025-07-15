# building original training dataset
# python build_dataset.py --api_data_path   --output_path ./data/train_data_preprocessed

# building cleaned training dataset
# python build_dataset.py --api_data_path ./data/cleaned_train_v1.json  --output_path ./data/train_data_cleaned_v1_preprocessed

# building cleaned training dataset v2
# python build_dataset.py --api_data_path ./data/cleaned_train_v2_correct.json  --output_path ./data/train_data_cleaned_v2_preprocessed

# building dataset with error corrections v1
# python build_dataset.py --api_data_path ./data/correction_examples_wrong_params.json  --output_path ./data/train_data_correction_examples_wrong_params

# building dataset with error corrections and hallucinations v2
# python build_dataset_correction.py --prev_data_path ./data/train_data_preprocessed --api_data_path ./data/correction_examples_wrong_params_hallucinations.json  --output_path ./data/train_data_correction_examples_wrong_params_hallucinations

# building val train part of train splitted to train and validation
# python build_dataset.py --api_data_path ./data/train_data_val_part.json --output_path ./data/train_data_val_part

# building train part of train splitted to train and validation
# python build_dataset.py --api_data_path ./data/train_data_train_part.json --output_path ./data/train_data_train_part