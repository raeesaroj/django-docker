# BIPAD SERVER

[![pipeline status](https://gitlab.com/bipad/server/badges/develop/pipeline.svg)](https://gitlab.com/bipad/server/commits/develop) [![coverage report](https://gitlab.com/bipad/server/badges/develop/coverage.svg)](https://bipad.gitlab.io/server/)

## SETUP

1. Clone this repository
2. Install [docker](https://get.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/)
3. Create a symlink with name docker-compose.yml to docker-compose.local.yml
4. Run external services `docker-compose -f external_services.yml up -d`
5. Run the server `docker-compose up -d`

*Note: for logs run `docker-compose logs -f --tail 100`*

