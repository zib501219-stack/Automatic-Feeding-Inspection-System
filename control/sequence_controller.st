(*
 IEC 61131-3 Structured Text reference implementation.
 Safety inputs must act through certified safety hardware; this program is
 the standard-control sequence and is not a safety PLC certification.
*)

ReadyPermissive := DI_ESTOP_OK AND DI_GUARD_OK AND DI_AIR_OK
                   AND NOT DI_BIN_OK_FULL AND NOT DI_BIN_NG_FULL;

IF NOT ReadyPermissive THEN
    State := 900;
END_IF;

CASE State OF
    0: (* STOPPED *)
        DO_BOWL_ENABLE := FALSE;
        DO_GATE1 := FALSE; DO_GATE2 := FALSE;
        DO_TRANSFER := FALSE; DO_EJECT_OK := FALSE; DO_EJECT_NG := FALSE;
        IF DI_START AND ReadyPermissive THEN State := 10; END_IF;

    10: (* HOMING *)
        DO_GATE1 := FALSE; DO_GATE2 := FALSE;
        DO_TRANSFER := FALSE; DO_EJECT_OK := FALSE; DO_EJECT_NG := FALSE;
        IF DI_GATE1_HOME AND DI_GATE2_HOME AND DI_TRANSFER_HOME AND DI_EJECT_HOME THEN
            State := 20;
        END_IF;

    20: (* FEED QUEUE *)
        DO_BOWL_ENABLE := TRUE;
        IF DI_QUEUE_PRESENT THEN DO_BOWL_ENABLE := FALSE; State := 30; END_IF;

    30: (* ISOLATE ONE PART *)
        DO_GATE1 := TRUE;
        IF DI_GATE1_WORK THEN DO_GATE2 := TRUE; END_IF;
        IF DI_GATE1_WORK AND DI_GATE2_WORK THEN State := 40; END_IF;

    40: (* TRANSFER *)
        DO_TRANSFER := TRUE;
        IF DI_TRANSFER_WORK AND DI_PART_AT_V THEN State := 50; END_IF;

    50: (* TRIGGER *)
        DO_CAMERA_TRIGGER := TRUE;
        DO_LASER_TRIGGER := TRUE;
        IF TriggerPulse.Q THEN
            DO_CAMERA_TRIGGER := FALSE; DO_LASER_TRIGGER := FALSE; State := 60;
        END_IF;

    60: (* WAIT RESULTS *)
        IF DI_CAMERA_DONE AND DI_LASER_READY THEN State := 70; END_IF;

    70: (* DECISION *)
        LatchedOK := VisionOK AND DimensionOK AND ResultValid;
        LatchedNG := NOT LatchedOK;
        State := 80;

    80: (* EJECT *)
        DO_EJECT_OK := LatchedOK;
        DO_EJECT_NG := LatchedNG;
        IF DI_EJECT_WORK THEN State := 90; END_IF;

    90: (* VERIFY CLEAR *)
        DO_EJECT_OK := FALSE; DO_EJECT_NG := FALSE;
        IF DI_EJECT_HOME AND NOT DI_PART_AT_V THEN State := 100; END_IF;

    100: (* RETURN *)
        DO_TRANSFER := FALSE; DO_GATE1 := FALSE; DO_GATE2 := FALSE;
        IF DI_TRANSFER_HOME AND DI_GATE1_HOME AND DI_GATE2_HOME THEN State := 110; END_IF;

    110: (* COUNT *)
        TotalCount := TotalCount + 1;
        IF LatchedOK THEN OKCount := OKCount + 1; ELSE NGCount := NGCount + 1; END_IF;
        IF DI_STOP THEN State := 0; ELSE State := 20; END_IF;

    900: (* FAULT *)
        DO_BOWL_ENABLE := FALSE;
        DO_GATE1 := FALSE; DO_GATE2 := FALSE; DO_TRANSFER := FALSE;
        DO_EJECT_OK := FALSE; DO_EJECT_NG := FALSE;
        IF DI_RESET AND ReadyPermissive THEN State := 10; END_IF;
END_CASE;

DO_MOTION_ENABLE := ReadyPermissive AND (State <> 900);
DO_STACK_GREEN := (State > 0) AND (State < 900);
DO_STACK_YELLOW := (State = 0);
DO_STACK_RED := (State = 900);
