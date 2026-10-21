# Website publishing

GitHub-hosted CI builds and checks the website. On `main`, it stamps `_site/` with
the commit and uploads the `site` artifact, including `.htaccess`. The campus
`e4e-website` runner downloads the artifact and starts `e4e-website-publish`, which
uploads it to `e4e@mywebsite.eng.ucsd.edu:htdocs/`. The hosting server accepts SSH
from campus only. The runner does not receive the SSH private key; the publishing
service obtains it from the platform's OpenBao secret store.

When `AUTO_VERSIONING_ENABLED=true`, the build waits for automatic version
metadata on `main`; it publishes the App's metadata follow-up commit rather than
the original unversioned merge. Configure the App and branch permissions described
in the root README before activating this setting. Versioning does not enable a
disabled deployment workflow or change the production verification required for
release tags.

The slot's NixOS configuration is `flake.nix` plus `incus/publish.nix`. Its exact
infrastructure dependencies are committed in `flake.lock`. Configuration changes
on `main` trigger `converge.yml`; `update-flake.yml` advances the infrastructure
pin weekly, evaluating the configuration before committing it.

## Initial activation (coordinate with the infrastructure administrator)

Follow the [platform onboarding runbook](https://github.com/KastnerRG/krg-infra/blob/main/docs/onboarding-e4e-website.md).
Before activating the slot:

- Use Actions Runner 2.327.1 or newer on the campus slot for the Node 24 action
  runtime. The website itself still builds with Node 22; these are separate runtimes.

- Apply the platform's OpenBao role and install the publisher's public key on the
  hosting account. Confirm the hosting server has `rsync`.
- Install the platform runner GitHub App on this repository.
- Configure `vars.APP_ID` and `secrets.APP_PRIVATE_KEY` for the weekly pin-update
  GitHub App, with permission to push to protected `main`.
- Require approval for all outside collaborators in Actions settings. Never run
  untrusted pull-request code on the campus runner.
- Cancel queued publishing jobs before the first manual slot converge, as described
  in the runbook. The publisher workflow was manually disabled when this handoff was
  prepared; enable **Deploy E4E website** after coordinating slot readiness.

After activation, dispatch **Deploy E4E website** on `main`, inspect its publish log,
and check `https://e4e.ucsd.edu/last_deployed.txt` for the expected commit. Remove the
old `KASTNER_ML_DEPLOY_SSH` and `KASTNER_ML_KNOWN_HOSTS` secrets only after the new
publisher is verified.

## Updating the dependency lock manually

With Nix installed:

```sh
nix flake update krg-infra
nix eval --raw .#nixosConfigurations.e4e-website.config.system.build.toplevel.drvPath
```

Commit the resulting `flake.lock`. A configuration evaluation checks the module
contract; it does not prove the campus network, SSH credential, or live upload works.
