# Automatic Feeding and AI Inspection System

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
