var path = require('path');
var webpack = require('webpack');
var axios = require('axios');
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
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
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
    ],
    resolve : {
        alias: {
            // bind version of jquery-ui
            "jquery-ui": "jquery-ui/jquery-ui.js",
            // bind to modules;
            modules: path.join(__dirname, "node_modules"),
        }
    }
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
