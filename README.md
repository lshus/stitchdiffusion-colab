### I have implemented stitchdiffusion based on diffusers to generate 360-degree panoramas through text prompts. The detailed steps of installation and model inference are in the following.


#### [Attention] This colab is not working due to the updated google colab again, I don't plan to fix it.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lshus/stitchdiffusion-colab/blob/main/colab_stitchdiffusion.ipynb) 
#### [Next Step] To achieve 2048x1024 (2K) 360-degree panorama based on SDXL+StitchDiffusion in Feb 2025.

 



## 1. Create Environment

Recommend to use [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) here.
   ```
   conda create -n stitchdiffusion python=3.9
   conda activate stitchdiffusion
   conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia
   ```

## 2. Packages Installation

Step 1.
```
git clone https://github.com/lshus/stitchdiffusion-colab.git
```
Step 2.
```
pip install -r requirements.txt
```

## 3. Download LoRA file

Step 1.
[Download link](https://drive.google.com/file/d/1MiaG8v0ZmkTwwrzIEFtVoBj-Jjqi_5lz/view) of LoRA from [StitchDiffusion](https://github.com/littlewhitesea/StitchDiffusion)

Step 2. (Since I implemented it based on diffusers, some key names in the LoRA require to be changed for consistency. Before you run lora_modified.py, remember to modify "YOUR_PATH" in this file. Finally, you can get a file called "lora_modified.safetensors", which will be used later.)
```
python lora_modified.py
```

## 4. 360 Panorama Generation.

Step 1. Remeber to change "YOUR_PATH" in this stitchdiffusion_360_gen.py.

Step 2. Specify the input prompt. (360-degree panoramic image is the trigger word, if you want to generate a 360-degree panorama, the input prompt should include it.)

Step 3. Run the file.
```
python stitchdiffusion_360_gen.py
```



## Acknowledgement
 
Many thanks to [kohya-trainer](https://github.com/Linaqruf/kohya-trainer), [StitchDiffusion](https://github.com/littlewhitesea/StitchDiffusion) and [diffusers](https://github.com/huggingface/diffusers) for their open-source code. 
