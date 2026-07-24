# Native CAD source files

This folder contains genuine SolidWorks 2023 part files created from the portfolio design baseline, plus neutral STEP copies for NX and other CAD systems.

Design basis: cylindrical workpiece diameter 20 mm, length 60 mm, target rate 12 parts/min, 0.5 MPa pneumatic supply.

Files:

- `linear_feeder_track.SLDPRT`
- `separator_cylinder_mount.SLDPRT`
- `v_locator_base.SLDPRT`
- `transfer_cylinder_bracket.SLDPRT`

The models contain editable sketches and extrusion features. Existing editable DXF drawings remain under `drawings/`.

NX note: the STEP files can be opened and saved as NX `.prt`. Native NX batch feature generation was not committed because the local NX feature-modeling license was unavailable during this build.

## Enhanced key parts

`enhanced_key_parts/` contains the second-pass engineering models:

- linear feeder track with raised guide rails, recessed channel and counterbored mounting holes;
- separator-cylinder L bracket with upright plate, cylinder bore and mounting features;
- real V-locator geometry for the diameter 20 mm cylindrical workpiece;
- transfer-cylinder L bracket with upright bore and counterbored base;
- one reviewed isometric PNG for every enhanced part;
- editable CadQuery source used to regenerate the STEP files.

The original `.SLDPRT` files are retained as native sketch/extrusion examples. The enhanced STEP files are the more detailed geometry baseline.

## Engineering package

`engineering_package/` adds controlled part numbers `FI-001` to `FI-004`, BOM, four DXF drawings, four A3 PDF sheets, an exploded reference assembly STEP, placement data, a reviewed assembly snapshot and a validation note.

The reference assembly is an exploded key-part review layout. Use the repository's main detailed machine assembly for system-level arrangement and takt context.

## Engineering analysis

`engineering_analysis/` adds traceable pneumatic-force checks for the 16 mm and 20 mm cylinders, force safety factors, a five-second cycle allocation, feeder clearance recommendations, locator fits and a verification matrix separating calculated targets from physical commissioning.

## Sequence validation

`motion_validation/` contains the five-second cycle timeline, 0.1-second state samples, command interlock matrix and reviewed timeline chart. It documents the conditions for part release, transfer, inspection and return without presenting the sequence as a commissioned PLC result.

## Solid overlap screening

`collision_validation/` contains the per-solid bounding boxes and exact common-volume results from the detailed machine STEP. The scan found many intersecting pairs, so the detailed STEP is **not released as a collision-free manufacturing assembly**. The list mixes expected fitting interfaces with overlaps inherited from visual construction geometry and must be classified in a named native assembly.

`overlap_classification_worklist.csv` adds P1/P2/P3 priorities, inferred mechanism zones, likely geometry categories, required actions and an open/closed review field. These are screening inferences; final acceptance still requires named components and section-view review.

## Structural analysis

`structural_analysis/` contains a reproducible 24-element Euler-Bernoulli beam FE check for the 600 mm feeder base under a conservative 150 N center load. The first 12 mm design produced 0.970 mm deflection and exceeded the provisional 0.80 mm limit. The base was increased to 14 mm in the enhanced STEP and engineering package; the rerun gives 0.611 mm deflection and 9.84 MPa bending stress, passing the preliminary limits without crediting rail stiffening.

## Native-format status

`native_format_status/` records exactly which SolidWorks, STEP and DXF sources were verified, the NX `-10005` license failure, the enhanced-STEP import limitation and the recovery path for a constrained native assembly, DWG save and 3D solver study.
