# CS231n notes + slides 参考文献路线图

## 一条主线

> 数据与评价 → 线性分类 → 梯度与反向传播 → 网络设计与正则化 → 优化与实验方法 → CNN 架构 → 表征分析与鲁棒性 → 迁移学习

如果只走最短路线，建议依次精读：Domingos → Weston & Watkins → Baydin → Glorot & Bengio → He 初始化 → BatchNorm → Dropout → Adam → LeNet → AlexNet → VGG → ResNet → Zeiler & Fergus → Yosinski。

## 1. 数据、距离与评价

- Pedro Domingos (2012), [A Few Useful Things to Know about Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — 从数据泄漏、泛化、特征与目标函数等角度建立实验常识；是进入整门课前最值得先读的综述。[出处：`classification.md`]
- Antonio Torralba, Rob Fergus, William Freeman (2005), [Recognizing and Learning Object Categories](https://people.csail.mit.edu/torralba/shortCourseRLOC/index.html) — 从手工特征、匹配与分类走向视觉识别，补齐深度学习以前的历史背景。[出处：`classification.md`]
- Laurens van der Maaten, Geoffrey Hinton (2008), [Visualizing Data using t-SNE](https://www.jmlr.org/papers/v9/vandermaaten08a.html) — 理解讲义中的二维嵌入图，也提醒读者可视化只保留局部邻域而不等同于语义证明。[出处：`classification.md`, `understanding-cnn.md`]
- Alex Krizhevsky (2009), [Learning Multiple Layers of Features from Tiny Images / CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) — 课程作业的数据基准与 kNN、线性分类、CNN 对比的共同起点。[出处：`classification.md`]

## 2. 线性分类、间隔与概率输出

- Jason Weston, Chris Watkins (1999), [Support Vector Machines for Multi-Class Pattern Recognition](https://www.elen.ucl.ac.be/Proceedings/esann/esannpdf/es1999-461.pdf) — 讲义采用的多类 hinge-loss 形式；先掌握“正确类与每个错误类都保持间隔”。[出处：`linear-classify.md`]
- Ryan Rifkin, Aldebaro Klautau (2004), [In Defense of One-Vs-All Classification](https://www.jmlr.org/papers/v5/rifkin04a.html) — 对 one-vs-all 与更复杂多类 SVM 的实证比较，帮助判断理论表达力与实际效果的差异。[出处：`linear-classify.md`]
- Yichuan Tang (2013), [Deep Learning using Linear Support Vector Machines](https://arxiv.org/abs/1306.0239) — 比较神经网络顶层使用 L2-SVM 与 Softmax 的效果。[出处：`linear-classify.md`]
- Andrew Ng, [CS229 notes on Support Vector Machines](https://cs229.stanford.edu/notes2022fall/cs229-notes3.pdf) — 从最大间隔与对偶问题补齐 SVM 的严格推导。[出处：`linear-classify.md`]

## 3. 梯度、计算图与自动微分

- Atilim Gunes Baydin et al. (2018; cited draft 2015), [Automatic Differentiation in Machine Learning: a Survey](https://arxiv.org/abs/1502.05767) — 把数值微分、符号微分和自动微分放到同一框架中，是计算图与反向模式 AD 的总览。[出处：`optimization-2.md`]
- Erik Learned-Miller, [Vector, Matrix, and Tensor Derivatives](https://cs231n.stanford.edu/vecDerivs.pdf) — 面向反向传播的矩阵/向量求导速查与推导练习。[出处：`optimization-2.md`]
- Stephen Boyd, Lieven Vandenberghe (2004), [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) — 用凸性、次梯度和二阶结构理解为什么线性模型较易优化，而深网目标更复杂。[出处：`optimization-1.md`]
- David Goldberg (1991), [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) — 梯度检查失败时必须具备的浮点误差模型。[出处：`neural-networks-3.md`]

## 4. 神经网络的表达、激活与深度

- Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton (2012), [ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — ReLU、GPU 训练、数据增强和现代大规模 CNN 的标志性组合；后续架构线的起点。[出处：`neural-networks-1.md`, `convolutional-networks.md`]
- Kaiming He et al. (2015), [Delving Deep into Rectifiers](https://arxiv.org/abs/1502.01852) — PReLU 与针对 ReLU 的方差保持初始化（He initialization）。[出处：`neural-networks-1.md`, `neural-networks-2.md`]
- Ian Goodfellow et al. (2013), [Maxout Networks](https://arxiv.org/abs/1302.4389) — 把 ReLU/Leaky-ReLU 看作分段线性 maxout 单元的特例。[出处：`neural-networks-1.md`]
- George Cybenko (1989), [Approximation by Superpositions of a Sigmoidal Function](https://doi.org/10.1007/BF02551274) — 单隐层网络的通用逼近结果；说明“能表示”不等于“能高效训练或泛化”。[出处：`neural-networks-1.md`]
- Jimmy Ba, Rich Caruana (2014), [Do Deep Nets Really Need to be Deep?](https://arxiv.org/abs/1312.6184) — 通过蒸馏研究深模型函数能否由浅模型近似。[出处：`neural-networks-1.md`]
- Adriana Romero et al. (2015), [FitNets: Hints for Thin Deep Nets](https://arxiv.org/abs/1412.6550) — 用中间层 hint 训练更深更窄的学生网络。[出处：`neural-networks-1.md`]
- Anna Choromanska et al. (2015), [The Loss Surfaces of Multilayer Networks](https://arxiv.org/abs/1412.0233) — 讨论网络规模与非凸损失地形中低损失极小值的关系。[出处：`neural-networks-1.md`]
- Michael London, Michael Häusser (2005), [Dendritic Computation](https://physics.ucsd.edu/neurophysics/courses/physics_171/annurev.neuro.28.061604.135703.pdf) — 解释生物神经元远比课程中的点神经元模型复杂。[出处：`neural-networks-1.md`]
- Nicolas Brunel, Vincent Hakim, Magnus J. E. Richardson (2014), [Single neuron dynamics and computation](https://doi.org/10.1016/j.conb.2014.01.005) — 从单神经元动力学和计算视角补充生物神经元与课程点神经元的差异；属于背景阅读而非工程配方。[出处：`neural-networks-1.md`]

## 5. 初始化、归一化与正则化

- Xavier Glorot, Yoshua Bengio (2010), [Understanding the Difficulty of Training Deep Feedforward Neural Networks](https://proceedings.mlr.press/v9/glorot10a.html) — 从前向激活与反向梯度的方差解释 Xavier 初始化。[出处：`neural-networks-2.md`]
- Sergey Ioffe, Christian Szegedy (2015), [Batch Normalization](https://arxiv.org/abs/1502.03167) — 在网络内部标准化激活，缓解初始化与学习率敏感性。[出处：`neural-networks-2.md`, `convolutional-networks.md`]
- Hui Zou, Trevor Hastie (2005), [Regularization and Variable Selection via the Elastic Net](https://doi.org/10.1111/j.1467-9868.2005.00503.x) — 统一理解 L1 的稀疏性与 L2 的稳定性。[出处：`neural-networks-2.md`]
- Nitish Srivastava et al. (2014), [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.jmlr.org/papers/v15/srivastava14a.html) — 随机子网络训练及测试期近似集成的经典表述。[出处：`neural-networks-2.md`]
- Stefan Wager, Sida Wang, Percy Liang (2013), [Dropout Training as Adaptive Regularization](https://proceedings.neurips.cc/paper/2013/hash/38db3aed920cf82ab059bfccbd02be6a-Abstract.html) — 从自适应正则化角度解释 dropout。[出处：`neural-networks-2.md`]
- Li Wan et al. (2013), [Regularization of Neural Networks using DropConnect](https://proceedings.mlr.press/v28/wan13.html) — 随机丢弃权重连接而非激活，扩展“前向过程加噪声”的思路。[出处：`neural-networks-2.md`]
- Tomas Mikolov et al. (2013), [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546) — 讲义借其层次 Softmax/负采样讨论超大类别空间的近似计算。[出处：`neural-networks-2.md`]

## 6. 优化器、训练诊断与实验搜索

- Razvan Pascanu, Tomas Mikolov, Yoshua Bengio (2013), [On the Difficulty of Training Recurrent Neural Networks](https://arxiv.org/abs/1211.5063) — 梯度消失/爆炸与裁剪的几何解释。[出处：`neural-networks-3.md`]
- Ilya Sutskever (2013), [Training Recurrent Neural Networks](https://www.cs.utoronto.ca/~ilya/pubs/ilya_sutskever_phd_thesis.pdf) — 动量、初始化与序列模型训练的系统论述。[出处：`neural-networks-3.md`]
- Jeffrey Dean et al. (2012), [Large Scale Distributed Deep Networks](https://proceedings.neurips.cc/paper/2012/hash/6aca97005c68f1206823815f66102863-Abstract.html) — DistBelief、Downpour SGD 与分布式训练早期体系。[出处：`neural-networks-3.md`]
- Jascha Sohl-Dickstein, Ben Poole, Surya Ganguli (2014), [Fast Large-Scale Optimization by Unifying Stochastic Gradient and Quasi-Newton Methods](https://arxiv.org/abs/1311.2115) — SFO 尝试结合 SGD 与 L-BFGS 的优势。[出处：`neural-networks-3.md`]
- John Duchi, Elad Hazan, Yoram Singer (2011), [Adaptive Subgradient Methods for Online Learning and Stochastic Optimization](https://www.jmlr.org/papers/v12/duchi11a.html) — AdaGrad 及按历史梯度缩放坐标学习率。[出处：`neural-networks-3.md`]
- Tijmen Tieleman, Geoffrey Hinton (2012), [Lecture 6.5—RMSProp](https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf) — 用平方梯度指数移动平均避免 AdaGrad 学习率单调衰减。[出处：`neural-networks-3.md`]
- Diederik Kingma, Jimmy Ba (2015), [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) — 一阶矩、二阶矩与偏差修正构成课程默认优化器之一。[出处：`neural-networks-3.md`]
- Thomas M. Breuel (2014), [Unit Tests for Stochastic Optimization](https://arxiv.org/abs/1312.6055) — 用小而可控的实验隔离识别优化器问题。[出处：`neural-networks-3.md`]
- James Bergstra, Yoshua Bengio (2012), [Random Search for Hyper-Parameter Optimization](https://www.jmlr.org/papers/v13/bergstra12a.html) — 当只有少数超参数真正重要时，随机搜索比网格覆盖得更有效。[出处：`neural-networks-3.md`]
- Geoffrey Hinton, Oriol Vinyals, Jeff Dean (2015), [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — 把集成模型的软目标压回单模型，降低测试成本。[出处：`neural-networks-3.md` 中的 “Dark Knowledge”]
- Léon Bottou (2012), [Stochastic Gradient Descent Tricks](https://leon.bottou.org/publications/pdf/tricks-2012.pdf) — 学习率、打乱、缩放与实现细节的实战指南。[出处：`neural-networks-3.md`]
- Yann LeCun et al. (1998), [Efficient BackProp](https://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf) — 输入中心化、初始化与曲率条件对训练速度的影响。[出处：`neural-networks-3.md`]
- Yoshua Bengio (2012), [Practical Recommendations for Gradient-Based Training of Deep Architectures](https://arxiv.org/abs/1206.5533) — 把初始化、优化、正则化和调参经验串成完整训练清单。[出处：`neural-networks-3.md`]

## 7. CNN：从局部连接到残差网络

- Yann LeCun et al. (1998), [Gradient-Based Learning Applied to Document Recognition](https://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf) — LeNet、卷积权重共享与端到端手写识别。[出处：`convolutional-networks.md`]
- Min Lin, Qiang Chen, Shuicheng Yan (2014), [Network in Network](https://arxiv.org/abs/1312.4400) — 1×1 卷积与全局平均池化的重要来源。[出处：`convolutional-networks.md`]
- Fisher Yu, Vladlen Koltun (2016), [Multi-Scale Context Aggregation by Dilated Convolutions](https://arxiv.org/abs/1511.07122) — 用空洞卷积扩大感受野而不降低分辨率。[出处：`convolutional-networks.md`]
- Jost Tobias Springenberg et al. (2015), [Striving for Simplicity: The All Convolutional Net](https://arxiv.org/abs/1412.6806) — 以步幅卷积替代池化，并贡献 guided backprop 可视化。[出处：`convolutional-networks.md`, `understanding-cnn.md`]
- Matthew Zeiler, Rob Fergus (2014), [Visualizing and Understanding Convolutional Networks](https://arxiv.org/abs/1311.2901) — ZFNet、反卷积可视化与遮挡敏感性分析。[出处：`convolutional-networks.md`, `understanding-cnn.md`]
- Christian Szegedy et al. (2015), [Going Deeper with Convolutions](https://arxiv.org/abs/1409.4842) — GoogLeNet/Inception：多尺度分支与参数效率。[出处：`convolutional-networks.md`]
- Christian Szegedy et al. (2016), [Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning](https://arxiv.org/abs/1602.07261) — Inception 模块与残差连接的结合。[出处：`convolutional-networks.md`]
- Karen Simonyan, Andrew Zisserman (2015), [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) — 用统一的 3×3 卷积堆叠验证深度价值，形成 VGG 架构。[出处：`convolutional-networks.md`]
- Kaiming He et al. (2016), [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) — 以残差块和捷径连接训练极深网络。[出处：`convolutional-networks.md`]
- Kaiming He et al. (2016), [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027) — 分析恒等捷径与 pre-activation ResNet 的梯度通路。[出处：`convolutional-networks.md`]

## 8. 表征可视化、检测、反演与鲁棒性

- Ross Girshick et al. (2014), [Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation](https://arxiv.org/abs/1311.2524) — R-CNN 既展示迁移特征，也提供最大激活图像的解释方法。[出处：`understanding-cnn.md`]
- Christian Szegedy et al. (2014), [Intriguing Properties of Neural Networks](https://arxiv.org/abs/1312.6199) — 表征方向并不天然对应单个可解释神经元，并揭示对抗扰动。[出处：`understanding-cnn.md`]
- Karen Simonyan, Andrea Vedaldi, Andrew Zisserman (2014), [Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034) — 基于输入梯度的类别显著图与合成可视化。[出处：`understanding-cnn.md`]
- Aravindh Mahendran, Andrea Vedaldi (2015), [Understanding Deep Image Representations by Inverting Them](https://arxiv.org/abs/1412.0035) — 通过重建判断各层保留了哪些图像信息。[出处：`understanding-cnn.md`]
- Jonathan Long, Ning Zhang, Trevor Darrell (2014), [Do ConvNets Learn Correspondence?](https://proceedings.neurips.cc/paper/2014/hash/4d6b3e38b952600251ee92fe603170ff-Abstract.html) — 检验深层表征是否保留跨实例的局部对应关系。[出处：`understanding-cnn.md`]
- Olga Russakovsky et al. (2015), [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575) — 数据集、任务、评价指标与 2010–2014 视觉识别进展的权威总结。[出处：`understanding-cnn.md`]
- Ian Goodfellow, Jonathon Shlens, Christian Szegedy (2015), [Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572) — 线性解释、FGSM 与对抗训练的经典起点。[出处：`understanding-cnn.md`]

## 9. 迁移学习

- Ali Sharif Razavian et al. (2014), [CNN Features off-the-shelf: an Astounding Baseline for Recognition](https://arxiv.org/abs/1403.6382) — 固定 ImageNet 特征加简单分类器即可跨任务取得强基线。[出处：`transfer-learning.md`]
- Jeff Donahue et al. (2014), [DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition](https://arxiv.org/abs/1310.1531) — 系统验证深层激活作为通用视觉特征。[出处：`transfer-learning.md`]
- Jason Yosinski et al. (2014), [How Transferable Are Features in Deep Neural Networks?](https://arxiv.org/abs/1411.1792) — 分析层深、任务距离和共适应如何决定冻结或微调策略。[出处：`transfer-learning.md`]

## 教材、概念讲义与实践资源

这些资源同样由讲义明确链接，但不属于上面的论文主线。

### 教材与补充讲义

- Ian Goodfellow, Yoshua Bengio, Aaron Courville, [Deep Learning](https://www.deeplearningbook.org/) — 尤其第 6 章多层感知机。[出处：`neural-networks-1.md`]
- Michael Nielsen, [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) — 通用逼近与反向传播的直觉化解释。[出处：`neural-networks-1.md`]
- Andrew Ng, [CS229 notes on PCA](https://cs229.stanford.edu/notes2022fall/cs229-notes10.pdf) — 高维数据降维背景。[出处：`classification.md`]
- CS231n, [Minimal Neural Network case-study notebook](https://cs.stanford.edu/people/karpathy/cs231nfiles/minimal_net.html) — 与 `neural-networks-case-study.md` 配套的完整代码。

### 数学概念入口

- [p-norm](https://planetmath.org/vectorpnorm)、[PCA](https://en.wikipedia.org/wiki/Principal_component_analysis)、[Neighbourhood Components Analysis](https://en.wikipedia.org/wiki/Neighbourhood_components_analysis)、[Random Projection](https://scikit-learn.org/stable/modules/random_projection.html) — 距离与降维。[出处：`classification.md`]
- [Numerical differentiation](https://en.wikipedia.org/wiki/Numerical_differentiation)、[subgradient](https://en.wikipedia.org/wiki/Subderivative) — 数值梯度检查与不可微点。[出处：`optimization-1.md`, `neural-networks-3.md`]
- [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)、[Hessian](https://en.wikipedia.org/wiki/Hessian_matrix)、[L-BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS) — 从一阶方法走向曲率信息。[出处：`neural-networks-3.md`]

### 数据、代码与工具

- [FLANN](https://github.com/flann-lib/flann) — 近似最近邻检索。[出处：`classification.md`]
- [ConvNetJS demos](https://cs.stanford.edu/people/karpathy/convnetjs/)、[CNN feature t-SNE explorer](https://cs.stanford.edu/people/karpathy/cnnembed/) — 浏览器内的决策边界和表征可视化。[出处：`neural-networks-1.md`, `understanding-cnn.md`]
- [BLAS](https://www.netlib.org/blas/) — `im2col + GEMM` 卷积实现背后的矩阵乘法接口。[出处：`convolutional-networks.md`]
- [Caffe Model Zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo)、[Caffe](https://caffe.berkeleyvision.org/)、[Net Surgery](https://github.com/BVLC/caffe/blob/master/examples/net_surgery.ipynb) — 预训练模型、框架与网络参数修改示例。[出处：`convolutional-networks.md`, `transfer-learning.md`]
- [convnet-benchmarks](https://github.com/soumith/convnet-benchmarks)、[Torch ResNets](https://torch.ch/blog/2016/02/04/resnets.html) — 旧版框架中的卷积性能与 ResNet 复现记录。[出处：`convolutional-networks.md`]
- [Spearmint](https://github.com/JasperSnoek/spearmint)、[SMAC](https://www.cs.ubc.ca/labs/algorithms/Projects/SMAC/)、[Hyperopt](https://hyperopt.github.io/hyperopt/) — 贝叶斯/序贯超参数优化工具。[出处：`neural-networks-3.md`]
- [Loss Functions Tumblr](https://lossfunctions.tumblr.com/) — 训练曲线异常形态的轻量案例库。[出处：`neural-networks-3.md`]

## Slides 补充：视觉历史、数据集与基础模型

以下条目来自 Spring 2026 slides；与前文 notes 已列出的论文不重复。每条保留幻灯片中的原始出处，便于从课程语境回看。

- David H. Hubel, Torsten N. Wiesel (1959), [Receptive fields of single neurones in the cat's striate cortex](https://doi.org/10.1113/jphysiol.1959.sp006308) — 发现视觉皮层方向选择性和局部感受野，解释卷积局部连接的生物学启发。（来源：`slides/lecture_1_part_1.pdf`）
- Lawrence G. Roberts (1963), [Machine Perception of Three-Dimensional Solids](https://dspace.mit.edu/handle/1721.1/11589) — 早期从二维图像推断三维几何结构的计算机视觉工作。（来源：`slides/lecture_1_part_1.pdf`）
- Martin A. Fischler, Robert A. Elschlager (1973), [The Representation and Matching of Pictorial Structures](https://doi.org/10.1109/T-C.1973.223602) — 用部件与结构关系表示目标，是后来 pictorial-structure 模型的源头。（来源：`slides/lecture_1_part_1.pdf`）
- John Canny (1986), [A Computational Approach to Edge Detection](https://doi.org/10.1109/TPAMI.1986.4767851) — 以检测率、定位和单响应为目标设计经典 Canny 边缘检测器。（来源：`slides/lecture_1_part_1.pdf`, `slides/lecture_2.pdf`）
- David G. Lowe (2004), [Distinctive Image Features from Scale-Invariant Keypoints](https://doi.org/10.1023/B:VISI.0000029664.99615.94) — SIFT 的尺度不变局部特征，为深度特征之前的匹配范式。（来源：`slides/lecture_1_part_1.pdf`）
- Paul Viola, Michael Jones (2001), [Rapid Object Detection using a Boosted Cascade of Simple Features](https://doi.org/10.1023/A:1010933404324) — Haar 特征、AdaBoost 和级联分类器构成实时人脸检测系统。（来源：`slides/lecture_1_part_1.pdf`）
- Kunihiko Fukushima (1980), [Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position](https://doi.org/10.1007/BF00344251) — 早期层级视觉网络，包含类似简单/复杂细胞的层级不变性。（来源：`slides/lecture_1_part_1.pdf`）
- Geoffrey E. Hinton, Ruslan R. Salakhutdinov (2006), [Reducing the Dimensionality of Data with Neural Networks](https://doi.org/10.1126/science.1127647) — 用深层自编码器学习低维表示，推动 2000 年代深度学习复兴。（来源：`slides/lecture_1_part_1.pdf`）
- Yoshua Bengio et al. (2007), [Greedy Layer-Wise Training of Deep Networks](https://doi.org/10.1145/1273496.1273555) — 逐层无监督预训练缓解深网络优化困难。（来源：`slides/lecture_1_part_1.pdf`）
- Jia Deng et al. (2009), [ImageNet: A Large-Scale Hierarchical Image Database](https://doi.org/10.1109/CVPR.2009.5206848) — 大规模带层级标签的数据集，成为视觉分类规模化的基础。（来源：`slides/lecture_1_part_1.pdf`, `slides/lecture_2.pdf`）
- Mark Everingham et al. (2010), [The Pascal Visual Object Classes (VOC) Challenge](https://doi.org/10.1007/s11263-009-0275-4) — 统一检测、分割和分类评测，推动视觉基准标准化。（来源：`slides/lecture_1_part_1.pdf`）
- Ranjay Krishna et al. (2017), [Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations](https://arxiv.org/abs/1602.07332) — 提供区域、关系和问答标注，把视觉识别连接到语言。（来源：`slides/lecture_1_part_1.pdf`）
- David Silver et al. (2016), [Mastering the game of Go with deep neural networks and tree search](https://doi.org/10.1038/nature16961) — 深度网络与蒙特卡洛树搜索结合的 AlphaGo 范例。（来源：`slides/lecture_1_part_1.pdf`）
- David Silver et al. (2017), [Mastering the Game of Go without Human Knowledge](https://doi.org/10.1038/nature24270) — AlphaZero 展示自博弈和通用规划的扩展能力。（来源：`slides/lecture_1_part_1.pdf`）

## Slides 补充：优化、归一化与序列模型

- Yann N. Dauphin et al. (2014), [Identifying and Attacking the Saddle Point Problem in High-Dimensional Non-Convex Optimization](https://arxiv.org/abs/1406.2572) — 说明高维非凸训练常受鞍点而非局部极小值阻碍。（来源：`slides/lecture_3.pdf`）
- Ilya Sutskever et al. (2013), [On the importance of initialization and momentum in deep learning](https://proceedings.mlr.press/v28/sutskever13.html) — 系统研究初始化和动量对深网络 SGD 的影响。（来源：`slides/lecture_3.pdf`）
- Yuxin Wu, Kaiming He (2018), [Group Normalization](https://arxiv.org/abs/1803.08494) — 不依赖 batch size 的通道分组归一化，适合检测和小批量训练。（来源：`slides/lecture_6.pdf`）
- Sanghyun DeVries, Graham W. Taylor (2017), [Improved Regularization of Convolutional Neural Networks with Cutout](https://arxiv.org/abs/1708.04552) — 随机遮挡输入区域，作为数据增强和正则化。（来源：`slides/lecture_6.pdf`）
- Ilya Loshchilov, Frank Hutter (2017), [SGDR: Stochastic Gradient Descent with Warm Restarts](https://arxiv.org/abs/1608.03983) — 周期性重启余弦学习率，改善训练后期探索。（来源：`slides/lecture_3.pdf`）
- Priya Goyal et al. (2017), [Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour](https://arxiv.org/abs/1706.02677) — 线性学习率缩放和 warmup 支撑大 batch 训练。（来源：`slides/lecture_3.pdf`）
- James Martens, Roger Grosse (2015), [Optimizing Neural Networks with Kronecker-factored Approximate Curvature](https://arxiv.org/abs/1503.05671) — K-FAC 用 Kronecker 结构近似二阶曲率，降低自然梯度成本。（来源：`slides/lecture_3.pdf`）
- Jianlin Su et al. (2021), [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) — 用旋转位置编码把相对位置信息注入注意力。（来源：`slides/lecture_8.pdf`）
- Tri Dao et al. (2022), [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) — 通过 tiling 减少显存读写，在不近似注意力的情况下提速。（来源：`slides/lecture_8.pdf`）
- Alexey Baevski, Michael Auli (2019), [Adaptive Input Representations for Neural Language Modeling](https://arxiv.org/abs/1809.10853) — 为高频/低频词分配不同维度，降低大词表开销。（来源：`slides/lecture_8.pdf`, `slides/lecture_9.pdf`）
- Biao Zhang, Rico Sennrich (2019), [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467) — 去掉均值中心化的简化归一化，成为 RMSNorm 的标准来源。（来源：`slides/lecture_8.pdf`, `slides/lecture_9.pdf`）
- Noam Shazeer (2020), [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) — 以门控线性单元替代 FFN 激活，提高 Transformer 表达效率。（来源：`slides/lecture_8.pdf`, `slides/lecture_9.pdf`）
- Noam Shazeer et al. (2017), [Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) — 稀疏路由让参数规模扩展而计算量保持可控。（来源：`slides/lecture_8.pdf`, `slides/lecture_9.pdf`）
- Rewon Child et al. (2019), [Generating Long Sequences with Sparse Transformers](https://arxiv.org/abs/1904.10509) — 用稀疏注意力扩展长序列生成。（来源：`slides/lecture_3.pdf`）
- Christoph Feichtenhofer et al. (2019), [SlowFast Networks for Video Recognition](https://arxiv.org/abs/1812.03982) — 快速通道捕捉运动、慢速通道捕捉语义，代表视频双时间尺度建模。（来源：`slides/lecture_3.pdf`）

## Slides 补充：自监督视觉、检测与可解释性

- Carl Doersch, Abhinav Gupta, Alexei A. Efros (2015), [Unsupervised Visual Representation Learning by Context Prediction](https://arxiv.org/abs/1505.05192) — 以相对 patch 位置作为伪标签学习视觉表征。（来源：`slides/lecture_12.pdf`）
- Mehdi Noroozi, Paolo Favaro (2016), [Unsupervised Learning of Visual Representations by Solving Jigsaw Puzzles](https://arxiv.org/abs/1603.09246) — 用拼图排列任务迫使网络理解物体结构。（来源：`slides/lecture_12.pdf`）
- Deepak Pathak et al. (2016), [Context Encoders: Feature Learning by Inpainting](https://arxiv.org/abs/1604.07379) — 通过图像补全获得语义和上下文表征。（来源：`slides/lecture_12.pdf`）
- Spyros Gidaris, Praveer Singh, Nikos Komodakis (2018), [Unsupervised Representation Learning by Predicting Image Rotations](https://arxiv.org/abs/1803.07728) — 旋转预测作为简单有效的预文本任务。（来源：`slides/lecture_12.pdf`）
- Kaiming He et al. (2022), [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) — 高比例遮挡、非对称 encoder–decoder 让视觉 MAE 高效扩展。（来源：`slides/lecture_12.pdf`）
- Aaron van den Oord, Yazhe Li, Oriol Vinyals (2018), [Representation Learning with Contrastive Predictive Coding](https://arxiv.org/abs/1807.03748) — InfoNCE 与预测未来 latent 的对比学习框架。（来源：`slides/lecture_12.pdf`, `slides/lecture_13.pdf`）
- Ben Poole et al. (2019), [On Variational Bounds of Mutual Information](https://arxiv.org/abs/1905.06922) — 解释 InfoNCE 等互信息下界的估计偏差和方差。（来源：`slides/lecture_12.pdf`）
- Ting Chen et al. (2020), [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709) — SimCLR 以强增强、大 batch 和 projection head 建立对比学习基线。（来源：`slides/lecture_13.pdf`）
- Kaiming He et al. (2020), [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722) — MoCo 用动量编码器和队列扩展负样本。（来源：`slides/lecture_13.pdf`）
- Mathilde Caron et al. (2021), [Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294) — DINO 展示无标签 ViT 的语义分割和邻域结构。（来源：`slides/lecture_13.pdf`）
- Maxime Oquab et al. (2023), [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193) — 用大规模数据和蒸馏训练通用视觉特征。（来源：`slides/lecture_13.pdf`）
- Timothée Darcet et al. (2024), [Vision Transformers Need Registers](https://arxiv.org/abs/2309.16588) — 解释 ViT 中异常高范数 token，并用 registers 改善特征图质量。（来源：`slides/lecture_13.pdf`）
- Jonathan Long, Evan Shelhamer, Trevor Darrell (2015), [Fully Convolutional Networks for Semantic Segmentation](https://arxiv.org/abs/1411.4038) — 将分类 CNN 改造成 dense prediction 网络。（来源：`slides/lecture_9.pdf`）
- Wei Liu et al. (2016), [SSD: Single Shot MultiBox Detector](https://arxiv.org/abs/1512.02325) — 多尺度 default boxes 的单阶段检测器。（来源：`slides/lecture_9.pdf`）
- Tsung-Yi Lin et al. (2017), [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002) — 降低易分类负样本权重，解决 dense detector 类别不平衡。（来源：`slides/lecture_9.pdf`）
- Nicolas Carion et al. (2020), [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) — DETR 用 set prediction 和 bipartite matching 去掉手工 NMS/anchor。（来源：`slides/lecture_9.pdf`）
- Bolei Zhou et al. (2016), [Learning Deep Features for Discriminative Localization](https://arxiv.org/abs/1512.04150) — CAM 把分类器权重投影回图像定位判别区域。（来源：`slides/lecture_9.pdf`）
- Ramprasaath R. Selvaraju et al. (2017), [Grad-CAM](https://arxiv.org/abs/1610.02391) — 用梯度和特征图生成类别定位解释。（来源：`slides/lecture_9.pdf`）
- Kirillov et al. (2023), [Segment Anything](https://arxiv.org/abs/2304.02643) — 以 promptable foundation model 将分割泛化到开放图像分布。（来源：`slides/lecture_1_part_1.pdf`）
- Andrej Karpathy, Justin Johnson, Li Fei-Fei (2016), [Visualizing and Understanding Recurrent Networks](https://arxiv.org/abs/1506.02078) — 用可视化分析字符级 RNN 的记忆单元和语法行为。（来源：`slides/lecture_7.pdf`）
- Aishwarya Agrawal et al. (2015), [VQA: Visual Question Answering](https://arxiv.org/abs/1505.00468) — 以图像和自然语言问题构成多模态问答任务。（来源：`slides/lecture_7.pdf`）
- Yuke Zhu et al. (2016), [Visual7W](https://arxiv.org/abs/1511.03416) — 将问答答案 grounding 到图像区域。（来源：`slides/lecture_7.pdf`）
- Abhishek Das et al. (2017), [Visual Dialog](https://arxiv.org/abs/1611.08669) — 将视觉问答扩展到多轮对话上下文。（来源：`slides/lecture_7.pdf`）

## Slides 补充：生成模型、视频、多模态与 3D

- Jascha Sohl-Dickstein et al. (2015), [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://arxiv.org/abs/1503.03585) — 首次系统提出 diffusion forward/reverse 生成框架。（来源：`slides/lecture_14.pdf`）
- Yang Song, Stefano Ermon (2019), [Generative Modeling by Estimating Gradients of the Data Distribution](https://arxiv.org/abs/1907.05600) — score matching 与 Langevin dynamics 的生成模型。（来源：`slides/lecture_14.pdf`）
- Jonathan Ho et al. (2020), [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) — 将扩散训练转化为噪声预测，成为 DDPM 基线。（来源：`slides/lecture_14.pdf`）
- Jiaming Song, Chenlin Meng, Stefano Ermon (2021), [Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502) — 允许非马尔可夫、少步数采样。（来源：`slides/lecture_14.pdf`）
- Bowen Song et al. (2021), [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456) — 用 SDE 统一 score-based 生成和采样器。（来源：`slides/lecture_14.pdf`）
- Ting Chen et al. (2021), [Is Space-Time Attention All You Need for Video Understanding?](https://arxiv.org/abs/2102.05095) — TimeSformer 将时空注意力用于视频建模。（来源：`slides/lecture_10.pdf`）
- Ze Liu et al. (2022), [Video Swin Transformer](https://arxiv.org/abs/2106.13230) — 局部移位窗口把 Swin 扩展到视频时空。（来源：`slides/lecture_10.pdf`）
- Anurag Arnab et al. (2021), [ViViT: A Video Vision Transformer](https://arxiv.org/abs/2103.15691) — 研究纯 Transformer 的视频 patch 编码和因子化注意力。（来源：`slides/lecture_10.pdf`）
- Haoqi Fan et al. (2021), [Multiscale Vision Transformers](https://arxiv.org/abs/2104.11227) — 在时空层级中逐步改变 token 分辨率和通道规模。（来源：`slides/lecture_10.pdf`）
- João Carreira, Andrew Zisserman (2017), [Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset](https://arxiv.org/abs/1705.07750) — 大规模 Kinetics 视频数据与 I3D 基线。（来源：`slides/lecture_10.pdf`）
- Tero Karras et al. (2018), [Progressive Growing of GANs for Improved Quality, Stability, and Variation](https://arxiv.org/abs/1710.10196) — 逐级增加分辨率稳定高分辨率 GAN 训练。（来源：`slides/lecture_1_part_1.pdf`, `slides/lecture_14.pdf`）
- Aditya Ramesh et al. (2021), [Zero-Shot Text-to-Image Generation](https://arxiv.org/abs/2102.12092) — DALL·E 以离散图像 token 和 Transformer 做文本到图像生成。（来源：`slides/lecture_1_part_1.pdf`, `slides/lecture_14.pdf`）
- William Peebles, Saining Xie (2023), [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) — DiT 用 Transformer 替换 U-Net，展示扩散模型 scaling law。（来源：`slides/lecture_1_part_1.pdf`, `slides/lecture_14.pdf`）
- Ji et al. (2013), [3D Convolutional Neural Networks for Human Action Recognition](https://doi.org/10.1109/TPAMI.2012.59) — 将卷积从空间扩展到时间维度。（来源：`slides/lecture_10.pdf`）
- Andrej Karpathy et al. (2014), [Large-scale Video Classification with Convolutional Neural Networks](https://arxiv.org/abs/1406.2199) — 以大规模弱标注视频训练时空卷积模型。（来源：`slides/lecture_10.pdf`）
- Rajbhandari et al. (2020), [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) — 分片 optimizer state、梯度和参数，降低超大模型显存。（来源：`slides/lecture_11.pdf`）
- Aakanksha Chowdhery et al. (2022), [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311) — 展示大规模语言模型的参数、数据和计算扩展。（来源：`slides/lecture_11.pdf`）
- Llama Team (2024), [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — 开放权重 LLM 的数据、训练和指令微调报告。（来源：`slides/lecture_11.pdf`）
- Yanping Huang et al. (2019), [GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism](https://arxiv.org/abs/1811.06965) — 用流水线并行和 micro-batch 训练巨型网络。（来源：`slides/lecture_11.pdf`）
- OpenAI (2023), [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) — slides 用作现代大模型能力与评测的参照。（来源：`slides/lecture_11.pdf`, `slides/lecture_16.pdf`）
- Christopher Choy et al. (2016), [3D-R2N2](https://arxiv.org/abs/1604.00449) — 用 recurrent 3D occupancy 预测融合多视图。（来源：`slides/lecture_1_part_2.pdf`, `slides/lecture_15.pdf`）
- Charles R. Qi et al. (2017), [PointNet](https://arxiv.org/abs/1612.00593) — 直接对无序点集使用对称函数建模。（来源：`slides/lecture_15.pdf`）
- Charles R. Qi et al. (2017), [PointNet++](https://arxiv.org/abs/1706.02413) — 在局部邻域中递归抽取层级点云特征。（来源：`slides/lecture_15.pdf`）
- Shichen Liu et al. (2019), [DeepSDF](https://arxiv.org/abs/1901.05103) — 用连续隐式函数表示三维形状。（来源：`slides/lecture_15.pdf`）
- Ben Mildenhall et al. (2020), [NeRF](https://arxiv.org/abs/2003.08934) — 用坐标 MLP 和体渲染合成新视角。（来源：`slides/lecture_15.pdf`）
- Keunhong Park et al. (2021), [Nerfies](https://arxiv.org/abs/2011.12948) — 将 NeRF 扩展到非刚体动态场景。（来源：`slides/lecture_15.pdf`）
- Matthew Tancik et al. (2022), [Block-NeRF](https://arxiv.org/abs/2202.05263) — 以块化 NeRF 扩展到城市级大场景。（来源：`slides/lecture_15.pdf`）
- Jonathan T. Barron et al. (2022), [Mip-NeRF 360](https://arxiv.org/abs/2111.12077) — 处理无界场景和尺度抗混叠问题。（来源：`slides/lecture_15.pdf`）
- Lihe Yang et al. (2024), [Depth Anything](https://arxiv.org/abs/2401.10891) — 以大规模无标签图像学习通用单目深度。（来源：`slides/lecture_15.pdf`）

