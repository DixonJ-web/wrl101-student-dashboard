Set-Location -LiteralPath $PSScriptRoot
& "C:\Users\jaked\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m streamlit run app.py --server.port 8501 --server.headless true
