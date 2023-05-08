 <!-- # <p align=center>`awesome gan-inversion`</p> -->
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

<br />
<p align="center">
  <h1 align="center">Awesome Diffusion Personalization</h1>
</p>
<br />

We are focusing on how to efficiently learn a `concept`/`object`/`style` based on large diffusion models. 

## 🎉 Feature
- [x] **Personalization**: Learning a ```concept``` from few data and generate images containing it.
- [ ] **Inversion** [Doing]: Inverting images into `latent representation` (e.g., text_embedding, latent_code, etc.) which can reconstruct the input image. Then editing methods can be applied to it to manipulate given images.
- [ ] **Editing** [TODO]: Editing the latent representation to manipulate the generated images.
- [x] **Parameter-Efficient Fine-Tuning**: Inspired by LLM, we can speed up optimization process by various mechanisms.

## ⭐ Personalization Methods
**DisenBooth: Disentangled Parameter-Efficient Tuning for Subject-Driven Text-to-Image Generation.**<br>
*Hong Chen, Yipeng Zhang, Xin Wang, Xuguang Duan, Yuwei Zhou, Wenwu Zhu.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2305.03374v1)]

**Key-Locked Rank One Editing for Text-to-Image Personalization.**<br>
*Yoad Tewel, Rinon Gal, Gal Chechik, Yuval Atzmon.*<br>
SIGGRAPH 2023. [[PDF](http://arxiv.org/abs/2305.01644v1)][[Link](https://research.nvidia.com/labs/par/Perfusion/)]

**Identity Encoder for Personalized Diffusion.**<br>
*Yu-Chuan Su, Kelvin C. K. Chan, Yandong Li, Yang Zhao, Han Zhang, Boqing Gong, Huisheng Wang, Xuhui Jia.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.07429v1)]

**DiffFit: Unlocking Transferability of Large Diffusion Models Via Simple Parameter-Efficient Fine-Tuning.**<br>
*Enze Xie, Lewei Yao, Han Shi, Zhili Liu, Daquan Zhou, Zhaoqiang Liu, Jiawei Li, Zhenguo Li.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.06648v5)]

**Continual Diffusion: Continual Customization of Text-to-Image Diffusion with C-LoRA.**<br>
*James Seale Smith, Yen-Chang Hsu, Lingyu Zhang, Ting Hua, Zsolt Kira, Yilin Shen, Hongxia Jin.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.06027v1)][[Link](https://jamessealesmith.github.io/continual-diffusion/)]

**Gradient-Free Textual Inversion.**<br>
*Zhengcong Fei, Mingyuan Fan, Junshi Huang.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.05818v1)]

**Controllable Textual Inversion for Personalized Text-to-Image Generation.**<br>
*Jianan Yang, Haobo Wang, Ruixuan Xiao, Sai Wu, Gang Chen, Junbo Zhao.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.05265v2)][[Link](https://github.com/jnzju/COTI)]

**InstantBooth: Personalized Text-to-Image Generation Without Test-Time Finetuning.**<br>
*Jing Shi, Wei Xiong, Zhe Lin, Hyun Joon Jung.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.03411v1)]

**Taming Encoder for Zero Fine-tuning Image Customization with Text-to-Image Diffusion Models.**<br>
*Xuhui Jia, Yang Zhao, Kelvin C. K. Chan, Yandong Li, Han Zhang, Boqing Gong, Tingbo Hou, Huisheng Wang, Yu-Chuan Su.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.02642v1)]

**Subject-driven Text-to-Image Generation Via Apprenticeship Learning.**<br>
*Wenhu Chen, Hexiang Hu, Yandong Li, Nataniel Ruiz, Xuhui Jia, Ming-Wei Chang, William W. Cohen.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.00186v2)]

**A Closer Look at Parameter-Efficient Tuning in Diffusion Models.**<br>
*Chendong Xiang, Fan Bao, Chongxuan Li, Hang Su, Jun Zhu.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2303.18181v2)][[Link](https://github.com/Xiang-cd/unet-finetune)]

**SVDiff: Compact Parameter Space for Diffusion Fine-Tuning.**<br>
*Ligong Han, Yinxiao Li, Han Zhang, Peyman Milanfar, Dimitris Metaxas, Feng Yang.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2303.11305v3)]

**$P+$: Extended Textual Conditioning in Text-to-Image Generation.**<br>
*Andrey Voynov, Qinghao Chu, Daniel Cohen-Or, Kfir Aberman.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2303.09522v2)]

**Cones: Concept Neurons in Diffusion Models for Customized Generation.**<br>
*Zhiheng Liu, Ruili Feng, Kai Zhu, Yifei Zhang, Kecheng Zheng, Yu Liu, Deli Zhao, Jingren Zhou, Yang Cao.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2303.05125v1)]

**ELITE: Encoding Visual Concepts Into Textual Embeddings for Customized Text-to-Image Generation.**<br>
*Yuxiang Wei, Yabo Zhang, Zhilong Ji, Jinfeng Bai, Lei Zhang, Wangmeng Zuo.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2302.13848v1)]

**Encoder-based Domain Tuning for Fast Personalization of Text-to-Image Models.**<br>
*Rinon Gal, Moab Arar, Yuval Atzmon, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2302.12228v3)][[Link](https://tuning-encoder.github.io/)]

**Is This Loss Informative? Speeding Up Textual Inversion with Deterministic Objective Evaluation.**<br>
*Anton Voronov, Mikhail Khoroshikh, Artem Babenko, Max Ryabinin.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2302.04841v1)][[Link](https://github.com/yandex-research/DVAR.)]

**SINE: SINgle Image Editing with Text-to-Image Diffusion Models.**<br>
*Zhixing Zhang, Ligong Han, Arnab Ghosh, Dimitris Metaxas, Jian Ren.*<br>
arXiv 2022. [[PDF](http://arxiv.org/abs/2212.04489v1)][[Link](https://zhang-zx.github.io/SINE/)]

**Multi-Concept Customization of Text-to-Image Diffusion.**<br>
*Nupur Kumari, Bingliang Zhang, Richard Zhang, Eli Shechtman, Jun-Yan Zhu.*<br>
arXiv 2022. [[PDF](http://arxiv.org/abs/2212.04488v1)][[Link](https://www.cs.cmu.edu/~custom-diffusion)]

**An Image Is Worth One Word: Personalizing Text-to-Image Generation Using Textual Inversion.**<br>
*Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
arXiv 2022. [[PDF](http://arxiv.org/abs/2208.01618v1)][[Link](https://textual-inversion.github.io)]

**DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation.**<br>
*Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, Kfir Aberman.*<br>
CVPR 2023. [[PDF](http://arxiv.org/abs/2208.12242v2)][[Link](https://dreambooth.github.io/)]

## 🏹 Inversion
**NULL-text Inversion for Editing Real Images using Guided Diffusion Models.**<br>
*Ron Mokady, Amir Hertz, Kfir Aberman, Yael Pritch, Daniel Cohen-Or.*<br> 
CVPR 2023. [PDF] [Project] [Github]

**EDICT: Exact Diffusion Inversion via Coupled Transformations.**<br>
*Bram Wallace, Akash Gokul, Nikhil Naik.*<br> 
CVPR 2023. [PDF] [Github]

**An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion.**<br>
*Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br> 
ICLR 2023 (Oral). [PDF] [Project] [Github]

**Prompt-to-Prompt Image Editing with Cross Attention Control.**<br>
Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, Daniel Cohen-Or.*<br> 
ICLR 2023. [PDF] [Project] [Github]
:high_speed_train:

## 🎨 Editing
TODO

## 🚄 Parameter-Efficient Fine-Tuning
The NLP PEFT methods which have been proposed to diffusion models are marked by 📌, and the methods designed for diffusion are marked by 💎.

**💎 A Closer Look at Parameter-Efficient Tuning in Diffusion Models.**<br>
*Chendong Xiang, Fan Bao, Chongxuan Li, Hang Su, Jun Zhu.*<br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2303.18181v2)][[Link](https://github.com/Xiang-cd/unet-finetune)]

**📌 DyLoRA: Parameter Efficient Tuning of Pre-trained Models Using Dynamic Search-Free Low-Rank Adaptation.**<br>
*Mojtaba Valipour, Mehdi Rezagholizadeh, Ivan Kobyzev, Ali Ghodsi.*<br>
arXiv 2022. [[PDF](http://arxiv.org/abs/2210.07558v2)] [[Diffusion Impl.:KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS/tree/main)]

**📌 FedPara: Low-Rank Hadamard Product for Communication-Efficient Federated Learning.**<br>
*Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh.*<br>
ICLR 2022. [[PDF](http://arxiv.org/abs/2108.06098v3)] [[Diffusion Impl.:KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS/tree/main)]

**📌 Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning**<br>
*Haokun Liu, Derek Tam, Mohammed Muqeeth, Jay Mohta, Tenghao Huang, Mohit Bansal, Colin A. Raffel*<br>
NIPS 2022. [[PDF](https://proceedings.neurips.cc/paper_files/paper/2022/file/0cde695b83bd186c1fd456302888454c-Paper-Conference.pdf)] [[Diffusion Impl.:KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS/tree/main)]

**📌 LoRA: Low-Rank Adaptation of Large Language Models.**<br>
*Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen.*<br>
arXiv 2021. [[PDF](http://arxiv.org/abs/2106.09685v2)]

**The Power of Scale for Parameter-Efficient Prompt Tuning.**<br>
*Brian Lester, Rami Al-Rfou, Noah Constant.*<br>
EMNLP 2021. [[PDF](http://arxiv.org/abs/2104.08691v2)]

**Prefix-Tuning: Optimizing Continuous Prompts for Generation.**<br>
*Xiang Lisa Li, Percy Liang.*<br>
ACL 2021. [[PDF](http://arxiv.org/abs/2101.00190v1)]

**Parameter-Efficient Transfer Learning for NLP.**<br>
*Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly.*<br>
PMLR 2019. [[PDF](http://arxiv.org/abs/1902.00751v2)]
