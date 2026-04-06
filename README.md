<h1 align="center">DeskQuake for RAK4631</h1>

<p align="center">
	<img alt="Platform" src="https://img.shields.io/badge/platform-RAK4631-blue">
	<img alt="Sensor" src="https://img.shields.io/badge/sensor-RAK12027-orange">
	<img alt="Mesh" src="https://img.shields.io/badge/mesh-Meshtastic-green">
	<img alt="Status" src="https://img.shields.io/badge/status-beta-brightgreen">
</p>
	Earthquake-monitoring firmware for RAK4631 with local mesh alerting, operator serial commands, and drag-and-drop UF2 releases.
</p>

<p align="center">
	Independently maintained by KL5PFAK and derived from Meshtastic.
</p>

---

## Download

Current prerelease:
[DeskQuake Beta 0.1 for RAK4631](https://github.com/kl5pfak/deskquake-firmware/releases/tag/deskquake-v0.1-beta1)

Direct firmware download:
[DeskQuake-Beta-0.1-rak4631.uf2](https://github.com/kl5pfak/deskquake-firmware/releases/download/deskquake-v0.1-beta1/DeskQuake-Beta-0.1-rak4631.uf2)

---

## Quick Start

1. Put the RAK4631 into UF2 bootloader mode.
2. Drag [release/DeskQuake-Beta-0.1-rak4631.uf2](release/DeskQuake-Beta-0.1-rak4631.uf2) onto the mounted bootloader volume.
3. Reconnect to serial at `115200`.
4. Run `dqcount`, `dqreset`, or `dqdfu` to verify the beta tooling.

---

## What This Repo Adds

- DeskQuake earthquake monitoring behavior on RAK4631
- Mesh alerts when quake activity is detected
- Operator serial commands:
	- `dqcount`
	- `dqreset`
	- `dqdfu`
	- `dqhelp`
- A helper script for serial commands:
	- `bin/deskquake-command.sh`
- A UF2-oriented upload path for more reliable flashing on macOS:
	- `bin/upload-rak4631-uf2.sh`

---

## Sensor Hardware

- Target board: RAK4631
- Sensor module: RAK12027 using the D7S earthquake sensor
- Sensor bus: I2C on address `0x55`
- Sensor power control: `WB_IO2` is toggled by the firmware during startup and recovery
- Current alert channel label in firmware: `KL5PF`

The firmware probes the D7S sensor, waits for it to become ready, tracks SI and PGA values, counts quake events, and resets sensor events after a completed quake.

Sensor reference:
- Hardware listing: [RAKwireless RAK12027 Earthquake Sensor Omron D7S PID 100106](https://store.rokland.com/products/rakwireless-rak12027-earthquake-sensor-omron-d7s-pid-100106?_pos=1&_psq=Earth&_ss=e&_v=1.0&ref=FairbanksMesh)
- Official documentation: [RAK12027 Datasheet](https://docs.rakwireless.com/Product-Categories/WisBlock/RAK12027/Datasheet/)

---

## Build

Build locally with PlatformIO:

```bash
pio run -e rak4631
```

The resulting UF2 is written to:

```text
.pio/build/rak4631/
```

An easy-to-find release copy can also be placed in:

```text
release/DeskQuake-Beta-0.1-rak4631.uf2
```

---

## Operator Notes

- Close any running serial monitor before using `bin/deskquake-command.sh`.
- On macOS, prefer `bin/upload-rak4631-uf2.sh` if the standard upload path leaves the board silent.
- `dqdfu` works only after the board is already running a build that includes that command.
- The sensor is expected to answer on I2C address `0x55`. If it does not, quake monitoring will not enter the normal runtime state.

---

## Attribution

DeskQuake Firmware is maintained in this repository by KL5PFAK and is derived from the Meshtastic firmware project.

Upstream project:
[meshtastic/firmware](https://github.com/meshtastic/firmware)

Credit and thanks go to the Meshtastic maintainers and contributors whose work this repository builds on.

This repository continues to distribute the code under the GPLv3 terms in [LICENSE](LICENSE).
