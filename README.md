 <!-- # <p align=center>`awesome gan-inversion`</p> -->
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

<br />
<p align="center">
  <h1 align="center">Awesome Controllable T2I Diffusion Models</h1>
</p>
<br />

We are focusing on how to **Control** text-to-image diffusion models with **Novel Conditions**. 

The survey paper is coming soon (March).

<img src="assets/controllable_generation.png" alt="img" style="zoom: 33%;" />

## Citation
```text
@article{cao2023controllable,
  title={Controllable Generation with Text-to-Image Diffusion Models: A Survey},
  author={xx},
  journal={xx},
  year={2024}
}
```

## 🌈 Contents

- [Generation with Specific Condition](#Generation-with-Specific-Condition)
  - [Personalization](#Personalization)
    - [Subject-Driven Generation](#Subject-Driven-Generation)
    - [Person-Driven Generation](#Person-Driven-Generation)
    - [Style-Driven Generation](#Style-Driven-Generation)
    - [Interaction-Driven Generation](#Interaction-Driven-Generation)
    - [Image-Driven Generation](#Image-Driven-Generation)
    - [Distribution-Driven Generation](#Distribution-Driven-Generation)
  - [Spatial Control](#Spatial-Control)
  - [Advanced Text-Conditioned Generation](#Advanced-Text-Conditioned-Generation)
  - [In-Context Generation](#In-Context-Generation)
  - [Brain-Guided Generation](#Brain-Guided-Generation)
  - [Sound-Guided Generation](#Sound-Guided-Generation)
  - [Text Rendering](#Text-Rendering)
- [Generation with Multiple Conditions](#Generation-with-Multiple-Conditions)
  - [Joint Training](#Joint-Training)
  - [Continual Learning](#Continual-Learning)
  - [Weight Fusion](#Weight-Fusion)
  - [Attention-based Integration](#Attention-based-Integration)
  - [Guidance Composition](#Guidance-Composition)
- [Universal Controllable Generation](#Universal-Controllable-Generation)
  - [Universal Conditional Score Prediction](#Universal-Conditional-Score-Prediction)
  - [Universal Condition-Guided Score Estimation](#Universal-Condition-Guided-Score-Estimation)


## 🚀Generation with Specific Condition
### Personalization
#### Subject-Driven Generation
**An Image is Worth One Word- Personalizing  Text-to-Image Generation using Textual Inversion.**<br>
*Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
ICLR 2023. [[PDF](https://arxiv.org/abs/2208.01618)]

**DreamBooth- Fine Tuning Text-to-Image Diffusion Models  for Subject-Driven Generation.**<br>
*Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, Kfir Aberman.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2208.12242)]

**Re-Imagen: Retrieval-Augmented Text-to-Image Generator.**<br>
*Wenhu Chen, Hexiang Hu, Chitwan Saharia, William W. Cohen.*<br>
ICLR 2023. [[PDF](https://arxiv.org/abs/2209.14491)]

**DreamArtist: Towards Controllable One-Shot Text-to-Image Generation via Positive-Negative Prompt-Tuning.**<br>
*Ziyi Dong, Pengxu Wei, Liang Lin.*<br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2211.11337)]

**Multi-Concept Customization of Text-to-Image Diffusion.**<br>
*Nupur Kumari, Bingliang Zhang, Richard Zhang, Eli Shechtman, Jun-Yan Zhu.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2212.04488)]

**Is This Loss Informative? Faster Text-to-Image Customization by Tracking Objective Dynamics.**<br>
*Anton Voronov, Mikhail Khoroshikh, Artem Babenko, Max Ryabinin.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2302.04841)]

**Designing an Encoder for Fast Personalization of Text-to-Image  Models.**<br>
*Rinon Gal, Moab Arar, Yuval Atzmon, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2302.12228)]

**ELITE- Encoding Visual Concepts into Textual Embeddings  for Customized Text-to-Image Generation.**<br>
*Yuxiang Wei, Yabo Zhang, Zhilong Ji, Jinfeng Bai, Lei Zhang, Wangmeng Zuo.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2302.13848)]

**Unified Multi-Modal Latent Diffusion for
Joint Subject and Text Conditional Image Generation.**<br>
*Yiyang Ma, Huan Yang, Wenjing Wang, Jianlong Fu, Jiaying Liu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.09319)]

**P+- Extended Textual Conditioning in Text-to-Image Generation.**<br>
*Andrey Voynov, Qinghao Chu, Daniel Cohen-Or, Kfir Aberman.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.09522)]

**SVDiff- Compact Parameter Space for Diffusion Fine-Tuning.**<br>
*Ligong Han, Yinxiao Li, Han Zhang, Peyman Milanfar, Dimitris Metaxas, Feng Yang.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2303.11305)]

**A Closer Look at Parameter-Efficient Tuning in Diffusion Models .**<br>
*Chendong Xiang, Fan Bao, Chongxuan Li, Hang Su, Jun Zhu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.18181)]

**Subject-driven Text-to-Image Generation via  Apprenticeship Learning.**<br>
*Wenhu Chen, Hexiang Hu, Yandong Li, Nataniel Ruiz, Xuhui Jia, Ming-Wei Chang, William W. Cohen.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2304.00186)]

**Taming Encoder for Zero Fine-tuning Image Customization  with Text-to-Image Diffusion Models.**<br>
*Xuhui Jia, Yang Zhao, Kelvin C. K. Chan, Yandong Li, Han Zhang, Boqing Gong, Tingbo Hou, Huisheng Wang, Yu-Chuan Su.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2304.02642)]

**InstantBooth- Personalized Text-to-Image Generation without Test-Time  Finetuning.**<br>
*Jing Shi, Wei Xiong, Zhe Lin, Hyun Joon Jung.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2304.03411)]

**Controllable Textual Inversion for Personalized Text-to-Image Generation.**<br>
*Jianan Yang, Haobo Wang, Yanming Zhang, Ruixuan Xiao, Sai Wu, Gang Chen, Junbo Zhao.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2304.05265)]

**Gradient-Free Textual Inversion.**<br>
*Zhengcong Fei, Mingyuan Fan, Junshi Huang.*<br>
ACM MM 2023. [[PDF](https://arxiv.org/abs/2304.05818)]

**Key-Locked Rank One Editing for Text-to-Image Personalization.**<br>
*Yoad Tewel, Rinon Gal, Gal Chechik, Yuval Atzmon.*<br>
SIGGRAPH 2023. [[PDF](https://arxiv.org/abs/2305.01644)]

**DisenBooth- Disentangled Parameter-Efficient Tuning for Subject-Driven  Text-to-Image Generation.**<br>
*Hong Chen, Yipeng Zhang, Simin Wu, Xin Wang, Xuguang Duan, Yuwei Zhou, Wenwu Zhu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.03374)]

**BLIP-Diffusion- Pre-trained Subject Representation for  Controllable Text-to-Image Generation and Editing.**<br>
*Dongxu Li, Junnan Li, Steven C. H. Hoi.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2305.14720)]

**ProSpect- Prompt Spectrum for Attribute-Aware Personalization of  Diffusion Models.**<br>
*Yuxin Zhang, Weiming Dong, Fan Tang, Nisha Huang, Haibin Huang, Chongyang Ma, Tong-Yee Lee, Oliver Deussen, Changsheng Xu.*<br>
TOG 2023. [[PDF](https://arxiv.org/abs/2305.16225)]

**Break-A-Scene: Extracting Multiple Concepts from a Single Image.**<br>
*Omri Avrahami, Kfir Aberman, Ohad Fried, Daniel Cohen-Or, Dani Lischinski.*<br>
SIGGRAPH ASIA 2023. [[PDF](https://arxiv.org/abs/2305.16311)]

**COMCAT: Towards Efficient Compression and Customization of
Attention-Based Vision Models.**<br>
*Jinqi Xiao, Miao Yin, Yu Gong, Xiao Zang, Jian Ren, Bo Yuan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.17235)]

**Controlling Text-to-Image Diffusion by Orthogonal Finetuning .**<br>
*Zeju Qiu, Weiyang Liu, Haiwen Feng, Yuxuan Xue, Yao Feng, Zhen Liu, Dan Zhang, Adrian Weller, Bernhard Schölkopf.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2306.07280)]

**Generate Anything Anywhere in Any Scene.**<br>
*Yuheng Li, Haotian Liu, Yangming Wen, Yong Jae Lee.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.17154)]

**Domain-Agnostic Tuning-Encoder for Fast Personalization of  Text-To-Image Models .**<br>
*Moab Arar, Rinon Gal, Yuval Atzmon, Gal Chechik, Daniel Cohen-Or, Ariel Shamir, Amit H. Bermano.*<br>
SIGGRAPH ASIA 2023. [[PDF](https://arxiv.org/abs/2307.06925)]

**Subject-Diffusion- Open Domain Personalized  Text-to-Image Generation without Test-time  Fine-tuning.**<br>
*Jian Ma, Junhao Liang, Chen Chen, Haonan Lu.*<br>
ICLR2024 (3566). [[PDF](https://arxiv.org/abs/2307.11410)]

**Navigating Text-To-Image Customization: From LyCORIS Fine-Tuning to Model Evaluation.**<br>
*Shin-Ying Yeh, Yu-Guan Hsieh, Zhidong Gao, Bernard B W Yang, Giyeong Oh, Yanmin Gong.*<br>
ICLR 2024. [[PDF](https://arxiv.org/abs/2309.14859)]

**Kosmos-G: Generating Images in Context with Multimodal Large Language Models.**<br>
*Xichen Pan, Li Dong, Shaohan Huang, Zhiliang Peng, Wenhu Chen, Furu Wei.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.02992)]

**AN IMAGE IS WORTH MULTIPLE WORDS : LEARNING OBJECT LEVEL CONCEPTS USING MULTI-CONCEPT PROMPT LEARNING.**<br>
*Chen Jin, Ryutaro Tanno, Amrutha Saseendran, Tom Diethe, Philip Teare.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.12274)]

**A Data Perspective on Enhanced Identity Preservation for Diffusion  Personalization.**<br>
*Xingzhe He, Zhiwen Cao, Nicholas Kolkin, Lantao Yu, Helge Rhodin, Ratheesh Kalarot.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.04315)]

**DIFFNAT- Improving Diffusion Image Quality Using Natural Image  Statistics.**<br>
*Aniket Roy, Maiterya Suin, Anshul Shah, Ketul Shah, Jiang Liu, Rama Chellappa.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.09753)]

**An Image is Worth Multiple Words- Multi-attribute Inversion for Constrained Text-to-Image Synthesis.**<br>
*Aishwarya Agarwal, Srikrishna Karanam, Tripti Shukla, Balaji Vasan Srinivasan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.11919)]

**Lego- Learning to Disentangle and Invert Concepts Beyond Object Appearance in Text-to-Image Diffusion Models.**<br>
*Saman Motamed, Danda Pani Paudel, Luc Van Gool.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.13833)]

**CatVersion- Concatenating Embeddings for Diffusion-Based Text-to-Image Personalization.**<br>
*Ruoyu Zhao, Mingrui Zhu, Shiyin Dong, Nannan Wang, Xinbo Gao.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.14631)]

**CLiC: Concept Learning in Context.**<br>
*Mehdi Safaee, Aryan Mikaeili, Or Patashnik, Daniel Cohen-Or, Ali Mahdavi-Amiri.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.17083)]

**VideoAssembler: Identity-Consistent Video Generation with Reference Entities using Diffusion Model.**<br>
*Haoyu Zhao, Tianyi Lu, Jiaxi Gu, Xing Zhang, Zuxuan Wu, Hang Xu, Yu-Gang Jiang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.17338)]

**HiFi Tuner: High-Fidelity Subject-Driven Fine-Tuning for Diffusion Models.**<br>
*Zhonghao Wang, Wei Wei, Yang Zhao, Zhisheng Xiao, Mark Hasegawa-Johnson, Humphrey Shi, Tingbo Hou.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.00079)]

**VideoBooth: Diffusion-based Video Generation with Image Prompts.**<br>
*Yuming Jiang, Tianxing Wu, Shuai Yang, Chenyang Si, Dahua Lin, Yu Qiao, Chen Change Loy, Ziwei Liu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.00777)]

**Customization Assistant for Text-to-image Generation.**<br>
*Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, Tong Sun.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.03045)]

**Decoupled Textual Embeddings for Customized Image Generation.**<br>
*Yufei Cai, Yuxiang Wei, Zhilong Ji, Jinfeng Bai, Hu Han, Wangmeng Zuo.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.11826)]

**DreamTuner: Single Image is Enough for Subject-Driven Generation.**<br>
*Miao Hua, Jiawei Liu, Fei Ding, Wei Liu, Jie Wu, Qian He.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.13691)]


#### Person-Driven Generation
**FastComposer: Tuning-Free Multi-Subject Image Generation with Localized Attention.**<br>
*Guangxuan Xiao, Tianwei Yin, William T. Freeman, Frédo Durand, Song Han.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.10431)]

**Conditioning Diffusion Models via Attributes and Semantic Masks for Face Generation.**<br>
*Nico Giambi, Giuseppe Lisanti.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.00914)]

**Face0- Instantaneously Conditioning a Text-to-Image Model on a Face.**<br>
*Dani Valevski, Danny Wasserman, Yossi Matias, Yaniv Leviathan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.06638)]

**DreamIdentity- Improved Editability for Efficient  Face-identity Preserved Image Generation .**<br>
*Zhuowei Chen, Shancheng Fang, Wei Liu, Qian He, Mengqi Huang, Yongdong Zhang, Zhendong Mao.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2307.00300)]

**HyperDreamBooth- HyperNetworks for Fast  Personalization of Text-to-Image Models .**<br>
*Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Wei Wei, Tingbo Hou, Yael Pritch, Neal Wadhwa, Michael Rubinstein, Kfir Aberman.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2307.06949)]

**PhotoVerse- Tuning-Free Image Customization with Text-to-Image Diffusion Models.**<br>
*Li Chen, Mengyi Zhao, Yiheng Liu, Mingxu Ding, Yangyang Song, Shizun Wang, Xu Wang, Hao Yang, Jing Liu, Kang Du, Min Zheng.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.05793)]

**MagiCapture- High-Resolution Multi-Concept Portrait Customization.**<br>
*Junha Hyung, Jaeyo Shin, Jaegul Choo.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.06895)]

**High-fidelity Person-centric Subject-to-Image Synthesis.**<br>
*Yibin Wang, Weizhong Zhang, Jianwei Zheng, Cheng Jin.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.10329)]

**When StyleGAN Meets Stable Diffusion- a W + Adapter for Personalized Image Generation.**<br>
*Xiaoming Li, Xinyu Hou, Chen Change Loy.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.17461)]

**Retrieving Conditions from Reference Images for Diffusion Models.**<br>
*Haoran Tang, Xin Zhou, Jieren Deng, Zhihong Pan, Hao Tian, Pratik Chaudhari.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.02521)]

**FaceStudio: Put Your Face Everywhere in Seconds.**<br>
*Yuxuan Yan, Chi Zhang, Rui Wang, Yichao Zhou, Gege Zhang, Pei Cheng, Gang Yu, Bin Fu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.02663)]

**ViscoNet: Bridging and Harmonizing Visual and Textual Conditioning for ControlNet.**<br>
*Soon Yau Cheong, Armin Mustafa, Andrew Gilbert.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.03154)]

**DemoCaricature: Democratising Caricature Generation with a Rough Sketch.**<br>
*Dar-Yen Chen, Subhadeep Koley, Aneeshan Sain, Pinaki Nath Chowdhury, Tao Xiang, Ayan Kumar Bhunia, Yi-Zhe Song.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.04364)]

**PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding.**<br>
*Zhen Li, Mingdeng Cao, Xintao Wang, Zhongang Qi, Ming-Ming Cheng, Ying Shan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.04461)]

**Stellar: Systematic Evaluation of Human-Centric Personalized Text-to-Image Methods.**<br>
*Panos Achlioptas, Alexandros Benetatos, Iordanis Fostiropoulos, Dimitris Skourtis.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.06116)]

**PortraitBooth: A Versatile Portrait Model for Fast Identity-preserved Personalization.**<br>
*Xu Peng, Junwei Zhu, Boyuan Jiang, Ying Tai, Donghao Luo, Jiangning Zhang, Wei Lin, Taisong Jin, Chengjie Wang, Rongrong Ji.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.06354)]


#### Style-Driven Generation
**StyleDrop: Text-to-Image Generation in Any Style.**<br>
*Kihyuk Sohn, Nataniel Ruiz, Kimin Lee, Daniel Castro Chin, Irina Blok, Huiwen Chang, Jarred Barber, Lu Jiang, Glenn Entis, Yuanzhen Li, Yuan Hao, Irfan Essa, Michael Rubinstein, Dilip Krishnan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.00983)]

**StyleCrafter- Enhancing Stylized Text-to-Video Generation with Style Adapter.**<br>
*Gongye Liu, Menghan Xia, Yong Zhang, Haoxin Chen, Jinbo Xing, Xintao Wang, Yujiu Yang, Ying Shan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.00330)]

**ArtAdapter: Text-to-Image Style Transfer using Multi-Level Style Encoder and Explicit Adaptation.**<br>
*Dar-Yen Chen, Hamish Tennent, Ching-Wen Hsu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.02109)]

**Style Aligned Image Generation via Shared Attention.**<br>
*Amir Hertz, Andrey Voynov, Shlomi Fruchter, Daniel Cohen-Or.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.02133)]

**Towards Accurate Guided Diffusion Sampling through Symplectic Adjoint Method.**<br>
*Jiachun Pan, Hanshu Yan, Jun Hao Liew, Jiashi Feng, Vincent Y. F. Tan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.12030)]


#### Interaction-Driven Generation 
**ReVersion- Diffusion-Based Relation Inversion from Images .**<br>
*Ziqi Huang, Tianxing Wu, Yuming Jiang, Kelvin C. K. Chan, Ziwei Liu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.13495)]

**AnimateDiff- Animate Your Personalized Text-to-Image Diffusion Models  without Specific Tuning.**<br>
*Yuwei Guo, Ceyuan Yang, Anyi Rao, Zhengyang Liang, Yaohui Wang, Yu Qiao, Maneesh Agrawala, Dahua Lin, Bo Dai.*<br>
ICLR2024 (6688). [[PDF](https://arxiv.org/abs/2307.04725)]

**MotionDirector- Motion Customization of Text-to-Video Diffusion Models.**<br>
*Rui Zhao, Yuchao Gu, Jay Zhangjie Wu, David Junhao Zhang, Jiawei Liu, Weijia Wu, Jussi Keppo, Mike Zheng Shou.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.08465)]

**LAMP: Learn A Motion Pattern for Few-Shot-Based Video Generation.**<br>
*Ruiqi Wu, Liangyu Chen, Tong Yang, Chunle Guo, Chongyi Li, Xiangyu Zhang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.10769)]

**SAVE: Protagonist Diversification with Structure Agnostic Video Editing.**<br>
*Yeji Song, Wonsik Shin, Junsoo Lee, Jeesoo Kim, Nojun Kwak.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.02503)]

**Customizing Motion in Text-to-Video Diffusion Models.**<br>
*Joanna Materzynska, Josef Sivic, Eli Shechtman, Antonio Torralba, Richard Zhang, Bryan Russell.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.04966)]

**DreaMoving: A Human Dance Video Generation Framework based on Diffusion Models.**<br>
*Mengyang Feng, Jinlin Liu, Kai Yu, Yuan Yao, Zheng Hui, Xiefan Guo, Xianhui Lin, Haolan Xue, Chen Shi, Xiaowen Li, Aojie Li, Xiaoyang Kang, Biwen Lei, Miaomiao Cui, Peiran Ren, Xuansong Xie.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.05107)]

**MotionCrafter: One-Shot Motion Customization of Diffusion Models.**<br>
*Yuxin Zhang, Fan Tang, Nisha Huang, Haibin Huang, Chongyang Ma, Weiming Dong, Changsheng Xu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.05288)]

**InteractDiffusion: Interaction Control in Text-to-Image Diffusion Models.**<br>
*Jiun Tian Hoe, Xudong Jiang, Chee Seng Chan, Yap-Peng Tan, Weipeng Hu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.05849)]


#### Image-Driven Generation
**Hierarchical Text-Conditional Image Generation with CLIP Latents.**<br>
*Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, Mark Chen.*<br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2204.06125)]

**Versatile Diffusion: Text, Images and Variations All in One Diffusion Model.**<br>
*Xingqian Xu, Zhangyang Wang, Eric Zhang, Kai Wang, Humphrey Shi.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2211.08332)]

**Prompt-Free Diffusion: Taking “Text” out of Text-to-Image Diffusion Models.**<br>
*Xingqian Xu, Jiayi Guo, Zhangyang Wang, Gao Huang, Irfan Essa, Humphrey Shi.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.16223)]

**Uni-ControlNet: All-in-One Control to Text-to-Image Diffusion Models.**<br>
*Shihao Zhao, Dongdong Chen, Yen-Chun Chen, Jianmin Bao, Shaozhe Hao, Lu Yuan, Kwan-Yee K. Wong.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2305.16322)]

**IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models.**<br>
*Hu Ye, Jun Zhang, Sibo Liu, Xiao Han, Wei Yang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.06721)]

**ViscoNet: Bridging and Harmonizing Visual and Textual Conditioning for ControlNet.**<br>
*Soon Yau Cheong, Armin Mustafa, Andrew Gilbert.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.03154)]

**Context Diffusion: In-Context Aware Image Generation.**<br>
*Ivona Najdenkoska, Animesh Sinha, Abhimanyu Dubey, Dhruv Mahajan, Vignesh Ramanathan, Filip Radenovic.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.03584)]

**FreeControl: Training-Free Spatial Control of Any Text-to-Image Diffusion Model with Any Condition.**<br>
*Sicheng Mo, Fangzhou Mu, Kuan Heng Lin, Yanli Liu, Bochen Guan, Yin Li, Bolei Zhou.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.07536)]


#### Distribution-Driven Generation
**Concept-centric Personalization with Large-scale Diffusion Priors.**<br>
*Pu Cao, Lu Yang, Feng Zhou, Tianrui Huang, Qing Song.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.08195)]

**DreamDistribution: Prompt Distribution Learning for Text-to-Image Diffusion Models.**<br>
*Brian Nlong Zhao, Yuhang Xiao, Jiashu Xu, Xinyang Jiang, Yifan Yang, Dongsheng Li, Laurent Itti, Vibhav Vineet, Yunhao Ge.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.14216)]


### Spatial Control
**eDiff-I: Text-to-Image Diffusion Models with an Ensemble of Expert Denoisers.**<br>
*Yogesh Balaji, Seungjun Nah, Xun Huang, Arash Vahdat, Jiaming Song, Qinsheng Zhang, Karsten Kreis, Miika Aittala, Timo Aila, Samuli Laine, Bryan Catanzaro, Tero Karras, Ming-Yu Liu.*<br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2211.01324)]

**Sketch-Guided Text-to-Image Diffusion Models.**<br>
*Andrey Voynov, Kfir Aberman, Daniel Cohen-Or.*<br>
SIGGRAPH 2023. [[PDF](https://arxiv.org/abs/2211.13752)]

**SpaText: Spatio-Textual Representation for Controllable Image Generation.**<br>
*Omri Avrahami, Thomas Hayes, Oran Gafni, Sonal Gupta, Yaniv Taigman, Devi Parikh, Dani Lischinski, Ohad Fried, Xi Yin.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.14305)]

**GLIGEN: Open-Set Grounded Text-to-Image Generation.**<br>
*Yuheng Li, Haotian Liu, Qingyang Wu, Fangzhou Mu, Jianwei Yang, Jianfeng Gao, Chunyuan Li, Yong Jae Lee.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2301.07093)]

**Universal Guidance for Diffusion Models.**<br>
*Arpit Bansal, Hong-Min Chu, Avi Schwarzschild, Soumyadip Sengupta, Micah Goldblum, Jonas Geiping, Tom Goldstein.*<br>
CVPRW 2023. [[PDF](https://arxiv.org/abs/2302.07121)]

**LayoutDiffuse: Adapting Foundational Diffusion Models for Layout-to-Image Generation.**<br>
*Jiaxin Cheng, Xiao Liang, Xingjian Shi, Tong He, Tianjun Xiao, Mu Li.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2302.08908)]

**Modulating Pretrained Diffusion Models for Multimodal Image Synthesis.**<br>
*Cusuh Ham, James Hays, Jingwan Lu, Krishna Kumar Singh, Zhifei Zhang, Tobias Hinz.*<br>
SIGGRAPH 2023. [[PDF](https://arxiv.org/abs/2302.12764)]

**FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model.**<br>
*Jiwen Yu, Yinhuai Wang, Chen Zhao, Bernard Ghanem, Jian Zhang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.09833)]

**Freestyle Layout-to-Image Synthesis.**<br>
*Han Xue, Zhiwu Huang, Qianru Sun, Li Song, Wenjun Zhang.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2303.14412)]

**LayoutDiffusion: Controllable Diffusion Model for
Layout-to-image Generation.**<br>
*Guangcong Zheng, Xianpan Zhou, Xuewei Li, Zhongang Qi, Ying Shan, Xi Li.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2303.17189)]

**HumanSD: A Native Skeleton-Guided Diffusion Model for Human Image Generation.**<br>
*Xuan Ju, Ailing Zeng, Chenchen Zhao, Jianan Wang, Lei Zhang, Qiang Xu.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2304.04269)]

**Late-Constraint Diffusion Guidance for Controllable Image Synthesis.**<br>
*Chang Liu, Dong Liu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.11520)]

**Conditioning Diffusion Models via Attributes and Semantic Masks for Face Generation.**<br>
*Nico Giambi, Giuseppe Lisanti.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.00914)]

**GeoDiffusion: Text-Prompted Geometric Control for Object Detection Data Generation.**<br>
*Kai Chen, Enze Xie, Zhe Chen, Yibo Wang, Lanqing Hong, Zhenguo Li, Dit-Yan Yeung.*<br>
ICLR 2024. [[PDF](https://arxiv.org/abs/2306.04607)]

**Grounded Text-to-Image Synthesis with Attention Refocusing.**<br>
*Quynh Phung, Songwei Ge, Jia-Bin Huang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.05427)]

**Zero-shot spatial layout conditioning for text-to-image diffusion models.**<br>
*Guillaume Couairon, Marlène Careil, Matthieu Cord, Stéphane Lathuilière, Jakob Verbeek.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2306.13754)]

**Localized Text-to-Image Generation For Free via Cross Attention Control.**<br>
*Yutong He, Ruslan Salakhutdinov, J. Zico Kolter.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.14636)]

**SSMG: Spatial-Semantic Map Guided Diffusion Model for Free-form Layout-to-Image Generation.**<br>
*Chengyou Jia, Minnan Luo, Zhuohang Dang, Guang Dai, Xiaojun Chang, Mengmeng Wang, Jingdong Wang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.10156)]

**Dense Text-to-Image Generation with Attention Modulation.**<br>
*Yunji Kim, Jiyoung Lee, Jin-Hwa Kim, Jung-Woo Ha, Jun-Yan Zhu.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2308.12964)]

**JointNet: Extending Text-to-Image Diffusion for Dense Distribution Modeling.**<br>
*Jingyang Zhang, Shiwei Li, Yuanxun Lu, Tian Fang, David McKinnon, Yanghai Tsin, Long Quan, Yao Yao.*<br>
ICLR 2024. [[PDF](https://arxiv.org/abs/2310.06347)]

**HyperHuman- Hyper-Realistic Human Generation with Latent Structural  Diffusion.**<br>
*Xian Liu, Jian Ren, Aliaksandr Siarohin, Ivan Skorokhodov, Yanyu Li, Dahua Lin, Xihui Liu, Ziwei Liu, Sergey Tulyakov.*<br>
ICLR 2024. [[PDF](https://arxiv.org/abs/2310.08579)]

**R&B: REGION AND BOUNDARY AWARE ZERO-SHOT
GROUNDED TEXT-TO-IMAGE GENERATION.**<br>
*Jiayu Xiao, Henglei Lv, Liang Li, Shuhui Wang, Qingming Huang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.08872)]

**Enhancing Object Coherence in Layout-to-Image Synthesis.**<br>
*Yibin Wang, Weizhong Zhang, Jianwei Zheng, Cheng Jin.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.10522)]

**An Image is Worth Multiple Words- Multi-attribute Inversion for Constrained Text-to-Image Synthesis.**<br>
*Aishwarya Agarwal, Srikrishna Karanam, Tripti Shukla, Balaji Vasan Srinivasan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.11919)]

**LoCo: Locally Constrained Training-Free Layout-to-Image Synthesis.**<br>
*Peiang Zhao, Han Li, Ruiyang Jin, S. Kevin Zhou.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.12342)]

**AnyLens: A Generative Diffusion Model with Any Rendering Lens.**<br>
*Andrey Voynov, Amir Hertz, Moab Arar, Shlomi Fruchter, Daniel Cohen-Or.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.17609)]

**Layered Rendering Diffusion Model for Zero-Shot Guided Image Synthesis.**<br>
*Zipeng Qi, Guoxi Huang, Zebin Huang, Qin Guo, Jinwen Chen, Junyu Han, Jian Wang, Gang Zhang, Lufei Liu, Errui Ding, Jingdong Wang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.18435)]

**LOOSE CONTROL: Lifting ControlNet for Generalized Depth Conditioning.**<br>
*Shariq Farooq Bhat, Niloy J. Mitra, Peter Wonka.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.03079)]

**DemoCaricature: Democratising Caricature Generation with a Rough Sketch.**<br>
*Dar-Yen Chen, Subhadeep Koley, Aneeshan Sain, Pinaki Nath Chowdhury, Tao Xiang, Ayan Kumar Bhunia, Yi-Zhe Song.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.04364)]

**InteractDiffusion: Interaction Control in Text-to-Image Diffusion Models.**<br>
*Jiun Tian Hoe, Xudong Jiang, Chee Seng Chan, Yap-Peng Tan, Weipeng Hu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.05849)]

**FreeControl: Training-Free Spatial Control of Any Text-to-Image Diffusion Model with Any Condition.**<br>
*Sicheng Mo, Fangzhou Mu, Kuan Heng Lin, Yanli Liu, Bochen Guan, Yin Li, Bolei Zhou.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.07536)]

**Local Conditional Controlling for Text-to-Image Diffusion Models.**<br>
*Yibo Zhao, Liang Peng, Yang Yang, Zekai Luo, Hengjia Li, Yao Chen, Wei Zhao, qinglin lu, Boxi Wu, Wei Liu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.08768)]

**SCEdit: Efficient and Controllable Image Diffusion Generation via Skip Connection Editing.**<br>
*Zeyinzi Jiang, Chaojie Mao, Yulin Pan, Zhen Han, Jingfeng Zhang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.11392)]

**Towards Flexible, Scalable, and Adaptive Multi-Modal Conditioned Face Synthesis.**<br>
*Jingjing Ren, Cheng Xu, Haoyu Chen, Xinran Qin, Chongyi Li, Lei Zhu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.16274)]


### Advanced Text-Conditioned Generation
**TRAINING-FREE STRUCTURED DIFFUSION GUIDANCE FOR COMPOSITIONAL TEXT-TO-I MAGE SYNTHESIS.**<br>
*Weixi Feng, Xuehai He, Tsu-Jui Fu, Varun Jampani, Arjun Akula, Pradyumna Narayana, Sugato Basu, Xin Eric Wang, William Yang Wang.*<br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2212.05032)]

**Attend-and-Excite- Attention-Based Semantic Guidance for Text-to-Image  Diffusion Models.**<br>
*Hila Chefer, Yuval Alaluf, Yael Vinker, Lior Wolf, Daniel Cohen-Or.*<br>
TOG 2023. [[PDF](https://arxiv.org/abs/2301.13826)]

**GlueGen: Plug and Play Multi-modal Encoders for X-to-image Generation.**<br>
*Can Qin, Ning Yu, Chen Xing, Shu Zhang, Zeyuan Chen, Stefano Ermon, Yun Fu, Caiming Xiong, Ran Xu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.10056)]

**Expressive Text-to-Image Generation with Rich Text.**<br>
*Songwei Ge, Taesung Park, Jun-Yan Zhu, Jia-Bin Huang.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2304.06720)]

**Linguistic Binding in Diffusion Models-  Enhancing Attribute Correspondence  through Attention Map Alignment.**<br>
*Royi Rassin, Eran Hirsch, Daniel Glickman, Shauli Ravfogel, Yoav Goldberg, Gal Chechik.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2306.08877)]

**Tailored Visions: Enhancing Text-to-Image Generation with Personalized Prompt Rewriting.**<br>
*Zijie Chen, Lichao Zhang, Fangsheng Weng, Lili Pan, Zhenzhong Lan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.08129)]

**Paragraph-to-Image Generation with Information-Enriched Diffusion Model.**<br>
*Weijia Wu, Zhuang Li, Yefei He, Mike Zheng Shou, Chunhua Shen, Lele Cheng, Yan Li, Tingting Gao, Di Zhang, Zhongyuan Wang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.14284)]

**PEA-Diffusion: Parameter-Efficient Adapter with Knowledge Distillation  in non-English Text-to-Image Generation.**<br>
*Jian Ma, Chen Chen, Qingsong Xie, Haonan Lu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.17086)]


### In-Context Generation
**In-Context Learning Unlocked for Diffusion Models.**<br>
*Zhendong Wang, Yifan Jiang, Yadong Lu, Yelong Shen, Pengcheng He, Weizhu Chen, Zhangyang Wang, Mingyuan Zhou.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.01115)]

**Improving In-Context Learning in Diffusion Models with Visual Context-Modulated Prompts.**<br>
*Tianqi Chen, Yongfei Liu, Zhendong Wang, Jianbo Yuan, Quanzeng You, Hongxia Yang, Mingyuan Zhou.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.01408)]


### Brain-Guided Generation
**Seeing Beyond the Brain: Conditional Diffusion Model with Sparse Masked Modeling for Vision Decoding.**<br>
*Zijiao Chen, Jiaxin Qing, Tiange Xiang, Wan Lin Yue, Juan Helen Zhou.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.06956)]

**High-Resolution Image Reconstruction With Latent Diffusion Models From Human Brain Activity.**<br>
*Yu Takagi, Shinji Nishimoto.*<br>
CVPR 2023. 

**Natural.**<br>
*Furkan Ozcelik, Rufin VanRullen.*<br>
Scientific Reports 2023. [[PDF](https://arxiv.org/abs/2303.05334)]

**MindDiffuser: Controlled Image Reconstruction from Human Brain Activity with Semantic and Structural Diffusion.**<br>
*Yizhuo Lu, Changde Du, Dianpeng Wang, Huiguang He.*<br>
ACM MM 2023. [[PDF](https://arxiv.org/abs/2303.14139)]

**Natural Image Reconstruction from fMRI Based on Self-supervised Representation Learning and Latent Diffusion Model.**<br>
*Pengyu Ni, Yifeng Zhang.*<br>
ACM MM 2023. 

**DreamDiffusion: Generating High-Quality Images from Brain EEG Signals.**<br>
*Yunpeng Bai, Xintao Wang, Yan-pei Cao, Yixiao Ge, Chun Yuan, Ying Shan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.16934)]

**BrainVis: Exploring the Bridge between Brain and Visual Signals via Image Reconstruction.**<br>
*Honghao Fu, Zhiqi Shen, Jing Jih Chin, Hao Wang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.14871)]


### Sound-Guided Generation
**GlueGen: Plug and Play Multi-modal Encoders for X-to-image Generation.**<br>
*Can Qin, Ning Yu, Chen Xing, Shu Zhang, Zeyuan Chen, Stefano Ermon, Yun Fu, Caiming Xiong, Ran Xu.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.10056)]

**Align, Adapt and Inject: Sound-guided
Unified Image Generation.**<br>
*Yue Yang, Kaipeng Zhang, Yuying Ge, Wenqi Shao, Zeyue Xue, Yu Qiao, Ping Luo.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.11504)]


### Text Rendering
**Character-Aware Models Improve Visual Text Rendering.**<br>
*Rosanne Liu, Dan Garrette, Chitwan Saharia, William Chan, Adam Roberts, Sharan Narang, Irina Blok, RJ Mical, Mohammad Norouzi, Noah Constant.*<br>
ACL 2022. [[PDF](https://arxiv.org/abs/2212.10562)]

**GlyphDraw: Seamlessly Rendering Text with Intricate Spatial Structures in Text-to-Image.**<br>
*Jian Ma, Mingjun Zhao, Chen Chen, Ruichen Wang, Di Niu, Haonan Lu, Xiaodong Lin.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.17870)]

**TextDiffuser: Diffusion Models as Text Painters.**<br>
*Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, Furu Wei.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.10855)]

**GlyphControl: Glyph Conditional Control for Visual Text Generation.**<br>
*Yukang Yang, Dongnan Gui, Yuhui Yuan, Weicong Liang, Haisong Ding, Han Hu, Kai Chen.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2305.18259)]

**AnyText: Multilingual Visual Text Generation And Editing.**<br>
*Yuxiang Tuo, Wangmeng Xiang, Jun-Yan He, Yifeng Geng, Xuansong Xie.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.03054)]

**TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering.**<br>
*Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, Furu Wei.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.16465)]

**UDiffText: A Unified Framework for High-quality Text Synthesis in Arbitrary Images via Character-aware Diffusion Models.**<br>
*Yiming Zhao, Zhouhui Lian.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.04884)]

**Brush Your Text: Synthesize Any Scene Text on Images via Diffusion Model.**<br>
*Lingjun Zhang, Xinyuan Chen, Yaohui Wang, Yue Lu, Yu Qiao.*<br>
AAAI 2024. [[PDF](https://arxiv.org/abs/2312.12232)]


## ⭐Generation with Multiple Conditions
### Joint Training
**Composer: Creative and controllable image synthesis with composable conditions.**<br>
*Lianghua Huang, Di Chen, Yu Liu, Yujun Shen, Deli Zhao, Jingren Zhou.*<br>
ICML 2023. [[PDF](https://arxiv.org/abs/2302.09778)]

**SVDiff- Compact Parameter Space for Diffusion Fine-Tuning.**<br>
*Ligong Han, Yinxiao Li, Han Zhang, Peyman Milanfar, Dimitris Metaxas, Feng Yang.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2303.11305)]

**FastComposer: Tuning-Free Multi-Subject Image Generation with Localized Attention.**<br>
*Guangxuan Xiao, Tianwei Yin, William T. Freeman, Frédo Durand, Song Han.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.10431)]

**Cocktail: Mixing Multi-Modality Controls for Text-Conditional Image Generation.**<br>
*Minghui Hu, Jianbin Zheng, Daqing Liu, Chuanxia Zheng, Chaoyue Wang, Dacheng Tao, Tat-Jen Cham.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2306.00964)]


### Continual Learning
**Continual Diffusion- Continual Customization of  Text-to-Image Diffusion with C-LoRA.**<br>
*James Seale Smith, Yen-Chang Hsu, Lingyu Zhang, Ting Hua, Zsolt Kira, Yilin Shen, Hongxia Jin.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2304.06027)]

**Create Your World: Lifelong Text-to-Image
Diffusion.**<br>
*Gan Sun, Wenqi Liang, Jiahua Dong, Jun Li, Zhengming Ding, Yang Cong.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.04430)]

**Continual Diffusion with STAMINA: STack-And-Mask INcremental Adapters.**<br>
*James Seale Smith, Yen-Chang Hsu, Zsolt Kira, Yilin Shen, Hongxia Jin.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.18763)]


### Weight Fusion
**Multi-Concept Customization of Text-to-Image Diffusion.**<br>
*Nupur Kumari, Bingliang Zhang, Richard Zhang, Eli Shechtman, Jun-Yan Zhu.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2212.04488)]

**Cones- Concept Neurons in Diffusion Models for Customized Generation.**<br>
*Zhiheng Liu, Ruili Feng, Kai Zhu, Yifei Zhang, Kecheng Zheng, Yu Liu, Deli Zhao, Jingren Zhou, Yang Cao.*<br>
ICML 2023. [[PDF](https://arxiv.org/abs/2303.05125)]

**Mix-of-Show- Decentralized Low-Rank Adaptation for  Multi-Concept Customization of Diffusion Models.**<br>
*Yuchao Gu, Xintao Wang, Jay Zhangjie Wu, Yujun Shi, Yunpeng Chen, Zihan Fan, Wuyou Xiao, Rui Zhao, Shuning Chang, Weijia Wu, Yixiao Ge, Ying Shan, Mike Zheng Shou.*<br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2305.18292)]

**ZipLoRA- Any Subject in Any Style by Effectively Merging LoRAs.**<br>
*Viraj Shah, Nataniel Ruiz, Forrester Cole, Erika Lu, Svetlana Lazebnik, Yuanzhen Li, Varun Jampani.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.13600)]

**Orthogonal Adaptation for Modular Customization of Diffusion Models.**<br>
*Ryan Po, Guandao Yang, Kfir Aberman, Gordon Wetzstein.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.02432)]


### Attention-based Integration
**Cones 2- Customizable Image Synthesis  with Multiple Subjects .**<br>
*Zhiheng Liu, Yifei Zhang, Yujun Shen, Kecheng Zheng, Kai Zhu, Ruili Feng, Yu Liu, Deli Zhao, Jingren Zhou, Yang Cao.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.19327)]


### Guidance Composition
**Decompose and Realign: Tackling Condition Misalignment in Text-to-Image Diffusion Models.**<br>
*Luozhou Wang, Guibao Shen, Wenhang Ge, Guangyong Chen, Yijun Li, Ying-cong Chen.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.14408)]

**High-fidelity Person-centric Subject-to-Image Synthesis.**<br>
*Yibin Wang, Weizhong Zhang, Jianwei Zheng, Cheng Jin.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2311.10329)]

**Concept-centric Personalization with Large-scale Diffusion Priors.**<br>
*Pu Cao, Lu Yang, Feng Zhou, Tianrui Huang, Qing Song.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.08195)]


## 🔥Universal Controllable Generation
### Universal Conditional Score Prediction
**DiffBlender: Scalable and Composable Multimodal Text-to-Image Diffusion Models.**<br>
*Sungnyun Kim, Junsoo Lee, Kibeom Hong, Daesik Kim, Namhyuk Ahn.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.15194)]

**Generative Multimodal Models are In-Context Learners.**<br>
*Quan Sun, Yufeng Cui, Xiaosong Zhang, Fan Zhang, Qiying Yu, Zhengxiong Luo, Yueze Wang, Yongming Rao, Jingjing Liu, Tiejun Huang, Xinlong Wang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.13286)]


### Universal Condition-Guided Score Estimation
**Universal Guidance for Diffusion Models.**<br>
*Arpit Bansal, Hong-Min Chu, Avi Schwarzschild, Soumyadip Sengupta, Micah Goldblum, Jonas Geiping, Tom Goldstein.*<br>
CVPRW 2023. [[PDF](https://arxiv.org/abs/2302.07121)]

**FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model.**<br>
*Jiwen Yu, Yinhuai Wang, Chen Zhao, Bernard Ghanem, Jian Zhang.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.09833)]

**Towards Accurate Guided Diffusion Sampling through Symplectic Adjoint Method.**<br>
*Jiachun Pan, Hanshu Yan, Jun Hao Liew, Jiashi Feng, Vincent Y. F. Tan.*<br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.12030)]


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models&type=Date)](https://star-history.com/#PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models&Date)

