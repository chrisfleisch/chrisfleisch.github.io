import fs from 'node:fs'

if (process.env.CI) {
  process.exit(0)
}

if (!fs.existsSync('/.dockerenv')) {
  console.error(
    '\nnpm must be run inside Docker, not on the host.\n' +
      'Use ./scripts/docker-npm.sh <service> <npm-args...> instead ' +
      '(service is "tools" for root, "fe" for the frontend app).\n'
  )
  process.exit(1)
}
