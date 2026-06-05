FROM node:26-bookworm AS base

FROM base AS fe

WORKDIR /opt/app
