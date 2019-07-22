#!/bin/bash

echo "开始时间:"$(date "+%Y-%m-%d %T")
mysql -ujindou -pjindou test < admin.sql
echo "结束时间:"$(date "+%Y-%m-%d %T")
