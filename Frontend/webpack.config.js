const webpack = require("webpack");
const HTMLWebpackPlugin = require("html-webpack-plugin");
const { VueLoaderPlugin } = require("vue-loader");
const { join } = require("path");
const { NODE_ENV } = process.env;

const webpackConfig = {
  mode: NODE_ENV,

  entry: {
    app: join(__dirname, "./src/main.js")
  },

  output: {
    path: join(__dirname, "./dist"),
    publicPath: "/dist/",
    filename: "build.js"
  },

  plugins: [new VueLoaderPlugin()],

  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["vue-style-loader", "css-loader"]
      },
      {
        test: /\.scss$/,
        use: ["vue-style-loader", "css-loader", "sass-loader"]
      },
      {
        test: /\.sass$/,
        use: ["vue-style-loader", "css-loader", "sass-loader?indentedSyntax"]
      },
      {
        test: /\.vue$/,
        loader: "vue-loader",
        options: {
          loaders: {
            // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
            // the "scss" and "sass" values for the lang attribute to the right configs here.
            // other preprocessors should work out of the box, no loader config like this necessary.
            scss: ["vue-style-loader", "css-loader", "sass-loader"],
            sass: [
              "vue-style-loader",
              "css-loader",
              "sass-loader?indentedSyntax"
            ]
          },
          // other vue-loader options go here
          postLoaders: { html: "babel-loader" },
          excludedPreLoaders: /(eslint-loader)/
        }
      },
      {
        test: /\.js$/,
        loader: "babel-loader",
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: "file-loader",
        options: {
          name: "[name].[ext]?[hash]"
        }
      }
    ]
  },

  resolve: {
    alias: {
      vue$: "vue/dist/vue.esm.js"
    },
    extensions: ["*", ".js", ".vue", ".json"]
  },

  performance: {
    hints: false
  }
};

// SECTION NPM run control

if (NODE_ENV === "development") {
  webpackConfig.devServer = {
    clientLogLevel: "warning",
    historyApiFallback: true,
    port: 9000,
    hot: true,
    open: true,
    // noInfo: true,
    overlay: true,
    quiet: true // necessary for FriendlyErrorsPlugin
  };

  webpackConfig.devtool = "#eval-source-map";

  webpackConfig.plugins = [
    ...webpackConfig.plugins,
    new HTMLWebpackPlugin({
      showErrors: true,
      cache: true,
      // title: "brandi test",
      templage: join(__dirname, "index.html")
    })
  ];
}

if (NODE_ENV === "production") {
  webpackConfig.devtool = "#source-map";

  webpackConfig.plugins = [
    ...webpackConfig.plugins,

    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ];
}

module.exports = webpackConfig;
