# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- API endpoint at api.archignes.com/systems for accessing system information
- Initial Release.

## [0.1.0] - 2024-03-25

### Added

- a copy of the AWS Lambda function: serveSearchSystems.py
- Documentation of the purpose, API (including current status with badges), and repository in README.md
- CHANGELOG.md
- systems.json
- schema.json
- validate.js
- [Husky](https://typicode.github.io/husky/) pre-commit hook to run the validation (with [Ajv](https://ajv.js.org/)) and, with [lint-staged](https://github.com/lint-staged/lint-staged), [Prettier](https://prettier.io/) formatting
- GitHub actions to sync systems.json here with the one in AWS
- AWS setup: S3 bucket, Lambda function, API Gateway

## [0.0.1] - 2024-03-24

### Added

- this git repository
- MIT License
