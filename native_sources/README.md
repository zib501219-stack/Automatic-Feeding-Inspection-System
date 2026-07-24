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
