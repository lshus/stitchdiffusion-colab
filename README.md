[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lshus/stitchdiffusion-colab/blob/main/colab_stitchdiffusion.ipynb) 
 

#### It seems this colab is not working due to the updated google colab again, I don't plan to fix it. 

### I have implemented stitchdiffusion based on diffusers to generate 360-degree panoramas through text prompts.

## Create Environment

Recommend to use [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) here.
   ```
   conda create -n stitch python=3.9
   conda activate stitch
   conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia
   ```

## Packages Installation


 
Many thanks to [kohya-trainer](https://github.com/Linaqruf/kohya-trainer), [StitchDiffusion](https://github.com/littlewhitesea/StitchDiffusion) and [diffusers](https://github.com/huggingface/diffusers) for their open-source code. 
