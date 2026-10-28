# AWS Cloud Ops Adventure — Web Preview

Browser frontend for [AWS_Cloud_Ops_Adventure_Android](https://github.com/seki999/AWS_Cloud_Ops_Adventure_Android).

**Status: early preview, not a complete port.** All 60 original mission JSON files are synchronized at build time. Only a subset of simulated commands and objective kinds are currently supported; Kotlin engine, full AWS CLI, IAM rules, scoring, topology drag and charts have not yet been ported. No real AWS connection or charges.

## Build

```sh
python scripts/sync_content.py
npm install
npm run dev
```

GitHub Pages: Settings > Pages > Build and deployment > Source > GitHub Actions. Then check Actions > Deploy Web preview to GitHub Pages.

Deployment is published from the `main` branch through GitHub Actions.
