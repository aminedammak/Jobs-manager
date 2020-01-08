const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
        rules: [
         {
            test: /\.css$/,
            use: [
                MiniCssExtractPlugin.loader, 'css-loader'
            ]
        },
        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
              loader: "babel-loader"
            }
        }
    ]
  },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "styles.css"
        })
    ]
};