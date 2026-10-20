# Releasing

`main` is the only long-lived branch. Changes reach it through pull requests, merge commits only, and
every pull request and push to `main` must pass the `build` check (`.github/workflows/build.yml`: the
tests on Python 3.10–3.13, then build and check the sdist and wheel). Merging publishes nothing.

A release is a **GitHub Release** whose tag is the version, published by `tomasr78`:

```bash
gh release create v2.0.1 --repo ConvertAPI/convertapi-library-python --target main --title v2.0.1 --generate-notes
```

That runs `.github/workflows/publish.yml`, which:

1. refuses a Release published or re-run by anyone else;
2. checks the tag (`v2.0.1`, `v2.1.0-rc.1`), that the GitHub pre-release tick matches the version, that a
   stable version is a commit on `main`, and that PyPI has never had that version;
3. writes the version into `convertapi/__init__.py`, builds the sdist and wheel, and runs the tests
   against the installed wheel (the `live` tests too, when the `CONVERTAPI_SECRET` secret exists);
4. uploads both files to PyPI from the `pypi` environment with Trusted Publishing (no stored token, PEP 740
   attestations) and waits until PyPI serves them.

**Pre-releases** work the same way and may come from any branch. PyPI needs PEP 440 versions, so the
pre-release label is `alpha.N`, `beta.N` or `rc.N` (`v2.1.0-rc.1` becomes `2.1.0rc1`):

```bash
gh release create v2.1.0-rc.1 --repo ConvertAPI/convertapi-library-python --target my-branch --prerelease --title v2.1.0-rc.1 --notes "Release candidate for ..."
```

PyPI versions are permanent: a file name can never be uploaded again, even after the release is deleted.
A bad version can only be yanked on PyPI, then fixed by releasing the next version. Never delete and
re-create a release tag.

`__version__` in `convertapi/__init__.py` is a `0.0.0.dev0` placeholder; pull request builds produce
`0.0.0.dev{run}+g{sha}` as a downloadable artifact so a change can be tried before it is released.
Update `CHANGELOG.md` in the pull request that changes behaviour.

## Guard rails

- Rulesets: `main` takes pull requests with merge commits and a passing `build` (admins can bypass);
  only repository admins create, move or delete `v*` tags, and a `v*` tag must match the pattern above.
- The `pypi` environment accepts deployments from `v*` tags only.
- PyPI trusts `ConvertAPI/convertapi-library-python`, workflow `publish.yml`, environment `pypi`
  (https://pypi.org/manage/project/convertapi/settings/publishing/). Renaming the workflow file or the
  environment breaks publishing until the trusted publisher is changed to match.
