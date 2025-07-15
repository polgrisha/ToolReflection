python instance_generation/generation.py \
  -api ./data/train_data_no_instances.json \
  -out ./eval_generations/eval_7b_testv1_train \
  -llm /data5/about/ToolAlpaca/ToolAlpaca-7B \
  --agent_prompt test_v1 \
  --server_url "http://127.0.0.1:5678"