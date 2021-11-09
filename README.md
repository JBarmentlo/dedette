# INSTAL CONDA ON LINUX:

```
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
cd ~/Downloads && chmod +x Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh
export PATH=/mnt/nfs/homes/<YOUR USERNAME>/miniconda3/bin:$PATH && conda init <YOUR SHELL NAME>
```
restart your terminal
```
conda activate base
conda install -y jupyter numpy pandas
```