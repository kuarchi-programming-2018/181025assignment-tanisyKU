# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:42:00 2018

@author: WATARU TANISHIMA
"""
from turtle import *  # 描画環境 turtle をインポート
from rose import *  # plot1.pyと同一フォルダにあるrose.pyをインポート
hideturtle()
rose_window_recursion(
    [[-300, -300], [300, -300], [300, 300], [-300, 300]], 0.01, 500)
done()  # turtleの終了処理