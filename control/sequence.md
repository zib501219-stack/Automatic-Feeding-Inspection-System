# Automatic cycle sequence

1. Confirm safety chain, home positions and empty V-block.
2. Enable bowl and linear feeder until queue sensor is occupied.
3. Close gate 1, open gate 2 and isolate one shaft.
4. Move transfer carriage to V-block and confirm part presence.
5. Trigger camera and laser micrometer; wait for both completion flags.
6. Combine contour/defect result with diameter judgement.
7. Route OK or NG, eject the part and confirm clear.
8. Return carriage and gates; update counters and repeat.

Timeout at any step stops feeding, retracts to the defined safe state and raises a fault requiring acknowledgement.
