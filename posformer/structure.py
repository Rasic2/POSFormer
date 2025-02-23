from ase.io.trajectory import Trajectory


def traj2dump(traj_file: str = "opt.traj", dump_file: str = "opt.dump"):
    # 读取轨迹文件
    traj = Trajectory(traj_file)

    # 收集所有元素类型并生成映射
    elements = set()
    for atoms in traj:
        elements.update(atoms.get_chemical_symbols())
    element_to_type = {elem: i + 1 for i, elem in enumerate(sorted(elements))}

    # 写入 LAMMPS dump 文件
    with open(dump_file, 'w') as f:
        for step, atoms in enumerate(traj):
            f.write(f"ITEM: TIMESTEP\n{step}\n")
            f.write(f"ITEM: NUMBER OF ATOMS\n{len(atoms)}\n")

            # 处理盒子
            cell = atoms.cell
            if cell.orthorhombic:
                f.write("ITEM: BOX BOUNDS pp pp pp\n")
                for i in range(3):
                    f.write(f"0.0 {cell.lengths()[i]:.6f}\n")
            else:
                xy, xz, yz = cell[1][0], cell[2][0], cell[2][1]
                f.write("ITEM: BOX BOUNDS xy xz yz pp pp pp\n")
                f.write(f"0.0 {cell[0][0]:.6f} {xy:.6f}\n")
                f.write(f"0.0 {cell[1][1]:.6f} {xz:.6f}\n")
                f.write(f"0.0 {cell[2][2]:.6f} {yz:.6f}\n")

            # 写入原子信息
            f.write("ITEM: ATOMS id type x y z\n")
            for i, atom in enumerate(atoms):
                elem = atom.symbol
                atom_type = element_to_type[elem]
                x, y, z = atom.position
                f.write(f"{i + 1} {atom_type} {x:.6f} {y:.6f} {z:.6f}\n")
