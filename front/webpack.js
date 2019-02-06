var path = require('path');
var webpack = require('webpack');

module.exports = {
   entry : {
       main: [
           path.join(__dirname, 'src/style.scss')
       ]
   },

   output : {
       path: path.join(__dirname, 'src/build'),
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
};
