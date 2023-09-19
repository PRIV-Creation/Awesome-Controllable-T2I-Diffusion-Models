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

## 🌈 UniDiffusion
We are building a Diffusion Training repository [UniDiffusion](https://github.com/PRIV-Creation/UniDiffusion). UniDiffusion is aimed at researchers and users who wish to deeply customize the training of stable diffusion. We hope that this code repository can provide excellent support for future research and application extensions.

## 🎉 Feature
- [ ] **Codebase**: Codebase for diffusion model personalization.
- [x] **Personalization**: Learning a ```concept``` from few data and generate images containing it.
- [x] **Inversion** [Doing]: Inverting images into `latent representation` (e.g., text_embedding, latent_code, etc.) which can reconstruct the input image. Then editing methods can be applied to it to manipulate given images.
- [x] **Editing** [TODO]: Editing the latent representation to manipulate the generated images.
- [x] **Parameter-Efficient Fine-Tuning**: Inspired by LLM, we can speed up optimization process by various mechanisms.

## Codebase
Doing

## ⭐ Personalization Methods
**FaceChain: A Playground for Identity-Preserving Portrait Generation.**<br>
*Yang Liu, Cheng Yu, Lei Shang , Ziheng Wu, Xingjun Wang, Yuze Zhao, Lin Zhu, Chen Cheng, Weitao Che, Chao Xu, Haoyu Xie, Yuan Yao, Wenmeng Zhou, Yingda Chen, Xuansong Xie, Baigui Sun*<br>
arXiv 2023.08. [[PDF](https://arxiv.org/abs/2308.14256)][[Github](https://github.com/modelscope/facechain)]

**HyperDreamBooth: HyperNetworks for Fast Personalization of Text-to-Image Models.**<br>
*Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Wei Wei, Tingbo Hou, Yael Pritch, Neal Wadhwa, Michael Rubinstein, Kfir Aberman.*<br>
arXiv 2023.07. [[PDF](http://arxiv.org/abs/2307.06949v1)][[Github](https://hyperdreambooth.github.io)]

**Domain-Agnostic Tuning-Encoder for Fast Personalization of Text-To-Image Models.**<br>
*Moab Arar, Rinon Gal, Yuval Atzmon, Gal Chechik, Daniel Cohen-Or, Ariel Shamir, Amit H. Bermano.*<br>
arXiv 2023.07. [[PDF](http://arxiv.org/abs/2307.06925v1)][[Github](https://datencoder.github.io)]

**AvatarBooth: High-Quality and Customizable 3D Human Avatar Generation.**<br>
*Yifei Zeng, Yuanxun Lu, Xinya Ji, Yao Yao, Hao Zhu, Xun Cao.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.09864v1)][[Github](https://zeng-yifei.github.io/avatarbooth_page/)]

**Controlling Text-to-Image Diffusion by Orthogonal Finetuning.**<br>
*Zeju Qiu, Weiyang Liu, Haiwen Feng, Yuxuan Xue, Yao Feng, Zhen Liu, Dan Zhang, Adrian Weller, Bernhard Schölkopf.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.07280v1)][[Link](https://oft.wyliu.com/))]

**Face0: Instantaneously Conditioning A Text-to-Image Model on A Face.**<br>
*Dani Valevski, Danny Wasserman, Yossi Matias, Yaniv Leviathan.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.06638v1)]

**Cones 2: Customizable Image Synthesis with Multiple Subjects.**<br>
*Zhiheng Liu, Yifei Zhang, Yujun Shen, Kecheng Zheng, Kai Zhu, Ruili Feng, Yu Liu, Deli Zhao, Jingren Zhou, Yang Cao.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.19327v1)]

**Mix-of-Show: Decentralized Low-Rank Adaptation for Multi-Concept Customization of Diffusion Models.**<br>
*Yuchao Gu, Xintao Wang, Jay Zhangjie Wu, Yujun Shi, Yunpeng Chen, Zihan Fan, Wuyou Xiao, Rui Zhao, Shuning Chang, Weijia Wu, Yixiao Ge, Ying Shan, Mike Zheng Shou.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.18292v1)]

**Photoswap: Personalized Subject Swapping in Images.**<br>
*Jing Gu, Yilin Wang, Nanxuan Zhao, Tsu-Jui Fu, Wei Xiong, Qing Liu, Zhifei Zhang, He Zhang, Jianming Zhang, HyunJoon Jung, Xin Eric Wang.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.18286v1)]

**BLIP-Diffusion: Pre-trained Subject Representation for Controllable Text-to-Image Generation and Editing.**<br>
*Dongxu Li, Junnan Li, Steven C. H. Hoi.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.14720v2)]

**FastComposer: Tuning-Free Multi-Subject Image Generation with Localized Attention.**<br>
*Guangxuan Xiao, Tianwei Yin, William T. Freeman, Frédo Durand, Song Han.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.10431v2)]

**DisenBooth: Identity-Preserving Disentangled Tuning for Subject-Driven Text-to-Image Generation.**<br>
*Hong Chen, Yipeng Zhang, Xin Wang, Xuguang Duan, Yuwei Zhou, Wenwu Zhu.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.03374v2)]

**Key-Locked Rank One Editing for Text-to-Image Personalization.**<br>
*Yoad Tewel, Rinon Gal, Gal Chechik, Yuval Atzmon.*<br>
SIGGRAPH 2023. [[PDF](http://arxiv.org/abs/2305.01644v1)][[Link](https://research.nvidia.com/labs/par/Perfusion/)]

**Identity Encoder for Personalized Diffusion.**<br>
*Yu-Chuan Su, Kelvin C. K. Chan, Yandong Li, Yang Zhao, Han Zhang, Boqing Gong, Huisheng Wang, Xuhui Jia.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.07429v1)]

**DiffFit: Unlocking Transferability of Large Diffusion Models Via Simple Parameter-Efficient Fine-Tuning.**<br>
*Enze Xie, Lewei Yao, Han Shi, Zhili Liu, Daquan Zhou, Zhaoqiang Liu, Jiawei Li, Zhenguo Li.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.06648v5)]

**Continual Diffusion: Continual Customization of Text-to-Image Diffusion with C-LoRA.**<br>
*James Seale Smith, Yen-Chang Hsu, Lingyu Zhang, Ting Hua, Zsolt Kira, Yilin Shen, Hongxia Jin.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.06027v1)][[Github](https://jamessealesmith.github.io/continual-diffusion/)]

**Gradient-Free Textual Inversion.**<br>
*Zhengcong Fei, Mingyuan Fan, Junshi Huang.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.05818v1)]

**Controllable Textual Inversion for Personalized Text-to-Image Generation.**<br>
*Jianan Yang, Haobo Wang, Ruixuan Xiao, Sai Wu, Gang Chen, Junbo Zhao.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.05265v2)][[Github](https://github.com/jnzju/COTI)]

**InstantBooth: Personalized Text-to-Image Generation Without Test-Time Finetuning.**<br>
*Jing Shi, Wei Xiong, Zhe Lin, Hyun Joon Jung.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.03411v1)]

**Taming Encoder for Zero Fine-tuning Image Customization with Text-to-Image Diffusion Models.**<br>
*Xuhui Jia, Yang Zhao, Kelvin C. K. Chan, Yandong Li, Han Zhang, Boqing Gong, Tingbo Hou, Huisheng Wang, Yu-Chuan Su.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.02642v1)]

**Subject-driven Text-to-Image Generation Via Apprenticeship Learning.**<br>
*Wenhu Chen, Hexiang Hu, Yandong Li, Nataniel Ruiz, Xuhui Jia, Ming-Wei Chang, William W. Cohen.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.00186v4)]

**A Closer Look at Parameter-Efficient Tuning in Diffusion Models.**<br>
*Chendong Xiang, Fan Bao, Chongxuan Li, Hang Su, Jun Zhu.*<br>
arXiv 2023.03. [[PDF](http://arxiv.org/abs/2303.18181v2)][[Github](https://github.com/Xiang-cd/unet-finetune)]

**SVDiff: Compact Parameter Space for Diffusion Fine-Tuning.**<br>
*Ligong Han, Yinxiao Li, Han Zhang, Peyman Milanfar, Dimitris Metaxas, Feng Yang.*<br>
arXiv 2023.03. [[PDF](http://arxiv.org/abs/2303.11305v4)]

**P+: Extended Textual Conditioning in Text-to-Image Generation.**<br>
*Andrey Voynov, Qinghao Chu, Daniel Cohen-Or, Kfir Aberman.*<br>
arXiv 2023.03. [[PDF](http://arxiv.org/abs/2303.09522v3)]

**Cones: Concept Neurons in Diffusion Models for Customized Generation.**<br>
*Zhiheng Liu, Ruili Feng, Kai Zhu, Yifei Zhang, Kecheng Zheng, Yu Liu, Deli Zhao, Jingren Zhou, Yang Cao.*<br>
arXiv 2023.03. [[PDF](http://arxiv.org/abs/2303.05125v1)]

**ELITE: Encoding Visual Concepts Into Textual Embeddings for Customized Text-to-Image Generation.**<br>
*Yuxiang Wei, Yabo Zhang, Zhilong Ji, Jinfeng Bai, Lei Zhang, Wangmeng Zuo.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.13848v1)]

**Encoder-based Domain Tuning for Fast Personalization of Text-to-Image Models.**<br>
*Rinon Gal, Moab Arar, Yuval Atzmon, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.12228v3)][[Github](https://tuning-encoder.github.io/)]

**Is This Loss Informative? Faster Text-to-Image Customization by Tracking Objective Dynamics.**<br>
*Anton Voronov, Mikhail Khoroshikh, Artem Babenko, Max Ryabinin.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.04841v2)][[Github](https://github.com/yandex-research/DVAR.)]

**SINE: SINgle Image Editing with Text-to-Image Diffusion Models.**<br>
*Zhixing Zhang, Ligong Han, Arnab Ghosh, Dimitris Metaxas, Jian Ren.*<br>
arXiv 2022.12. [[PDF](http://arxiv.org/abs/2212.04489v1)][[Github](https://zhang-zx.github.io/SINE/)]

**Multi-Concept Customization of Text-to-Image Diffusion.**<br>
*Nupur Kumari, Bingliang Zhang, Richard Zhang, Eli Shechtman, Jun-Yan Zhu.*<br>
arXiv 2022.12. [[PDF](http://arxiv.org/abs/2212.04488v2)][[Link](https://www.cs.cmu.edu/~custom-diffusion/dataset.html)][[Link](https://www.cs.cmu.edu/~custom-diffusion)]

**DreamArtist: Towards Controllable One-Shot Text-to-Image Generation Via Positive-Negative Prompt-Tuning.**<br>
*Ziyi Dong, Pengxu Wei, Liang Lin.*<br>
arXiv 2022.11. [[PDF](http://arxiv.org/abs/2211.11337v3)]

**An Image Is Worth One Word: Personalizing Text-to-Image Generation Using Textual Inversion.**<br>
*Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
arXiv 2022.08. [[PDF](http://arxiv.org/abs/2208.01618v1)][[Github](https://textual-inversion.github.io)]

**DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation.**<br>
*Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, Kfir Aberman.*<br>
CVPR 2023. [[PDF](http://arxiv.org/abs/2208.12242v2)][[Github](https://dreambooth.github.io/)]

## 🏹 Inversion
**Negative-prompt Inversion: Fast Image Inversion for Editing with Text-guided Diffusion Models.**<br>
*Daiki Miyake, Akihiro Iohara, Yu Saito, Toshiyuki Tanaka.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.16807v1)]

**Prompt Tuning Inversion for Text-Driven Image Editing Using Diffusion Models.**<br>
*Wenkai Dong, Song Xue, Xiaoyue Duan, Shumin Han.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.04441v1)]

**Guided Image Synthesis Via Initial Image Editing in Diffusion Model.**<br>
*Jiafeng Mao, Xueting Wang, Kiyoharu Aizawa.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.03382v1)]

**An Edit Friendly DDPM Noise Space: Inversion and Manipulations.**<br>
*Inbar Huberman-Spiegelglas, Vladimir Kulikov, Tomer Michaeli.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.06140v2)]

**Hard Prompts Made Easy: Gradient-Based Discrete Optimization for Prompt Tuning and Discovery.**<br>
*Yuxin Wen, Neel Jain, John Kirchenbauer, Micah Goldblum, Jonas Geiping, Tom Goldstein.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.03668v2)][[Github](https://github.com/YuxinWenRick/hard-prompts-made-easy)]

**EDICT: Exact Diffusion Inversion Via Coupled Transformations.**<br>
*Bram Wallace, Akash Gokul, Nikhil Naik.*<br>
arXiv 2022.11. [[PDF](http://arxiv.org/abs/2211.12446v2)]

**Null-text Inversion for Editing Real Images Using Guided Diffusion Models.**<br>
*Ron Mokady, Amir Hertz, Kfir Aberman, Yael Pritch, Daniel Cohen-Or.*<br>
arXiv 2022.11. [[PDF](http://arxiv.org/abs/2211.09794v1)]

**Direct Inversion: Optimization-Free Text-Driven Real Image Editing with Diffusion Models.**<br>
*Adham Elarabawy, Harish Kamath, Samuel Denton.*<br>
arXiv 2022.11. [[PDF](http://arxiv.org/abs/2211.07825v1)]

## 🎨 Editing
**Adaptive Nonlinear Latent Transformation for Conditional Face Editing.**<br>
*Zhizhong Huang, Siteng Ma, Junping Zhang, Hongming Shan.*<br>
ICCV 2023. [[PDF](http://arxiv.org/abs/2307.07790v1)]

**DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models.**<br>
*Chong Mou, Xintao Wang, Jiechong Song, Ying Shan, Jian Zhang.*<br>
arXiv 2023.07. [[PDF](http://arxiv.org/abs/2307.02421v1)]

**LEDITS: Real Image Editing with DDPM Inversion and Semantic Guidance.**<br>
*Linoy Tsaban, Apolinário Passos.*<br>
arXiv 2023.07. [[PDF](http://arxiv.org/abs/2307.00522v1)]

**User-friendly Image Editing with Minimal Text Input: Leveraging Captioning and Injection Techniques.**<br>
*Sunwoo Kim, Wooseok Jang, Hyunsu Kim, Junho Kim, Yunjey Choi, Seungryong Kim, Gayeong Lee.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.02717v1)]

**Improving Diffusion-based Image Translation Using Asymmetric Gradient Guidance.**<br>
*Gihyun Kwon, Jong Chul Ye.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.04396v1)]

**PFB-Diff: Progressive Feature Blending Diffusion for Text-driven Image Editing.**<br>
*Wenjing Huang, Shikui Tu, Lei Xu.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.16894v1)]

**Continuous Layout Editing of Single Images with Diffusion Models.**<br>
*Zhiyuan Zhang, Zhitong Huang, Jing Liao.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.13078v1)]

**Paste, Inpaint and Harmonize Via Denoising: Subject-Driven Image Editing with Pre-Trained Diffusion Model.**<br>
*Xin Zhang, Jiaxian Guo, Paul Yoo, Yutaka Matsuo, Yusuke Iwasawa.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.07596v1)]

**Conditional Score Guidance for Text-Driven Image-to-Image Translation.**<br>
*Hyunsoo Lee, Minsoo Kang, Bohyung Han.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.18007v1)]

**InstructEdit: Improving Automatic Masks for Diffusion-based Image Editing With User Instructions.**<br>
*Qian Wang, Biao Zhang, Michael Birsak, Peter Wonka.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.18047v1)][[Github](https://qianwangx.github.io/InstructEdit/)]

**FISEdit: Accelerating Text-to-image Editing Via Cache-enabled Sparse Diffusion Inference.**<br>
*Zihao Yu, Haoyang Li, Fangcheng Fu, Xupeng Miao, Bin Cui.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.17423v1)]

**Towards Consistent Video Editing with Text-to-Image Diffusion Models.**<br>
*Zicheng Zhang, Bonan Li, Xuecheng Nie, Congying Han, Tiande Guo, Luoqi Liu.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.17431v1)]

**Text-to-image Editing by Image Information Removal.**<br>
*Zhongping Zhang, Jian Zheng, Jacob Zhiyuan Fang, Bryan A. Plummer.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.17489v1)]

**Negative-prompt Inversion: Fast Image Inversion for Editing with Text-guided Diffusion Models.**<br>
*Daiki Miyake, Akihiro Iohara, Yu Saito, Toshiyuki Tanaka.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.16807v1)]

**Custom-Edit: Text-Guided Image Editing with Customized Diffusion Models.**<br>
*Jooyoung Choi, Yunjey Choi, Yunji Kim, Junho Kim, Sungroh Yoon.*<br>
CVPR 2023. [[PDF](http://arxiv.org/abs/2305.15779v1)]

**ChatFace: Chat-Guided Real Face Editing Via Diffusion Latent Space Manipulation.**<br>
*Dongxu Yue, Qin Guo, Munan Ning, Jiaxi Cui, Yuesheng Zhu, Li Yuan.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.14742v2)]

**BLIP-Diffusion: Pre-trained Subject Representation for Controllable Text-to-Image Generation and Editing.**<br>
*Dongxu Li, Junnan Li, Steven C. H. Hoi.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.14720v2)]

**DiffUTE: Universal Text Editing Diffusion Model.**<br>
*Haoxing Chen, Zhuoer Xu, Zhangxuan Gu, Jun Lan, Xing Zheng, Yaohui Li, Changhua Meng, Huijia Zhu, Weiqiang Wang.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.10825v2)]

**Guided Image Synthesis Via Initial Image Editing in Diffusion Model.**<br>
*Jiafeng Mao, Xueting Wang, Kiyoharu Aizawa.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.03382v1)]

**Collaborative Diffusion for Multi-Modal Face Generation and Editing.**<br>
*Ziqi Huang, Kelvin C. K. Chan, Yuming Jiang, Ziwei Liu.*<br>
CVPR 2023. [[PDF](http://arxiv.org/abs/2304.10530v1)][[Github](https://ziqihuangg.github.io/projects/collaborative-diffusion.html)][[Github](https://github.com/ziqihuangg/Collaborative-Diffusion)]

**Text-guided Image-and-Shape Editing and Generation: A Short Survey.**<br>
*Cheng-Kang Ted Chao, Yotam Gingold.*<br>
arXiv 2023.04. [[PDF](http://arxiv.org/abs/2304.09244v1)]

**Video-P2P: Video Editing with Cross-attention Control.**<br>
*Shaoteng Liu, Yuechen Zhang, Wenbo Li, Zhe Lin, Jiaya Jia.*<br>
arXiv 2023.03. [[PDF](http://arxiv.org/abs/2303.04761v1)][[Github](https://video-p2p.github.io/)]

**Zero-Shot Video Editing Using Off-The-Shelf Image Diffusion Models.**<br>
*Wen Wang, Kangyang Xie, Zide Liu, Hao Chen, Yue Cao, Xinlong Wang, Chunhua Shen.*<br>
arXiv 2023.03. [[PDF](http://arxiv.org/abs/2303.17599v2)]

**Controlled and Conditional Text to Image Generation with Diffusion Prior.**<br>
*Pranav Aggarwal, Hareesh Ravi, Naveen Marri, Sachin Kelkar, Fengbin Chen, Vinh Khuc, Midhun Harikumar, Ritiz Tambi, Sudharshan Reddy Kakumanu, Purvak Lapsiya, Alvin Ghouas, Sarah Saber, Malavika Ramprasad, Baldo Faieta, Ajinkya Kale.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.11710v1)]

**Towards Enhanced Controllability of Diffusion Models.**<br>
*Wonwoong Cho, Hareesh Ravi, Midhun Harikumar, Vinh Khuc, Krishna Kumar Singh, Jingwan Lu, David I. Inouye, Ajinkya Kale.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.14368v2)]

**Region-Aware Diffusion for Zero-shot Text-driven Image Editing.**<br>
*Nisha Huang, Fan Tang, Weiming Dong, Tong-Yee Lee, Changsheng Xu.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.11797v1)]

**Composer: Creative and Controllable Image Synthesis with Composable Conditions.**<br>
*Lianghua Huang, Di Chen, Yu Liu, Yujun Shen, Deli Zhao, Jingren Zhou.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.09778v2)][[Github](https://damo-vilab.github.io/composer-page/)]

**PRedItOR: Text Guided Image Editing with Diffusion Prior.**<br>
*Hareesh Ravi, Sachin Kelkar, Midhun Harikumar, Ajinkya Kale.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.07979v2)]

**SEGA: Instructing Diffusion Using Semantic Dimensions.**<br>
*Manuel Brack, Felix Friedrich, Dominik Hintersdorf, Lukas Struppek, Patrick Schramowski, Kristian Kersting.*<br>
arXiv 2023.01. [[PDF](http://arxiv.org/abs/2301.12247v1)]

**Uncovering The Disentanglement Capability in Text-to-Image Diffusion Models.**<br>
*Qiucheng Wu, Yujian Liu, Handong Zhao, Ajinkya Kale, Trung Bui, Tong Yu, Zhe Lin, Yang Zhang, Shiyu Chang.*<br>
arXiv 2022.12. [[PDF](http://arxiv.org/abs/2212.08698v1)]

**SINE: SINgle Image Editing with Text-to-Image Diffusion Models.**<br>
*Zhixing Zhang, Ligong Han, Arnab Ghosh, Dimitris Metaxas, Jian Ren.*<br>
arXiv 2022.12. [[PDF](http://arxiv.org/abs/2212.04489v1)][[Github](https://zhang-zx.github.io/SINE/)]

**SmartBrush: Text and Shape Guided Object Inpainting with Diffusion Model.**<br>
*Shaoan Xie, Zhifei Zhang, Zhe Lin, Tobias Hinz, Kun Zhang.*<br>
arXiv 2022.12. [[PDF](http://arxiv.org/abs/2212.05034v1)]

**InstructPix2Pix: Learning to Follow Image Editing Instructions.**<br>
*Tim Brooks, Aleksander Holynski, Alexei A. Efros.*<br>
arXiv 2022.11. [[PDF](http://arxiv.org/abs/2211.09800v2)][[Link](https://www.timothybrooks.com/instruct-pix2pix)]

**EDICT: Exact Diffusion Inversion Via Coupled Transformations.**<br>
*Bram Wallace, Akash Gokul, Nikhil Naik.*<br>
arXiv 2022.11. [[PDF](http://arxiv.org/abs/2211.12446v2)]

**Paint by Example: Exemplar-based Image Editing with Diffusion Models.**<br>
*Binxin Yang, Shuyang Gu, Bo Zhang, Ting Zhang, Xuejin Chen, Xiaoyan Sun, Dong Chen, Fang Wen.*<br>
arXiv 2022.11. [[PDF](http://arxiv.org/abs/2211.13227v1)][[Github](https://github.com/Fantasy-Studio/Paint-by-Example)]

**Diffusion Models Already Have A Semantic Latent Space.**<br>
*Mingi Kwon, Jaeseok Jeong, Youngjung Uh.*<br>
ICLR2023. [[PDF](http://arxiv.org/abs/2210.10960v2)]

**Leveraging Off-the-shelf Diffusion Model for Multi-attribute Fashion Image Manipulation.**<br>
*Chaerin Kong, DongHyeon Jeon, Ohjoon Kwon, Nojun Kwak.*<br>
arXiv 2022.10. [[PDF](http://arxiv.org/abs/2210.05872v1)]

**DiffEdit: Diffusion-based Semantic Image Editing with Mask Guidance.**<br>
*Guillaume Couairon, Jakob Verbeek, Holger Schwenk, Matthieu Cord.*<br>
arXiv 2022.10. [[PDF](http://arxiv.org/abs/2210.11427v1)]

**Unifying Diffusion Models' Latent Space, with Applications to CycleDiffusion and Guidance.**<br>
*Chen Henry Wu, Fernando De la Torre.*<br>
arXiv 2022.10. [[PDF](http://arxiv.org/abs/2210.05559v2)]

**UniTune: Text-Driven Image Editing by Fine Tuning A Diffusion Model on A Single Image.**<br>
*Dani Valevski, Matan Kalman, Eyal Molad, Eyal Segalis, Yossi Matias, Yaniv Leviathan.*<br>
SIGGRAPH 2023. [[PDF](http://arxiv.org/abs/2210.09477v4)]

**More Control for Free! Image Synthesis with Semantic Diffusion Guidance.**<br>
*Xihui Liu, Dong Huk Park, Samaneh Azadi, Gong Zhang, Arman Chopikyan, Yuxiao Hu, Humphrey Shi, Anna Rohrbach, Trevor Darrell.*<br>
arXiv 2021.12. [[PDF](http://arxiv.org/abs/2112.05744v4)][[Github](https://xh-liu.github.io/sdg/)]

**SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations.**<br>
*Chenlin Meng, Yutong He, Yang Song, Jiaming Song, Jiajun Wu, Jun-Yan Zhu, Stefano Ermon.*<br>
arXiv 2021.08. [[PDF](http://arxiv.org/abs/2108.01073v2)][[Github](https://sde-image-editing.github.io/)]

## 🚄 Parameter-Efficient Fine-Tuning
The NLP PEFT methods which have been proposed to diffusion models are marked by 📌, and the methods designed for diffusion are marked by 💎.

**Parameter-efficient Is Not Sufficient: Exploring Parameter, Memory, and Time Efficient Adapter Tuning for Dense Predictions.**<br>
*Dongshuo Yin, Xueting Han, Bin Li, Hao Feng, Jing Bai.*<br>
NeurIPS2023. [[PDF](http://arxiv.org/abs/2306.09729v1)]

**One-for-All: Generalized LoRA for Parameter-Efficient Fine-tuning.**<br>
*Arnav Chavan, Zhuang Liu, Deepak Gupta, Eric Xing, Zhiqiang Shen.*<br>
arXiv 2023.06. [[PDF](http://arxiv.org/abs/2306.07967v1)]

**Visual Tuning.**<br>
*Bruce X. B. Yu, Jianlong Chang, Haixin Wang, Lingbo Liu, Shijie Wang, Zhiyu Wang, Junfan Lin, Lingxi Xie, Haojie Li, Zhouchen Lin, Qi Tian, Chang Wen Chen.*<br>
arXiv 2023.05. [[PDF](http://arxiv.org/abs/2305.06061v1)]

**💎 A Closer Look at Parameter-Efficient Tuning in Diffusion Models.**<br>
*Chendong Xiang, Fan Bao, Chongxuan Li, Hang Su, Jun Zhu.*<br>
arXiv 2023.03. [[PDF](http://arxiv.org/abs/2303.18181v2)][[Github](https://github.com/Xiang-cd/unet-finetune)]

**Towards Efficient Visual Adaption Via Structural Re-parameterization.**<br>
*Gen Luo, Minglang Huang, Yiyi Zhou, Xiaoshuai Sun, Guannan Jiang, Zhiyu Wang, Rongrong Ji.*<br>
arXiv 2023.02. [[PDF](http://arxiv.org/abs/2302.08106v2)]

**📌 DyLoRA: Parameter Efficient Tuning of Pre-trained Models Using Dynamic Search-Free Low-Rank Adaptation.**<br>
*Mojtaba Valipour, Mehdi Rezagholizadeh, Ivan Kobyzev, Ali Ghodsi.*<br>
arXiv 2022.10. [[PDF](http://arxiv.org/abs/2210.07558v2)] [[Diffusion Impl.:KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS/tree/main)]

**📌 Few-Shot Parameter-Efficient Fine-Tuning Is Better and Cheaper Than In-Context Learning.**<br>
*Haokun Liu, Derek Tam, Mohammed Muqeeth, Jay Mohta, Tenghao Huang, Mohit Bansal, Colin Raffel.*<br>
arXiv 2022.05. [[PDF](http://arxiv.org/abs/2205.05638v2)] [[Diffusion Impl.:KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS/tree/main)]

**📌 FedPara: Low-Rank Hadamard Product for Communication-Efficient Federated Learning.**<br>
*Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh.*<br>
ICLR 2022. [[PDF](http://arxiv.org/abs/2108.06098v3)] [[Diffusion Impl.:KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS/tree/main)]

**📌 LoRA: Low-Rank Adaptation of Large Language Models.**<br>
*Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen.*<br>
arXiv 2021.06. [[PDF](http://arxiv.org/abs/2106.09685v2)]

**The Power of Scale for Parameter-Efficient Prompt Tuning.**<br>
*Brian Lester, Rami Al-Rfou, Noah Constant.*<br>
arXiv 2021.04. [[PDF](http://arxiv.org/abs/2104.08691v2)]

**Prefix-Tuning: Optimizing Continuous Prompts for Generation.**<br>
*Xiang Lisa Li, Percy Liang.*<br>
arXiv 2021.01. [[PDF](http://arxiv.org/abs/2101.00190v1)]

**Parameter-Efficient Transfer Learning for NLP.**<br>
*Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly.*<br>
arXiv 2019.02. [[PDF](http://arxiv.org/abs/1902.00751v2)]

**Parameter-Efficient Transfer Learning for NLP.**<br>
*Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly.*<br>
PMLR 2019. [[PDF](http://arxiv.org/abs/1902.00751v2)]
