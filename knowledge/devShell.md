# **The Anatomy of a devShell**

In [[environments]] we briefly introduced the concept of a devShell. 

If we get a little more technical, a devShell is a reproducible, isolated shell environment defined declaratively (usually via a `flake.nix`). It provides a specific set of system packages, compilers, and shared libraries without installing them globally. 

The problem it solves: "It works on my machine" syndrome and the lack of standard file-system paths on NixOS. 

Imagine a Python project requiring a concrete system-level library (e.g., `libpq` for PostgreSQL, `geos` for PostGIS, or specific versions of `gcc`), pip or uv will fail to compile native extensions because they cannot find these libraries in the standard paths like `/usr/lib`. 

When you run `nix develop` in that Python project's directory, Nix reads the declarative configuration (the `flake.nix`) and fetches or builds the exact versions of `libpq`, `geos`, and `gcc` specified. It stores them in the immutable `/nix/store`.

Then, rather than installing them globally, Nix drops you into a new, isolated bash shell. Behind the scenes, it intercepts and rewrites your environment variables—such as `PATH`, `LD_LIBRARY_PATH`, `C_INCLUDE_PATH`, and `PKG_CONFIG_PATH`—to point directly to those specific `/nix/store` paths.

Now, when you run `pip install` or `uv sync` inside this shell, the compiler seamlessly finds the required headers and libraries. It succeeds perfectly, regardless of whether you are on NixOS, macOS, or a completely clean Ubuntu installation.

---
***Note**: Delaying this until it's really necessary during a project, or until Milestone 2 is completed*


**Why This is a Game-Changer for Development**


**Creating your first devShell in NixOS**



## Lectures: 

[Easy development environments with Nix and Nix flakes!](https://dev.to/arnu515/easy-development-environments-with-nix-and-nix-flakes-21mb)

[Declarative shell environments with `shell.nix`](https://nix.dev/tutorials/first-steps/declarative-shell.html)

[Making a dev shell with nix flakes](https://fasterthanli.me/series/building-a-rust-service-with-nix/part-10)

[Development shells with Nix: four quick examples (2025)](https://michael.stapelberg.ch/posts/2025-07-27-dev-shells-with-nix-4-quick-examples/)
