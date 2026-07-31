{
  description = "Minimal UV-to-NixOS devShell for testing solutions using nix-ld.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            uv
            ruff
          ];

          # Expose libraries to the nix-ld environment
          # NOTE: This devShell requires `programs.nix-ld.enable = true;` to be set in your 
          # NixOS configuration (/etc/nixos/configuration.nix) to successfully run downloaded 
          # pre-compiled binaries (e.g. PyPI dynamic wheels).
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc.lib
            pkgs.zlib
            pkgs.glib
          ];
        };
      });
}
