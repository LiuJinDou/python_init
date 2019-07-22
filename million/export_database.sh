#!/bin/bash

echo "开始时间:"$(date "+%Y-%m-%d %T")
mysqldump -ujindou -pjindou test > admin_database.sql
echo "结束时间:"$(date "+%Y-%m-%d %T")
