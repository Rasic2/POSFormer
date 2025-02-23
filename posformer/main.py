from ase.io import read, write
from ase.optimize import BFGS
from m3gnet.models import M3GNet, M3GNetCalculator, Potential

from posformer.structure import traj2dump

pretrained_model = M3GNet.load()  # 强制重新下载

# 初始化计算器（自动下载预训练模型）
calc = M3GNetCalculator(potential=Potential(pretrained_model))  # 可选参数 device="cuda" 启用GPU

# 构建 ASE 原子结构
atoms = read("POSCAR")
atoms.calc = calc
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.05)  # 设置力收敛阈值

write("CONTCAR", atoms)

traj2dump()
