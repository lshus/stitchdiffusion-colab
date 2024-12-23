from safetensors.torch import load_file, save_file
import torch

import pdb


def print_state_dict_keys(lora_path):
    """
    Loads a safetensors file and prints all the keys in the state_dict.

    Args:
        lora_path: Path to the lora.safetensors file.
    """

    try:
        state_dict = load_file(lora_path)
        print("Keys in the state_dict:")
        for key in state_dict.keys():
            print(key)
    except Exception as e:
        print(f"Error loading or processing the file: {e}")



def reshape_lora_weights(lora_path, output_path):
    """
    Reshapes LoRA weights in a safetensors file to remove potentially problematic dimensions.
    Specifically addresses issues with 1x1 convolutions in LoRA weights.

    Args:
        lora_path: Path to the input lora.safetensors file.
        output_path: Path to save the modified safetensors file.
    """

    state_dict = load_file(lora_path)
    new_state_dict = {}

    for key, value in state_dict.items():
        # pdb.set_trace()
        if "lora_down" in key or "lora_up" in key:
            # Target specific problematic patterns:
            # Case 1: [..., 1, 1] -> [...]
            # pdb.set_trace()
            if len(value.shape) == 4 and value.shape[2] == 1 and value.shape[3] == 1:
                print(f"Reshaping (case 1) {key} from {value.shape} to {value.reshape(value.shape[:2]).shape}")
                new_state_dict[key] = value.reshape(value.shape[:2])
            # Case 2: [..., x, 1] -> [...]  where x > 1
            elif len(value.shape) == 3 and value.shape[2] == 1:
                print(f"Reshaping (case 2) {key} from {value.shape} to {value.reshape(value.shape[:2]).shape}")
                new_state_dict[key] = value.reshape(value.shape[:2])
             # Case 3: [..., 1, x] -> [...] where x > 1
            elif len(value.shape) == 3 and value.shape[1] == 1:
                print(f"Reshaping (case 3) {key} from {value.shape} to {value.reshape(value.shape[0], value.shape[2]).shape}")
                new_state_dict[key] = value.reshape(value.shape[0], value.shape[2])
            # Case 4: [..., 1] -> [...]
            elif len(value.shape) in [2, 3, 4] and value.shape[-1] == 1:
                print(f"Reshaping (case 4) {key} from {value.shape} to {value.reshape(value.shape[:-1]).shape}")
                new_state_dict[key] = value.reshape(value.shape[:-1])
            else:
                new_state_dict[key] = value
        else:
            new_state_dict[key] = value

    save_file(new_state_dict, output_path)

# Example usage:
lora_checkpoint_path = "YOUR_PATH/lora.safetensors"  # Your original LoRA file
modified_lora_path = "YOUR_PATH/lora_modified.safetensors"  # Path to save the modified file

reshape_lora_weights(lora_checkpoint_path, modified_lora_path)

print(f"Modified LoRA checkpoint saved to {modified_lora_path}")

# print_state_dict_keys(lora_checkpoint_path)