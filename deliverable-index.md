# 交付物索引

- `README.md`：GitHub项目首页、核心结果和验证边界
- `models/automatic_feeding_inspection.py|step|glb`：参数化整机源码、STEP与浏览模型
- `native_sources/solidworks/`：4个基础 SolidWorks 2023 原生零件
- `native_sources/enhanced_key_parts/`：第一批4个增强关键件
- `native_sources/production_parts_v2/`：第二批分料闸板、硬限位支架、传感器支架和相机横梁安装座，含STEP、DXF、A3 PDF、截图、BOM与生成源码
- `native_sources/production_parts_v3/`：第三批导轨压板、气缸叉头、阀岛板和背光支架
- `native_sources/engineering_package/`：受控零件号、工程图和爆炸参考装配
- `native_sources/engineering_analysis/`：气缸推力、节拍、间隙和定位配合校核
- `native_sources/motion_validation/`：五秒循环、0.1秒采样和互锁矩阵
- `native_sources/collision_validation/`：实体交叠、优先级分类和整改工作表
- `native_sources/structural_analysis/`：加厚后轨道底板简化梁有限元
- `control/`：34点I/O、13步状态机、报警矩阵、HMI规范和结构化文本参考程序
- `drawings/`：整机总装图及第一批关键零件图
- `docs/`：参数、假设、BOM、制造和验证资料
- `docs/procurement_interface_freeze.*`：采购询价接口、性能要求和下单前复核项
- `resume_evidence/README.md`及`装配体复核视图_*.png`：简历证据入口
- `Automatic-Feeding-Inspection-System_Engineering_Project_Book.pdf`：工程项目书

## Digital acceptance closure

- `validation/digital_acceptance/README.md`: final digital acceptance summary
- `validation/digital_acceptance/acceptance_matrix.csv`: itemized completion status
- `validation/digital_acceptance/controlled_part_drawing_register.csv`: 12-part STEP/DXF/PDF register
- `validation/digital_acceptance/p1_digital_closure.csv`: named P1 disposition closure
- `validation/digital_acceptance/procurement_technical_release.csv`: technical procurement release
- `validation/digital_acceptance/controller_and_motion_test.json`: repeatable control/motion checks
- `validation/digital_acceptance/physical_validation_plan.md`: only intentionally pending stage
