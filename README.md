<div align="center" markdown="1">

<img src=".github/meshtastic_logo.png" alt="Meshtastic Logo" width="80"/>
<h1>DeskQuake Firmware</h1>

![GitHub release downloads](https://img.shields.io/github/downloads/meshtastic/firmware/total)
[![CI](https://img.shields.io/github/actions/workflow/status/meshtastic/firmware/main_matrix.yml?branch=master&label=actions&logo=github&color=yellow)](https://github.com/meshtastic/firmware/actions/workflows/ci.yml)
[![CLA assistant](https://cla-assistant.io/readme/badge/meshtastic/firmware)](https://cla-assistant.io/meshtastic/firmware)
[![Fiscal Contributors](https://opencollective.com/meshtastic/tiers/badge.svg?label=Fiscal%20Contributors&color=deeppink)](https://opencollective.com/meshtastic/)
[![Vercel](https://img.shields.io/static/v1?label=Powered%20by&message=Vercel&style=flat&logo=vercel&color=000000)](https://vercel.com?utm_source=meshtastic&utm_campaign=oss)

<a href="https://trendshift.io/repositories/5524" target="_blank"><img src="https://trendshift.io/api/badge/repositories/5524" alt="meshtastic%2Ffirmware | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

</div>

<div align="center">
	<a href="https://github.com/kl5pfak/deskquake-firmware">Code</a>
	-
	<a href="https://github.com/kl5pfak/deskquake-firmware/releases/tag/deskquake-v0.2-beta2">Beta 0.2 Release</a>
	-
	<a href="https://github.com/kl5pfak/deskquake-firmware/blob/deskquake-beta-0.1/docs/index.md">Documentation</a>
</div>

## Overview

This repository contains the DeskQuake firmware fork built on Meshtastic for the RAK4631 paired with the RAK12027 seismic sensor. It monitors local ground motion, evaluates events on-device, and sends alerts across a Meshtastic mesh without depending on internet or cellular infrastructure.

DeskQuake Beta 0.2 is the current published prerelease for field validation on RAK4631 hardware. The validated release asset is `DeskQuake-Beta-0.2-rak4631.uf2` under the `deskquake-v0.2-beta2` prerelease.

This fork remains based on Meshtastic firmware and preserves the broader mesh stack while adding DeskQuake-specific sensor handling, operator commands, private-channel alert routing, and UF2 deployment helpers.

### Get Started

- 🔧 **[Build the firmware](https://github.com/kl5pfak/deskquake-firmware/blob/deskquake-beta-0.1/docs/index.md)** - Review the DeskQuake hardware and operator workflow.
- ⚡ **[Download Beta 0.2](https://github.com/kl5pfak/deskquake-firmware/releases/tag/deskquake-v0.2-beta2)** - Get the current prerelease UF2 for RAK4631.
- 🧪 **[Beta release notes](https://github.com/kl5pfak/deskquake-firmware/blob/deskquake-beta-0.1/release/deskquake-beta-0.2-github-release.md)** - See the validated Beta 0.2 behavior and test notes.

## DeskQuake Highlights

- Target board: RAK4631
- Sensor module: RAK12027 with Omron D7S
- Default DeskQuake alert channel: channel `5` / `KL5PF`
- Operator commands: `dqcount`, `dqreset`, `dqtest`, `dqdfu`, `dqhelp`
- Current release: `deskquake-v0.2-beta2` prerelease

## Upstream Base

DeskQuake is maintained as a Meshtastic-based fork. Upstream Meshtastic firmware remains at https://github.com/meshtastic/firmware.

## Stats

![Alt](https://repobeats.axiom.co/api/embed/8025e56c482ec63541593cc5bd322c19d5c0bdcf.svg "Repobeats analytics image")

---

## Attribution

DeskQuake Firmware is maintained in this repository by KL5PFAK and is derived from the Meshtastic firmware project.

Upstream project:
[meshtastic/firmware](https://github.com/meshtastic/firmware)

Credit and thanks go to the Meshtastic maintainers and contributors whose work this repository builds on.

This repository continues to distribute the code under the GPLv3 terms in [LICENSE](LICENSE).
