FROM node:25-bookworm AS base

FROM base AS fe

WORKDIR /opt/app
