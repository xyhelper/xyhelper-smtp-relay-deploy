#!/bin/bash
set -e
docker compose pull
docker compose up -d --remove-orphans
docker compose logs -f --tail 100