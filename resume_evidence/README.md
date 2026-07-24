# 简历项目证据索引

对应简历项目：**阶梯轴自动上料与检测设备结构设计**

## 简历表述与仓库证据

| 简历内容 | 直接证据 |
|---|---|
| 60 × 20 mm阶梯轴、振动盘、直线轨道 | `docs/parameters.csv`、`models/automatic_feeding_inspection.step` |
| 双气缸分料、V形定位和分流机构 | `control/sequence.md`、`drawings/V形定位座_V_Block_Locator.pdf`、`drawings/分料安装板_Separator_Mounting_Plate.pdf` |
| 0.5 MPa气缸选型 | `docs/preliminary_calculations.md`、`docs/feeding_track_and_adjustment_design.md` |
| 可调气缸安装座、限位和检测支架 | `docs/feeding_track_and_adjustment_design.md`、`models/automatic_feeding_inspection.py` |
| 主要机构建模、装配、工程图与BOM | `models/automatic_feeding_inspection.step`、`drawings/二维工程图册_2D_Engineering_Drawings.pdf`、`docs/BOM.csv` |
| 推料、分流及防护结构复核 | `validation/`、本目录的最新装配体复核视图、`project-validation-summary.md` |

## 本次几何复核

- STEP SHA256：`071f014049536518183d65d9e7de3739b73534262586aff83b1db8708f279486`
- 类型：装配体
- 装配节点：180
- 叶节点/实体：179
- 面数量：924
- 包围盒：`1480 × 862.5 × 1324.5 mm`
- 复核工具：CAD几何引用检查与ISO快照

## 使用边界

仓库能够证明送料、分料、定位、检测工位和防护结构的几何设计，以及气缸推力量级和动作顺序。连续运行次数、实际节拍、检测准确率和测量误差没有实体设备记录时，不作为实测结果。
