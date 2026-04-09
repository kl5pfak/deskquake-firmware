---
layout: default
title: DeskQuake
---

<h1 align="center">DeskQuake for RAK4631</h1>

<p align="center">
  <img src="logo.jpeg" width="250" alt="DeskQuake logo">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-RAK4631-blue">
  <img src="https://img.shields.io/badge/sensor-RAK12027-orange">
  <img src="https://img.shields.io/badge/mesh-Meshtastic-green">
  <img src="https://img.shields.io/badge/status-beta-brightgreen">
</p>

DeskQuake is experimental earthquake-monitoring firmware for the RAK4631 paired with the RAK12027 seismic sensor. It watches for local ground motion, evaluates events on-device, and sends alerts across a Meshtastic mesh so nearby nodes can react without internet infrastructure.

## Warning

DeskQuake is an experimental field project and must not be treated as a life-safety, emergency-warning, or certified seismic detection system. Use it for testing, situational awareness, and operator evaluation only.

## What It Does

<p align="center">
  <img src="Screen.jpeg" width="450" alt="DeskQuake telemetry preview">
</p>

Each node measures seismic activity locally and decides when readings cross the configured event threshold. When that happens, the device publishes an alert over Meshtastic so other nodes in range, including multi-hop neighbors, can see the event quickly.

This makes the system useful in remote locations where the mesh network itself is the communications backbone.

## System Flow

1. The RAK12027 D7S sensor captures vibration data.
2. DeskQuake processes the incoming seismic values.
3. Detection logic determines whether the reading qualifies as an event.
4. The node broadcasts an alert over Meshtastic.
5. Other mesh nodes receive the alert and surface it to operators.

## Download

Planned prerelease for later upload:
`DeskQuake Beta 0.2 for RAK4631`

Planned release tag:
`deskquake-v0.2-beta2`

Planned firmware image name:
`DeskQuake-Beta-0.2-rak4631.uf2`

Beta 0.2 note:
Verbose DeskQuake serial status logging remains enabled intentionally for field validation in this beta build.

Source repository:
[kl5pfak/deskquake-firmware](https://github.com/kl5pfak/deskquake-firmware)

## Quick Start

1. Put the RAK4631 into UF2 bootloader mode.
2. Copy the UF2 file to the mounted bootloader volume.
3. Reconnect over serial at `115200` baud.
4. Run `dqhelp` to list the available beta commands.
5. Use `dqcount`, `dqreset`, `dqtest`, or `dqdfu` to confirm the tooling is working.

## Hardware

- Target board: RAK4631
- Sensor module: RAK12027 with the Omron D7S
- Sensor bus: I2C at address `0x55`
- Sensor power control: `WB_IO2`
- Default DeskQuake alert channel in firmware: channel `5` / `KL5PF`

References:

- [RAKwireless RAK12027 product page](https://store.rokland.com/products/rakwireless-rak12027-earthquake-sensor-omron-d7s-pid-100106?_pos=1&_psq=Earth&_ss=e&_v=1.0&ref=FairbanksMesh)
- [RAK12027 datasheet](https://docs.rakwireless.com/Product-Categories/WisBlock/RAK12027/Datasheet/)

## Operator Commands

- `dqcount`
- `dqreset`
- `dqtest`
- `dqdfu`
- `dqhelp`

Helper scripts:

- [deskquake-command.sh](../bin/deskquake-command.sh)
- [set-deskquake-alert-channel.py](../bin/set-deskquake-alert-channel.py)
- [upload-rak4631-uf2.sh](../bin/upload-rak4631-uf2.sh)

Non-destructive upload validation:

- `bin/upload-rak4631-uf2.sh -n`

Build-time alert channel selection:

- `python3 bin/set-deskquake-alert-channel.py`
- Defaults: channel `5`, label `KL5PF`

Beta 0.2 behavior note:

- Frequent `DeskQuake status: ...` lines on the serial console are expected in this beta.
- Repeated mesh messages like `quake node state: 0` are not expected and were removed from the RAK4631 DeskQuake build.

## Attribution

DeskQuake is maintained by KL5PFAK and builds on the Meshtastic firmware project.

Upstream project:
[meshtastic/firmware](https://github.com/meshtastic/firmware)

Thanks go to the Meshtastic maintainers and contributors whose work made this fork possible.

This repository continues to distribute the code under the GPLv3 terms described in [LICENSE](https://github.com/kl5pfak/deskquake-firmware/blob/deskquake-v0.2-beta2/LICENSE).

## Project Links

- [Code](https://github.com/kl5pfak/deskquake-firmware)
- [Issues](https://github.com/kl5pfak/deskquake-firmware/issues)
- [Pull requests](https://github.com/kl5pfak/deskquake-firmware/pulls)
- [Actions](https://github.com/kl5pfak/deskquake-firmware/actions)
- [Security](https://github.com/kl5pfak/deskquake-firmware/security)
