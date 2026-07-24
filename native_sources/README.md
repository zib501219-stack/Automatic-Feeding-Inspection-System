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
