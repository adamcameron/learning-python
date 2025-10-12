# learning-python

And now I need to learn Python...

## Bring up the dev environment:

```bash
docker compose -f docker/docker-compose.yml down # optional: --remove-orphans --volumes
docker compose -f docker/docker-compose.yml build
docker compose -f docker/docker-compose.yml up --detach
```

Currently this just runs `bash` and sits there waiting.

There is a shell script `bin/rebuild.sh` that does the above steps in one go (including removing orphans and volumes).

## Tooling

```bash
# run tests
docker exec learning-python-python-1 uv run pytest

# run test watcher
docker exec -it learning-python-python-1 uv run ptw .

# check code syntax
docker exec learning-python-python-1 uvx ruff check

# fix code formatting
docker exec learning-python-python-1 uvx ruff format --diff

# check pyright for static typechecking issues
docker exec learning-python-python-1 uvx pyright
```
