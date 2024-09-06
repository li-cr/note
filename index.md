---
layout: default
title: 文件目录
---

# 目录和文件列表

<ul>
  {% assign folders = site.static_files | where: "path", "/" %}
  {% for folder in folders %}
    <li>
      <a href="{{ folder.path }}">{{ folder.name }}</a>
      {% if folder.path contains "/" %}
        <ul>
          {% assign files = site.static_files | where: "path", folder.path %}
          {% for file in files %}
            <li><a href="{{ file.path }}">{{ file.name }}</a></li>
          {% endfor %}
        </ul>
      {% endif %}
    </li>
  {% endfor %}
</ul>
