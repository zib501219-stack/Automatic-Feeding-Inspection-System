# Automatic Feeding and AI Inspection System

> 简历项目证据入口：[`resume_evidence/README.md`](resume_evidence/README.md)

面向 60 × 20 mm、约 0.12 kg 阶梯轴的自动定向上料、单件分离、V形定位、视觉与激光尺寸检测、OK/NG 分流工作站。设计节拍 **12 件/分钟（5 s/循环）**。

## Modules

- 振动盘与离散螺旋轨道、直线送料轨道
- 双气缸分料、移载滑台、V形定位和到位传感
- 工业相机 + 远心镜头 + 背光源 + 激光测径
- AI 缺陷分类技术路线、OK/NG 气动排料
- 气动阀岛、电控柜、HMI、安全门联锁与防护

## Files

- `models/automatic_feeding_inspection.py`: editable parametric source
- `models/automatic_feeding_inspection.step`: detailed STEP assembly
- `models/automatic_feeding_inspection.glb`: browser preview
- `docs/`: requirements, calculations, BOM, manufacturing and validation
- `validation/`: ISO/opposite/front/top verification views

Actual vision accuracy and measured takt require the final camera, dataset, PLC program and physical machine. They are not fabricated in this repository.

## 二维工程图 / 2D engineering drawings

- `drawings/总装图_Overall_Assembly.*`：A2 总装图，直接由详细 STEP 装配体生成三视图、明细栏与装配技术要求。
- `drawings/直线送料轨道_Linear_Feeder_Track.*`、`V形定位座_V_Block_Locator.*`、`分料安装板_Separator_Mounting_Plate.*`：A3 关键零件图。
- `drawings/二维工程图册_2D_Engineering_Drawings.pdf`：四页合订图册。

标注采用中国大陆简体中文与 GB/T 常用机械制图术语，英文为辅助说明；每张图同时提供 DXF、PDF、PNG 和可重生成 Python 源文件。
