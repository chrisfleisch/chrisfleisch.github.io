FROM node:26-bookworm AS base

FROM base AS fe

WORKDIR /opt/app

# Keep this version in sync with @playwright/test in fe/package.json
RUN npx --yes playwright@1.62.1 install --with-deps chromium

FROM base AS tools

WORKDIR /opt/app
