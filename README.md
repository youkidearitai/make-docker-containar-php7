# PHP7 on tekitoh-memdhoi.info

PHP7のビルドに使ってるDockerfileです。デプロイ時のFabricのfabfileもあります。

[My site tekitoh-memdhoi.info](http://tekitoh-memdhoi.info)

## How to work

以下のコマンドでPHP7のバージョンアップができるようにしてあります。

    $ sudo docker build -t youkidearitai/php7-tmcmaker .
    $ fab deploy

当然、サーバー側にもDockerfileがあって、それによって本番用のコンテナになります。

## 自前で用意するもの

+ confディレクトリ配下のもの。
+ ssh\_config

ぼくのサーバーの大事な部分は見せられないので頑張ってください（？）。

## LICENSE

The MIT License.

    The MIT License (MIT)
    
    Copyright (c) <2016> <tekimen>
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

