{
  "name": "fast-food-wait-times",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "npm run start --prefix server",
    "build-client": "npm run build --prefix client",
    "install-server": "npm install --prefix server",
    "install-client": "npm install --prefix client",
    "install": "npm run install-server && npm run install-client"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/ljmccode/park-wait-times.git"
  },
  "author": "",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/ljmccode/park-wait-times/issues"
  },
  "homepage": "https://github.com/ljmccode/park-wait-times#readme",
  "engines": {
    "node": "16.x"
  }
}
