var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
   entry : {
       main: [
           path.join(__dirname, 'index.js')
       ]
   },

   output : {
       path: path.join(__dirname, '../static/build'),
           filename: 'bundle.js',
   },

    module: {
        rules: [
            {
                 test: /\.css$/,
                 use: [
                   'style-loader',
                   'css-loader'
                 ]
            },
            {
                test: /\.(sass|scss)$/,
                exclude: /(node_modules|bower_components)/,
                use: [
                'style-loader', 'css-loader', 'sass-loader'
                ]
            },
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new BundleTracker({ filename: '../static/webpack.stats.json' }),

        new webpack.DefinePlugin({
        'process.env': {
          NODE_ENV: JSON.stringify('development'),
          BASE_URL: JSON.stringify('http://0.0.0.0:8000/'),
        }
      })
    ]
};

// config.plugins = [
//     new webpack.HotModuleReplacementPlugin(),
//     new BundleTracker({ filename: '../backend/static/webpack.scss.json' }),
//     // new HtmlWebpackPlugin({
//     //   title: 'Hot Module Replacement'
//     // }),
//
//     new webpack.DefinePlugin({
//     'process.env': {
//       NODE_ENV: JSON.stringify('development'),
//       BASE_URL: JSON.stringify('http://0.0.0.0:8000/'),
//     }
//   })
// ];
