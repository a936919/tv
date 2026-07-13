# Versioning

`version.properties` is the single source of truth for the maintained app release:

```properties
VERSION_CODE=557
VERSION_NAME=5.5.7
```

## Feature releases

When a maintained feature is released:

1. Increase `VERSION_CODE` by at least one. Android uses this integer to decide whether an APK is an upgrade.
2. Update `VERSION_NAME` using semantic `major.minor.patch` notation for the user-visible release.
3. Commit the version change together with the feature or release commit.

Normal local Gradle builds use these two values directly.

## TV-AutoBuild releases

The public builder passes `-PappVersionCode` and `-PappVersionName` without rewriting the source tree:

- `versionCode = source VERSION_CODE * 1,000,000 + GitHub run number`
- `versionName = source VERSION_NAME-autobuild.<run number>+<TV short SHA>`

For example, source `5.5.7`/`557` in run 12 at TV commit `abcdef0` becomes:

- `versionCode = 557000012`
- `versionName = 5.5.7-autobuild.12+abcdef0`

The source version records the functional release. The autobuild suffix identifies the exact build, while the derived code remains monotonically upgradeable for up to 999,999 workflow runs per source version.
