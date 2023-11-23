const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: [
      'localhost',
      'eblan03112005.fvds.ru',
      '192.168.1.1',
      '77.246.159.10',
'bogdanbogomdan.ru'
    ],
  },
})
