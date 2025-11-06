# 🚀 Index of Algorithms for AIMA n-th Edition (Future)

## 預計新增的現代 AI 算法與圖表

本文檔列出未來版本可能新增的算法，反映 2020 年代的 AI 研究進展。

---

## 📊 新增算法統計

- **新增章節**: 3 個（深度學習進階、大型語言模型、生成式 AI）
- **新增算法**: 50+ 個
- **新增圖表**: 60+ 個
- **更新章節**: 所有主要章節

---

## 🆕 Part VII: Deep Neural Networks (深度神經網絡進階)

### Chapter 26: Advanced Neural Network Architectures (進階神經網絡架構)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 26.1 | Convolutional-Neural-Network | `CNN` | [`deep_learning.py`][dl] | LeCun | 1998 |
| 26.2 | Conv-Layer-Forward-Pass | `conv_forward` | [`deep_learning.py`][dl] | - | - |
| 26.3 | Max-Pooling | `max_pooling` | [`deep_learning.py`][dl] | - | - |
| 26.4 | Batch-Normalization | `batch_norm` | [`deep_learning.py`][dl] | Ioffe & Szegedy | 2015 |
| 26.5 | Dropout-Regularization | `dropout` | [`deep_learning.py`][dl] | Hinton et al. | 2012 |
| 26.6 | ResNet-Block | `residual_block` | [`deep_learning.py`][dl] | He et al. | 2015 |
| 26.7 | Skip-Connection | `skip_connection` | [`deep_learning.py`][dl] | - | - |
| 26.8 | DenseNet-Block | `dense_block` | [`deep_learning.py`][dl] | Huang et al. | 2017 |
| 26.9 | Inception-Module | `inception_module` | [`deep_learning.py`][dl] | Szegedy et al. | 2015 |
| 26.10 | MobileNet-Block | `mobilenet_block` | [`deep_learning.py`][dl] | Howard et al. | 2017 |

---

### Chapter 27: Attention Mechanisms and Transformers (注意力機制與 Transformer)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 27.1 | Recurrent-Neural-Network | `RNN` | [`sequence_models.py`][seq] | Rumelhart | 1986 |
| 27.2 | LSTM-Cell | `LSTM` | [`sequence_models.py`][seq] | Hochreiter & Schmidhuber | 1997 |
| 27.3 | GRU-Cell | `GRU` | [`sequence_models.py`][seq] | Cho et al. | 2014 |
| 27.4 | Seq2Seq-Model | `seq2seq` | [`sequence_models.py`][seq] | Sutskever et al. | 2014 |
| 27.5 | Attention-Mechanism | `attention` | [`attention.py`][attn] | Bahdanau et al. | 2015 |
| 27.6 | **Scaled-Dot-Product-Attention** 🌟 | `scaled_dot_product_attention` | [`attention.py`][attn] | Vaswani et al. | 2017 |
| 27.7 | **Multi-Head-Attention** 🌟 | `multi_head_attention` | [`attention.py`][attn] | Vaswani et al. | 2017 |
| 27.8 | **Transformer-Encoder** 🌟 | `transformer_encoder` | [`transformers.py`][trans] | Vaswani et al. | 2017 |
| 27.9 | **Transformer-Decoder** 🌟 | `transformer_decoder` | [`transformers.py`][trans] | Vaswani et al. | 2017 |
| 27.10 | Positional-Encoding | `positional_encoding` | [`transformers.py`][trans] | - | - |
| 27.11 | Self-Attention | `self_attention` | [`attention.py`][attn] | - | - |
| 27.12 | Cross-Attention | `cross_attention` | [`attention.py`][attn] | - | - |

---

### Chapter 28: Large Language Models (大型語言模型)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 28.1 | **BERT-Pretraining** 🌟 | `bert_pretrain` | [`language_models.py`][lm] | Devlin et al. | 2018 |
| 28.2 | Masked-Language-Modeling | `masked_lm` | [`language_models.py`][lm] | - | - |
| 28.3 | Next-Sentence-Prediction | `next_sentence_pred` | [`language_models.py`][lm] | - | - |
| 28.4 | **GPT-Architecture** 🌟 | `gpt_model` | [`language_models.py`][lm] | Radford et al. | 2018 |
| 28.5 | Causal-Language-Modeling | `causal_lm` | [`language_models.py`][lm] | - | - |
| 28.6 | **Fine-Tuning-LLM** | `fine_tune` | [`language_models.py`][lm] | - | - |
| 28.7 | **Prompt-Engineering** | `prompt_template` | [`language_models.py`][lm] | - | 2021 |
| 28.8 | **Few-Shot-Learning** 🌟 | `few_shot_learning` | [`language_models.py`][lm] | Brown et al. | 2020 |
| 28.9 | **In-Context-Learning** | `in_context_learning` | [`language_models.py`][lm] | - | 2020 |
| 28.10 | **Chain-of-Thought-Prompting** | `chain_of_thought` | [`language_models.py`][lm] | Wei et al. | 2022 |
| 28.11 | **RLHF** (Reinforcement Learning from Human Feedback) 🌟 | `rlhf` | [`language_models.py`][lm] | Christiano et al. | 2017 |
| 28.12 | Instruction-Tuning | `instruction_tuning` | [`language_models.py`][lm] | - | 2022 |
| 28.13 | **Retrieval-Augmented-Generation** | `rag` | [`language_models.py`][lm] | Lewis et al. | 2020 |

---

## 🎨 Part VIII: Generative AI (生成式 AI)

### Chapter 29: Generative Models (生成模型)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 29.1 | Autoencoder | `autoencoder` | [`generative.py`][gen] | - | 1980s |
| 29.2 | Variational-Autoencoder | `VAE` | [`generative.py`][gen] | Kingma & Welling | 2013 |
| 29.3 | VAE-Reparameterization-Trick | `reparameterization` | [`generative.py`][gen] | - | - |
| 29.4 | **GAN-Architecture** 🌟 | `GAN` | [`generative.py`][gen] | Goodfellow et al. | 2014 |
| 29.5 | GAN-Training-Loop | `gan_train` | [`generative.py`][gen] | - | - |
| 29.6 | DCGAN (Deep Convolutional GAN) | `DCGAN` | [`generative.py`][gen] | Radford et al. | 2015 |
| 29.7 | **StyleGAN** | `StyleGAN` | [`generative.py`][gen] | Karras et al. | 2019 |
| 29.8 | Conditional-GAN | `CGAN` | [`generative.py`][gen] | Mirza & Osindero | 2014 |
| 29.9 | CycleGAN | `CycleGAN` | [`generative.py`][gen] | Zhu et al. | 2017 |
| 29.10 | **Diffusion-Model** 🌟 | `diffusion_model` | [`diffusion.py`][diff] | Sohl-Dickstein et al. | 2015 |
| 29.11 | **DDPM** (Denoising Diffusion Probabilistic Models) 🌟 | `DDPM` | [`diffusion.py`][diff] | Ho et al. | 2020 |
| 29.12 | Diffusion-Forward-Process | `diffusion_forward` | [`diffusion.py`][diff] | - | - |
| 29.13 | Diffusion-Reverse-Process | `diffusion_reverse` | [`diffusion.py`][diff] | - | - |
| 29.14 | **Stable-Diffusion** 🌟 | `stable_diffusion` | [`diffusion.py`][diff] | Rombach et al. | 2022 |
| 29.15 | Latent-Diffusion | `latent_diffusion` | [`diffusion.py`][diff] | - | - |
| 29.16 | **CLIP** (Contrastive Language-Image Pre-training) | `CLIP` | [`multimodal.py`][mm] | Radford et al. | 2021 |

---

### Chapter 30: Multimodal AI (多模態 AI)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 30.1 | Vision-Transformer | `ViT` | [`vision_models.py`][vis] | Dosovitskiy et al. | 2020 |
| 30.2 | Patch-Embedding | `patch_embed` | [`vision_models.py`][vis] | - | - |
| 30.3 | **DALL-E-Architecture** 🌟 | `dalle` | [`multimodal.py`][mm] | Ramesh et al. | 2021 |
| 30.4 | Image-GPT | `image_gpt` | [`multimodal.py`][mm] | Chen et al. | 2020 |
| 30.5 | **Flamingo** | `flamingo` | [`multimodal.py`][mm] | Alayrac et al. | 2022 |
| 30.6 | Text-to-Image-Generation | `text_to_image` | [`multimodal.py`][mm] | - | - |
| 30.7 | Image-Captioning | `image_caption` | [`multimodal.py`][mm] | - | - |
| 30.8 | Visual-Question-Answering | `vqa` | [`multimodal.py`][mm] | - | - |

---

## 🎮 Part V (Expanded): Advanced Reinforcement Learning

### Chapter 21 (Extended): Modern RL Algorithms

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 21.9 | **Deep-Q-Network (DQN)** 🌟 | `DQN` | [`deep_rl.py`][drl] | Mnih et al. | 2015 |
| 21.10 | Experience-Replay | `experience_replay` | [`deep_rl.py`][drl] | - | - |
| 21.11 | Target-Network | `target_network` | [`deep_rl.py`][drl] | - | - |
| 21.12 | Double-DQN | `double_dqn` | [`deep_rl.py`][drl] | van Hasselt et al. | 2015 |
| 21.13 | Dueling-DQN | `dueling_dqn` | [`deep_rl.py`][drl] | Wang et al. | 2016 |
| 21.14 | Prioritized-Experience-Replay | `prioritized_replay` | [`deep_rl.py`][drl] | Schaul et al. | 2015 |
| 21.15 | **Policy-Gradient** 🌟 | `policy_gradient` | [`deep_rl.py`][drl] | Sutton et al. | 2000 |
| 21.16 | REINFORCE-Algorithm | `reinforce` | [`deep_rl.py`][drl] | Williams | 1992 |
| 21.17 | **Actor-Critic** | `actor_critic` | [`deep_rl.py`][drl] | Konda & Tsitsiklis | 2000 |
| 21.18 | **A3C** (Asynchronous Actor-Critic) | `A3C` | [`deep_rl.py`][drl] | Mnih et al. | 2016 |
| 21.19 | **PPO** (Proximal Policy Optimization) 🌟 | `PPO` | [`deep_rl.py`][drl] | Schulman et al. | 2017 |
| 21.20 | Trust-Region-Policy-Optimization | `TRPO` | [`deep_rl.py`][drl] | Schulman et al. | 2015 |
| 21.21 | Soft-Actor-Critic | `SAC` | [`deep_rl.py`][drl] | Haarnoja et al. | 2018 |
| 21.22 | **AlphaZero-MCTS** 🌟 | `alphazero_mcts` | [`games_rl.py`][grl] | Silver et al. | 2017 |
| 21.23 | Monte-Carlo-Tree-Search-Neural | `mcts_neural` | [`games_rl.py`][grl] | - | - |
| 21.24 | Model-Based-RL | `model_based_rl` | [`deep_rl.py`][drl] | - | - |
| 21.25 | World-Models | `world_models` | [`deep_rl.py`][drl] | Ha & Schmidhuber | 2018 |

---

## 🔬 Part IX: Modern AI Techniques (現代 AI 技術)

### Chapter 31: Self-Supervised Learning (自監督學習)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 31.1 | Contrastive-Learning | `contrastive_learning` | [`ssl.py`][ssl] | - | - |
| 31.2 | **SimCLR** | `simclr` | [`ssl.py`][ssl] | Chen et al. | 2020 |
| 31.3 | **MoCo** (Momentum Contrast) | `moco` | [`ssl.py`][ssl] | He et al. | 2020 |
| 31.4 | **BYOL** (Bootstrap Your Own Latent) | `byol` | [`ssl.py`][ssl] | Grill et al. | 2020 |
| 31.5 | Data-Augmentation-Pipeline | `augmentation` | [`ssl.py`][ssl] | - | - |
| 31.6 | Pretext-Task | `pretext_task` | [`ssl.py`][ssl] | - | - |

---

### Chapter 32: Meta-Learning and Few-Shot Learning (元學習與小樣本學習)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 32.1 | **MAML** (Model-Agnostic Meta-Learning) 🌟 | `MAML` | [`meta_learning.py`][meta] | Finn et al. | 2017 |
| 32.2 | Meta-Gradient-Update | `meta_gradient` | [`meta_learning.py`][meta] | - | - |
| 32.3 | Prototypical-Networks | `prototypical_net` | [`meta_learning.py`][meta] | Snell et al. | 2017 |
| 32.4 | Matching-Networks | `matching_net` | [`meta_learning.py`][meta] | Vinyals et al. | 2016 |
| 32.5 | Siamese-Networks | `siamese_net` | [`meta_learning.py`][meta] | Koch et al. | 2015 |
| 32.6 | Relation-Networks | `relation_net` | [`meta_learning.py`][meta] | Sung et al. | 2018 |

---

### Chapter 33: Neural Architecture Search (神經架構搜索)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 33.1 | NAS-Search-Space | `nas_search_space` | [`nas.py`][nas] | - | - |
| 33.2 | **ENAS** (Efficient NAS) | `ENAS` | [`nas.py`][nas] | Pham et al. | 2018 |
| 33.3 | **DARTS** (Differentiable Architecture Search) | `DARTS` | [`nas.py`][nas] | Liu et al. | 2018 |
| 33.4 | NASNet-Cell | `nasnet_cell` | [`nas.py`][nas] | Zoph et al. | 2018 |
| 33.5 | AutoML-Pipeline | `automl` | [`nas.py`][nas] | - | - |

---

### Chapter 34: Explainable AI (可解釋 AI)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 34.1 | **LIME** (Local Interpretable Model-Agnostic Explanations) 🌟 | `LIME` | [`explainable_ai.py`][xai] | Ribeiro et al. | 2016 |
| 34.2 | **SHAP** (SHapley Additive exPlanations) 🌟 | `SHAP` | [`explainable_ai.py`][xai] | Lundberg & Lee | 2017 |
| 34.3 | Grad-CAM | `grad_cam` | [`explainable_ai.py`][xai] | Selvaraju et al. | 2017 |
| 34.4 | Integrated-Gradients | `integrated_gradients` | [`explainable_ai.py`][xai] | Sundararajan et al. | 2017 |
| 34.5 | Attention-Visualization | `attention_viz` | [`explainable_ai.py`][xai] | - | - |
| 34.6 | Feature-Attribution | `feature_attribution` | [`explainable_ai.py`][xai] | - | - |

---

### Chapter 35: Federated Learning and Privacy (聯邦學習與隱私)

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 35.1 | **Federated-Averaging** 🌟 | `federated_averaging` | [`federated.py`][fed] | McMahan et al. | 2017 |
| 35.2 | Differential-Privacy | `differential_privacy` | [`privacy.py`][priv] | Dwork et al. | 2006 |
| 35.3 | Private-Aggregation | `private_aggregation` | [`privacy.py`][priv] | - | - |
| 35.4 | Secure-Multi-Party-Computation | `smpc` | [`privacy.py`][priv] | - | - |
| 35.5 | Homomorphic-Encryption | `homomorphic_enc` | [`privacy.py`][priv] | - | - |

---

## 🔄 更新現有章節的新算法

### Chapter 18 (Extended): Modern Deep Learning

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 18.35 | **Adam-Optimizer** 🌟 | `Adam` | [`optimizers.py`][opt] | Kingma & Ba | 2014 |
| 18.36 | RMSprop-Optimizer | `RMSprop` | [`optimizers.py`][opt] | Hinton | 2012 |
| 18.37 | Learning-Rate-Scheduling | `lr_schedule` | [`optimizers.py`][opt] | - | - |
| 18.38 | Weight-Initialization-Xavier | `xavier_init` | [`utils.py`][utils] | Glorot & Bengio | 2010 |
| 18.39 | Weight-Initialization-He | `he_init` | [`utils.py`][utils] | He et al. | 2015 |
| 18.40 | Gradient-Clipping | `gradient_clipping` | [`utils.py`][utils] | - | - |

---

### Chapter 22-23 (Extended): Modern NLP

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 23.6 | **Word2Vec** 🌟 | `word2vec` | [`embeddings.py`][emb] | Mikolov et al. | 2013 |
| 23.7 | Skip-Gram-Model | `skip_gram` | [`embeddings.py`][emb] | - | - |
| 23.8 | CBOW (Continuous Bag of Words) | `cbow` | [`embeddings.py`][emb] | - | - |
| 23.9 | **GloVe** | `glove` | [`embeddings.py`][emb] | Pennington et al. | 2014 |
| 23.10 | **FastText** | `fasttext` | [`embeddings.py`][emb] | Bojanowski et al. | 2017 |
| 23.11 | **ELMo** | `elmo` | [`embeddings.py`][emb] | Peters et al. | 2018 |
| 23.12 | Contextualized-Embeddings | `contextualized_emb` | [`embeddings.py`][emb] | - | - |
| 23.13 | **Tokenization-BPE** | `bpe_tokenizer` | [`tokenizers.py`][tok] | Sennrich et al. | 2016 |
| 23.14 | WordPiece-Tokenization | `wordpiece` | [`tokenizers.py`][tok] | - | - |
| 23.15 | SentencePiece | `sentencepiece` | [`tokenizers.py`][tok] | Kudo & Richardson | 2018 |

---

### Chapter 24 (Extended): Modern Computer Vision

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Year** |
|:-----------|:---------|:-------------------------|:---------|:------------|:---------|
| 24.9 | **YOLO** (You Only Look Once) 🌟 | `YOLO` | [`object_detection.py`][od] | Redmon et al. | 2016 |
| 24.10 | **R-CNN** | `RCNN` | [`object_detection.py`][od] | Girshick et al. | 2014 |
| 24.11 | Fast-R-CNN | `fast_rcnn` | [`object_detection.py`][od] | Girshick | 2015 |
| 24.12 | Faster-R-CNN | `faster_rcnn` | [`object_detection.py`][od] | Ren et al. | 2015 |
| 24.13 | **Mask-R-CNN** | `mask_rcnn` | [`segmentation.py`][seg] | He et al. | 2017 |
| 24.14 | Semantic-Segmentation | `semantic_seg` | [`segmentation.py`][seg] | - | - |
| 24.15 | Instance-Segmentation | `instance_seg` | [`segmentation.py`][seg] | - | - |
| 24.16 | **U-Net** | `unet` | [`segmentation.py`][seg] | Ronneberger et al. | 2015 |
| 24.17 | DeepLab | `deeplab` | [`segmentation.py`][seg] | Chen et al. | 2017 |

---

## 📊 新增資料結構

### Extended Data Structures

| **Figure** | **Name (in repository)** | **File** | **Description** |
|:-----------|:-------------------------|:---------|:----------------|
| 26.N | ImageNet-Dataset | [`datasets.py`][data] | 大規模圖像分類數據集 |
| 27.N | COCO-Dataset | [`datasets.py`][data] | 目標檢測和分割數據集 |
| 28.N | SQuAD-Dataset | [`datasets.py`][data] | 問答數據集 |
| 28.N | GLUE-Benchmark | [`datasets.py`][data] | NLP 基準測試集 |
| 29.N | CelebA-Dataset | [`datasets.py`][data] | 人臉屬性數據集 |
| 30.N | Attention-Pattern-Visualizer | [`visualizers.py`][viz] | 注意力模式可視化工具 |

---

## 🌟 重點新算法（必須實現）

### 核心算法標記為 🌟

1. **Transformer 相關**
   - Scaled Dot-Product Attention (Figure 27.6)
   - Multi-Head Attention (Figure 27.7)
   - Transformer Encoder/Decoder (Figure 27.8-9)

2. **大型語言模型**
   - BERT (Figure 28.1)
   - GPT (Figure 28.4)
   - Few-Shot Learning (Figure 28.8)
   - RLHF (Figure 28.11)

3. **生成式 AI**
   - GAN (Figure 29.4)
   - Diffusion Models (Figure 29.10)
   - DDPM (Figure 29.11)
   - Stable Diffusion (Figure 29.14)

4. **強化學習**
   - DQN (Figure 21.9)
   - PPO (Figure 21.19)
   - AlphaZero MCTS (Figure 21.22)

5. **計算機視覺**
   - YOLO (Figure 24.9)
   - Mask R-CNN (Figure 24.13)

6. **可解釋 AI**
   - LIME (Figure 34.1)
   - SHAP (Figure 34.2)

---

## 👥 新算法的先驅者總覽

### Transformer 時代（2017-）

- **Ashish Vaswani et al.** - Transformer ("Attention Is All You Need", 2017)
- **Jacob Devlin et al.** - BERT (2018)
- **Alec Radford et al.** - GPT series (2018-2023)
- **Tom Brown et al.** - GPT-3, Few-Shot Learning (2020)

### 生成式 AI

- **Ian Goodfellow** - GAN (2014)
- **Jascha Sohl-Dickstein et al.** - Diffusion Models (2015)
- **Jonathan Ho et al.** - DDPM (2020)
- **Robin Rombach et al.** - Stable Diffusion (2022)
- **Aditya Ramesh et al.** - DALL-E (2021)

### 深度強化學習

- **Volodymyr Mnih et al.** - DQN, A3C (2015-2016)
- **John Schulman et al.** - TRPO, PPO (2015-2017)
- **David Silver et al.** - AlphaGo, AlphaZero (2016-2017)

### 計算機視覺

- **Joseph Redmon et al.** - YOLO (2016)
- **Kaiming He et al.** - ResNet, Mask R-CNN (2015-2017)
- **Alexey Dosovitskiy et al.** - Vision Transformer (2020)

### 可解釋 AI

- **Marco Tulio Ribeiro et al.** - LIME (2016)
- **Scott Lundberg & Su-In Lee** - SHAP (2017)

---

## 📈 實現優先級

### High Priority (第一階段)

1. Transformer 架構完整實現
2. BERT 和 GPT 基礎模型
3. 基本 Diffusion Models
4. DQN 和 PPO
5. YOLO 目標檢測

### Medium Priority (第二階段)

6. 完整的 GAN 家族
7. 元學習算法（MAML）
8. 自監督學習（SimCLR, MoCo）
9. 可解釋 AI（LIME, SHAP）
10. Vision Transformer

### Low Priority (第三階段)

11. 神經架構搜索
12. 聯邦學習
13. 世界模型
14. 進階 Transformer 變體

---

## 🔗 新增檔案結構

```python
aima-python/
├── deep_learning.py          # 深度學習基礎
├── attention.py              # 注意力機制
├── transformers.py           # Transformer 架構
├── language_models.py        # 大型語言模型
├── generative.py             # 生成模型（VAE, GAN）
├── diffusion.py              # 擴散模型
├── multimodal.py             # 多模態模型
├── deep_rl.py                # 深度強化學習
├── games_rl.py               # 遊戲 AI（AlphaZero 等）
├── ssl.py                    # 自監督學習
├── meta_learning.py          # 元學習
├── nas.py                    # 神經架構搜索
├── explainable_ai.py         # 可解釋 AI
├── federated.py              # 聯邦學習
├── privacy.py                # 隱私保護
├── optimizers.py             # 優化器
├── embeddings.py             # 詞嵌入
├── tokenizers.py             # 分詞器
├── object_detection.py       # 目標檢測
├── segmentation.py           # 圖像分割
├── vision_models.py          # 視覺模型
├── sequence_models.py        # 序列模型
├── datasets.py               # 數據集工具
└── visualizers.py            # 可視化工具
```

---

## 📝 實現建議

### 代碼風格

- 遵循現有的 Python 3.7+ 風格
- 使用 Type Hints
- 完整的 Docstrings
- 單元測試覆蓋
- Jupyter Notebook 示例

### 依賴管理

```python
# 新增依賴
torch>=2.0.0
transformers>=4.30.0
diffusers>=0.21.0
einops>=0.6.0
timm>=0.9.0
```

### 測試策略

- 單元測試：每個算法獨立測試
- 集成測試：完整pipeline測試
- 效能測試：與baseline比較
- 可視化測試：輸出質量檢查

---

## 🎯 教育價值

這些新算法反映了：

1. **深度學習革命**（2012-2020）
2. **Transformer 時代**（2017-現在）
3. **生成式 AI 爆發**（2020-現在）
4. **負責任 AI**（可解釋性、隱私）
5. **效率與可擴展性**（NAS、聯邦學習）

---

## 🌍 與封面人物的聯繫

這些現代算法延續了封面人物的遺產：

- **艾達·洛芙萊斯** → GPT 等可以"創作"的 AI
- **圖靈** → Transformer 的注意力機制
- **貝葉斯** → 現代概率生成模型
- **辛頓** → 深度學習的實現者

---

## 📚 參考資源

### 重要論文

- "Attention Is All You Need" (Vaswani et al., 2017)
- "BERT: Pre-training of Deep Bidirectional Transformers" (Devlin et al., 2018)
- "Language Models are Few-Shot Learners" (Brown et al., 2020)
- "Denoising Diffusion Probabilistic Models" (Ho et al., 2020)

### 在線資源

- [Papers With Code](https://paperswithcode.com/)
- [Hugging Face](https://huggingface.co/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

---

**注意**: 🌟 標記的算法是核心算法，應優先實現和測試。

<!---新增檔案引用連結-->
[dl]:../master/deep_learning.py
[attn]:../master/attention.py
[trans]:../master/transformers.py
[lm]:../master/language_models.py
[gen]:../master/generative.py
[diff]:../master/diffusion.py
[mm]:../master/multimodal.py
[drl]:../master/deep_rl.py
[grl]:../master/games_rl.py
[ssl]:../master/ssl.py
[meta]:../master/meta_learning.py
[nas]:../master/nas.py
[xai]:../master/explainable_ai.py
[fed]:../master/federated.py
[priv]:../master/privacy.py
[opt]:../master/optimizers.py
[emb]:../master/embeddings.py
[tok]:../master/tokenizers.py
[od]:../master/object_detection.py
[seg]:../master/segmentation.py
[vis]:../master/vision_models.py
[seq]:../master/sequence_models.py
[data]:../master/datasets.py
[viz]:../master/visualizers.py
[utils]:../master/utils.py

