# DeskQuake Beta 0.2 Upload Checklist

## Recommended GitHub Release Title

`DeskQuake Beta 0.2 for RAK4631`

## Planned Tag

`deskquake-v0.2-beta2`

## Planned Asset Name

`DeskQuake-Beta-0.2-rak4631.uf2`

## Suggested Upload Steps

1. Build the firmware for `rak4631`.
2. Rename or copy the UF2 artifact to `DeskQuake-Beta-0.2-rak4631.uf2` if needed.
3. Create the GitHub prerelease with tag `deskquake-v0.2-beta2`.
4. Paste the release body from `release/deskquake-beta-0.2-github-release.md`.
5. Optionally use `release/deskquake-beta-0.2-summary.md` as the short summary/description.
6. Upload `DeskQuake-Beta-0.2-rak4631.uf2` as the release asset.

## Validated Points To Mention

- Private-channel DeskQuake alert routing is active.
- Build-time alert-channel selection is available.
- `dqtest` is included and kept in the firmware.
- Generic DetectionSensor mesh spam was removed from the DeskQuake RAK4631 build.
- Verbose serial `DeskQuake status: ...` logging remains intentionally enabled for Beta 0.2.