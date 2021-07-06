@echo off

set /p CommitDescription=Describe the changes: 

pause

set JEKYLL_ENV=production
call bundle exec jekyll build

call git add -A
call git commit -m "%CommitDescription%"
call git push

for /f %%i in ('git rev-parse HEAD') do set LastCommitId=%%i

call cd _site
call git add -A
call git commit -m "Deploy %LastCommitId%"
call git push

pause