---
layout: default
title: 根目录文件展示
---

# 根目录文件列表

<ul>
  {% for file in site.static_files %}
    {% if file.path contains "/" %}
      <li><a href="{{ file.path }}">{{ file.name }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
