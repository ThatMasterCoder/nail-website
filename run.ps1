
Write-Output "starting typescript in watch mode"
# tsc frontend/src/main.ts --outdir frontend/dist/
tsc 

Write-Output "starting server"
flask --app backend/app.py --debug run

