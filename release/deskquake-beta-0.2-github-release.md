# DeskQuake Beta 0.2 for RAK4631

Experimental earthquake-monitoring firmware for the RAK4631 paired with the RAK12027 D7S sensor.

## Warning

DeskQuake is an experimental field project. It is not a life-safety, emergency-warning, or certified seismic detection system.

## Highlights

- Routes DeskQuake alerts to the configured private mesh channel instead of the public default channel.
- Adds build-time DeskQuake alert-channel selection with `bin/set-deskquake-alert-channel.py`.
- Adds `dqtest` to send one test alert from the serial console.
- Improves the RAK4631 UF2 upload workflow and adds dry-run support.
- Removes generic DetectionSensor heartbeat spam from the DeskQuake RAK4631 build.

## Beta Notes

- Verbose `DeskQuake status: ...` serial logging remains enabled intentionally in Beta 0.2 for field validation and troubleshooting.
- Frequent serial status lines are expected in this beta build.
- Repeated mesh messages like `quake node state: 0` are not expected and were removed from the RAK4631 DeskQuake build.

## Operator Commands

- `dqcount`
- `dqreset`
- `dqtest`
- `dqdfu`
- `dqhelp`

## Validated In Testing

- Built successfully for `rak4631`.
- Flashed successfully using the UF2 workflow.
- Private-channel alerting was exercised on real hardware.
- Manual shake testing produced a real quake event and clean event closeout.
- `dqcount`, `dqreset`, `dqdfu`, `dqhelp`, and `dqtest` were exercised during validation.

## Planned Release Assets

- Tag: `deskquake-v0.2-beta2`
- UF2: `DeskQuake-Beta-0.2-rak4631.uf2`