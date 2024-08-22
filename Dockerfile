FROM node:22-bookworm AS base

FROM base AS fe

WORKDIR /opt/app