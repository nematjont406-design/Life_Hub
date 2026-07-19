[33mcommit 540802c6b817e85d30774ff23e47f0415fe10611[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m)[m
Author: your GitHub username <nematjont406@gmail.com>
Date:   Sun Jul 19 14:25:36 2026 +0500

    Fix database migration error and improve deployment configuration
    
    - Fix context_processors.py to handle OperationalError when database is not ready
    - Update requirements.txt to support Django 6.x (changed from <5.0 to <7.0)
    - Add render.yaml for proper Render deployment configuration
    - Update build.sh to handle errors gracefully during admin user creation
    - Remove empty migration file 0005_fix_expense_description_null.py
    - Fix migration 0006 to depend on 0004 instead of non-existent 0005

 build.sh                                                    |  6 [32m+++[m[31m---[m
 config/context_processors.py                                |  9 [32m+++++++[m[31m--[m
 render.yaml                                                 | 11 [32m+++++++++++[m
 requirements.txt                                            |  2 [32m+[m[31m-[m
 users/migrations/0005_fix_expense_description_null.py       | 13 [31m-------------[m
 ...0006_alter_expense_description_alter_task_description.py |  2 [32m+[m[31m-[m
 6 files changed, 23 insertions(+), 20 deletions(-)
