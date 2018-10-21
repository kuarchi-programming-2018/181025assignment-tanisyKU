# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 00:22:00 2018

@author: WATARU TANISHIMA
"""

import module1  # 作成したモジュール module1.pyの読み込み

file_name = 'data4.csv'  # ファイル名
x, y = module1.read_data(file_name)  # module1内の関数read_dataによりデータを取得
xmin, xmax, ymin, ymax = 0, 12, 0, 10  # 描画範囲
lc, ls, lw = 'yellow', '-', 5.0  # 描画オプション
title, xl, yl = 'LineGraph', 'X-Axis', 'Y-Axis'  # タイトル，ラベル
module1.draw_graph(x, y, xmin, xmax, ymin, ymax, lc,
                   ls, lw, title, xl, yl)  # module1内の
# 関数draw_graphによりグラフ描画