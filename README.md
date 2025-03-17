# 环境安装

## 1. 创建独立环境（Python 3.9）

```bash
conda create -n posformer python=3.9
conda activate posformer
```

## 2. 安装基础框架

```bash
conda install -c apple tensorflow-deps==2.10.0
pip install tensorflow-macos==2.10.0 keras==2.10.0 tensorflow-metal==0.6.0
conda install -c pytorch pytorch==1.12.1
```

## 3. 安装图神经网络库

```bash
pip install dgl==0.9.1 -f https://data.dgl.ai/wheels/macos-12.0-arm64/repo.html
```

## 4. 安装材料科学库（需手动处理依赖）

```bash
pip install matgl m3gnet --no-deps
pip install pymatgen==2023.7.20
```