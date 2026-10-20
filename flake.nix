# website2.0 publish target: the INTERIOR half of the mkTenant contract (ADR 0020).
#
# COPY-IN HANDOFF: this file belongs at the ROOT of UCSD-E4E/website2.0 (see
# docs/handoff/e4e-website/HANDOFF.md in krg-infra). Same platform pieces as the
# reference-manager / fishsense-services flakes, but this tenant runs NO app: the slot is
# only the campus-side hop that publishes the built site to Jacobs web hosting
# (mywebsite.eng.ucsd.edu, whose SSH is reachable from campus only). No compose, no edge.
#
# `e4e-website-selfupdate` on the slot converges it with
#   nixos-rebuild switch --flake github:UCSD-E4E/website2.0#e4e-website
# (.github/workflows/converge.yml, or the nightly autoUpgrade).
{
  description = "website2.0 — KRG Incus platform tenant `e4e-website` (publishes e4e.ucsd.edu)";

  inputs = {
    # Tracks krg-infra `main`; the EXACT rev is pinned in `flake.lock`. Advancing it
    # ("Axis B", krg-infra docs/tenant-updates.md) is how the slot gets OS security
    # patches: .github/workflows/update-flake.yml does it weekly. Don't disable it.
    krg-infra.url = "github:KastnerRG/krg-infra?dir=nix";
    nixpkgs.follows = "krg-infra/nixpkgs";
  };

  outputs = {
    self,
    krg-infra,
    nixpkgs,
  }: let
    system = "x86_64-linux";

    tenant = krg-infra.lib.mkTenant {
      name = "e4e-website"; # Incus project + OpenBao role tenant-e4e-website + runner scope
      zone = "e4e"; # informational only: the slot has no public route
      hostname = "e4e.ucsd.edu"; # the site it publishes (served by Jacobs hosting, not the slot)
      resources = {
        # What the admin provisioned (krg-infra terraform/incus). The build runs on
        # GitHub-hosted CI; the slot only rsyncs the result and rebuilds itself.
        cpu = 2;
        ram = "4GiB";
        disk = "20GiB";
      };
      image = "krg-golden"; # slot boots from the hardened template
      # No `compose`: there is no app to run.
      # LOAD-BEARING: scopes the auto-provisioned runner (ADR 0022) AND the nightly
      # autoUpgrade / selfupdate flake URL (github:<repo>#e4e-website).
      repo = "UCSD-E4E/website2.0";
    };
  in {
    nixosConfigurations.e4e-website = nixpkgs.lib.nixosSystem {
      inherit system;
      modules = [
        krg-infra.nixosModules.tenant
        {krg.tenant = tenant;}
        # Incus VM plumbing: the SAME module the krg-golden image builds from.
        ({modulesPath, ...}: {
          imports = [(modulesPath + "/virtualisation/incus-virtual-machine.nix")];
        })
        # Ephemeral VM tier is OEC-exempt, matching krg-golden (base.nix hard-enables it).
        ({lib, ...}: {
          krg.oecQualysTrellix.enable = lib.mkForce false;
        })
        # Stamp the commit this generation was built from (`nixos-version
        # --configuration-revision`): converge.yml's verify checks it against main.
        {system.configurationRevision = self.rev or self.dirtyRev or "dirty";}
        ./deploy/incus/publish.nix # the publish unit + its SSH key render
      ];
    };

    # Reproducible boundary projection (admin copies into krg-infra terraform/incus):
    #   nix eval .#krgTenant.terraformTenant --json
    krgTenant = tenant;
  };
}
