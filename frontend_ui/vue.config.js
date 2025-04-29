const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  lintOnSave: false,
  transpileDependencies: true,
  configureWebpack: (config) => {
    if (process.env.NODE_ENV === 'development') {
      config.devtool = 'source-map'; // Disable source maps in development for removing debug
    }
  },
});

