
Write-Output "starting typescript in watch mode"
tsc frontend/src/main.ts --outdir frontend/dist/

Write-Output "starting server"
flask --app backend/app.py --debug run

