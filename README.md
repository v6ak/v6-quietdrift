# QuietDrift by v6ak for Home Assistant

## Setup

### Config file

Add the following line to config.yaml:

```
v6_quietdrift:
```

### GUI

Not yet supported.

## Usage:

Set position this way:

```
service: v6_quietdrift.set_switchbot_curtain_position
data:
  speed: 1
  position: 90
  entity_id: cover.curtain_3_f00b
```

There is also an older service `cover.v6_set_switchbot_curtain_position`. It does the very same job,
but the old service cannot be easily configured by GUI, only by YAML.
