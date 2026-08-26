# MicrobitStabilizer

A Micro:bit-based stabilization system that uses the built-in accelerometer to detect tilt and dynamically control servos to keep a platform balanced.

## Overview

**MicrobitStabilizer** reads the Micro:bit's 3-axis accelerometer data and converts the measured tilt into servo adjustments.

The system currently stabilizes two axes:

* **X-axis:** Controls servos connected to pins `P10` and `P13`
* **Y-axis:** Controls servos connected to pins `P1` and `P2`
* **Z-axis:** Read for monitoring but not currently used for stabilization

The project is designed around a calibrated relationship between accelerometer readings and physical tilt.

## Hardware

* BBC micro:bit
* 4× servo motors
* Stabilization platform / mechanical frame
* Suitable servo power supply
* Jumper wires
* Mechanical mounting hardware

### Pin Configuration

| Pin   | Function       |
| ----- | -------------- |
| `P1`  | Y-axis servo 1 |
| `P2`  | Y-axis servo 2 |
| `P10` | X-axis servo 1 |
| `P13` | X-axis servo 2 |

> **Important:** Servos can draw significantly more current than the micro:bit can safely supply. Use an appropriate external power supply and ensure the grounds are connected.

## How It Works

The Micro:bit accelerometer reports acceleration approximately in milli-g units.

The program converts this value into an estimated angle:

```python
def coordinate_degree(n):
    return n/1000*90
```

This assumes approximately:

```text
1000 accelerometer units ≈ 90°
```

The resulting angle is then used to offset the servo position from the neutral position of `90°`.

For the Y-axis:

```python
pin1.write_analog(90+coordinate_degree(y))
pin2.write_analog(90-coordinate_degree(y))
```

The two servos move in opposite directions, allowing them to compensate for the detected tilt.

The same principle is applied to the X-axis using `P10` and `P13`.

## Stabilization Limits

The current implementation only activates stabilization within defined angular ranges.

### Y-axis

```text
-22.5° ≤ Y ≤ 22.5°
```

### X-axis

```text
-45° ≤ X ≤ 45°
```

Outside these ranges, the corresponding stabilization function is not executed.

## Calibration Data

The source code contains the following measured reference points:

```text
perpendicular_normal: -1056
perpendicular_front:  -972
perpendicular_back:    988
perpendicular_right:  1000
perpendicular_left:  -1016
```

## Current Limitations

The current implementation is a basic proportional stabilization system rather than a full feedback controller.

Potential issues include:

1. **Linear angle conversion**
   The relationship between accelerometer readings and angle is approximated as linear.

2. **No filtering**
   Accelerometer noise can cause servo jitter.

3. **No PID control**
   The system currently does not account for accumulated error or rate of change.

4. **Z-axis is unused**
   Although `z` is measured, it does not currently influence stabilization.

5. **Servo limits are not explicitly enforced**
   Calculated servo positions should ideally be constrained to safe operating limits.

6. **No deadband**
   Small accelerometer fluctuations may cause unnecessary servo movement.

## Future Improvements

### 1. Implement a deadband

Ignore very small changes in measured tilt to reduce servo jitter.

### 2. Add filtering

A moving average or low-pass filter could smooth accelerometer readings before they are sent to the servo controller.

### 3. Implement PID control

A PID controller could significantly improve stability:

```text
Control = Kp × Error
        + Ki × Accumulated Error
        + Kd × Rate of Error Change
```

This would allow the platform to respond more intelligently to disturbances.

### 4. Improve calibration

Measure multiple known orientations and calculate a calibration model rather than assuming:

```text
1000 units = 90°
```

### 5. Add servo saturation

Limit servo commands to a safe range:

```text
0° ≤ servo angle ≤ 180°
```

### 6. Use sensor fusion

For more accurate orientation estimation, accelerometer data could eventually be combined with a gyroscope using a complementary filter or another sensor-fusion algorithm.

## Project Goal

The long-term goal of **MicrobitStabilizer** is to develop a compact, low-cost stabilization platform using a Micro:bit as the control system.

The project can serve as a foundation for experimenting with:

* Feedback control
* Robotics
* Embedded systems
* Accelerometer calibration
* Servo control
* PID controllers
* Sensor fusion
* Mechatronics

## License

This project is open-source. Add your preferred license before publishing the repository.
