#!/usr/bin/python
# -*- coding: utf-8 -*-

artisan_slider_style = """
            QSlider::groove:vertical {{
                background: #ddd;
                border: 0.5px solid #aaa;
                width: 3px;
                border-radius: 5px;
            }}
            QSlider::sub-page:vertical {{
                background: #ddd;
                border: 0.5px solid #aaa;
                width: 85px;
                border-radius: 5px;
            }}
            QSlider::add-page:vertical {{
                background: {color};
                border: 1px solid {color};
                width: 5px;
                border-radius: 2px;
            }}
            QSlider::handle:vertical {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #eee);
                border: 0.5px solid #ddd;
                height: 8px;
                margin-top: -1px;
                margin-bottom: -1px;
                margin-left: -10px;
                margin-right: -10px;
                border-radius: 5px;
            }}
            QSlider::handle:vertical:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            QSlider::sub-page:vertical:disabled {{
                background: #bbb;
                border-color: #999;
            }}
            QSlider::add-page:vertical:disabled {{
                background: #eee;
                border-color: #999;
            }}
            QSlider::handle:vertical:disabled {{
                background: #eee;
                border: 1px solid #aaa;
                border-radius: 5px;
            }}
"""
