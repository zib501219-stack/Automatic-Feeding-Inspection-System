# Feeding-system sequence and interlock validation

## Result

The proposed sequence closes in exactly 5.0 seconds, matching the 12 parts/min target. The generated state table samples the sequence every 0.1 seconds.

The critical logical rules are:

- rear gate closes before the front gate releases a part;
- transfer extension requires part presence, separator confirmation and a clear nest;
- camera trigger requires transfer-extended and clamp confirmation;
- the next feed cannot start until transfer-home is true.

## Boundary

This is an offline sequence model, not a PLC simulation. Valve switching time, cylinder cushioning, sensor debounce, image-processing time, reject handling and fault recovery must be commissioned on the selected hardware. The 5-second cycle remains a design target until measured.
