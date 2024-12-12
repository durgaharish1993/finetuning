
from peft import PeftModel
from transformers import AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")
model = PeftModel.from_pretrained(base_model, "larsoncarter/Christian-AI-LLAMA")