# DeskQuake Beta 0.2

Planned tag: `deskquake-v0.2-beta2`

## Highlights

- DeskQuake earthquake alerts are routed to the configured private mesh channel instead of falling back to the public default channel.
- Added build-time DeskQuake alert-channel selection via `bin/set-deskquake-alert-channel.py`.
- Added `dqtest` to force a single DeskQuake test alert from the serial console.
- Improved the RAK4631 UF2 upload workflow and added a dry-run mode.
- Removed generic DetectionSensor heartbeat spam from the DeskQuake RAK4631 build.

## Beta Notes

- Verbose DeskQuake serial status logging remains enabled intentionally in Beta 0.2 for field validation and troubleshooting.
- Frequent `DeskQuake status: ...` lines in the serial monitor are expected in this beta build.
- The old repeated mesh messages like `quake node state: 0` are not expected and were removed from the DeskQuake RAK4631 build.

## Validated In Testing

- RAK4631 build succeeded after the DeskQuake merge and follow-up fixes.
- UF2 flash flow worked on hardware.
- DeskQuake private-channel alerting was exercised on the live node.
- Manual shake testing produced a real quake event and clean event closeout.
- `dqcount`, `dqreset`, `dqdfu`, `dqhelp`, and `dqtest` were exercised during validation.