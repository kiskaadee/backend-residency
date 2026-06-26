# Docker & Containerization Notes

## Docker Core Concepts
- **Image:** A read-only template with instructions for creating a Docker container.
- **Container:** A runnable instance of an image. Isolated from other containers and the host.
- **Dockerfile:** A text document containing all the commands a user could call on the command line to assemble an image.
- **Docker Compose:** A tool for defining and running multi-container Docker applications using YAML configuration.

## Multi-stage Builds
- Used to keep final production image sizes small by compiling/building in an initial stage, then copying only the built artifacts into a minimal runtime image.
