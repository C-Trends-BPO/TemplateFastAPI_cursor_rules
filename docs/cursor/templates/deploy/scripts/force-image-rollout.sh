#!/usr/bin/env bash
# Força rolling update com a mesma tag em todas as réplicas (manager do Swarm).
# Uso: bash deploy/scripts/force-image-rollout.sh <STACK_NAME> <IMAGE_TAG_OU_SHA>
#
# Exemplo:
#   bash deploy/scripts/force-image-rollout.sh minha_app ghcr.io/org/repo:abc123def

set -euo pipefail

STACK_NAME="${1:?Informe STACK_NAME (ex.: minha_app)}"
IMAGE_TAG="${2:?Informe a tag ou SHA da imagem (ex.: ghcr.io/org/repo:abc123)}"

SERVICE="${STACK_NAME}_web"

echo "Serviço: ${SERVICE}"
echo "Imagem alvo: ${IMAGE_TAG}"

docker service inspect "${SERVICE}" >/dev/null 2>&1 || {
  echo "Serviço ${SERVICE} não encontrado. Verifique STACK_NAME."
  exit 1
}

docker pull "${IMAGE_TAG}"

docker service update \
  --image "${IMAGE_TAG}" \
  --update-order stop-first \
  --with-registry-auth \
  "${SERVICE}"

echo "Rollout iniciado. Acompanhe com:"
echo "  docker service ps ${SERVICE} --filter desired-state=running --format '{{.Node}} {{.Image}}'"
