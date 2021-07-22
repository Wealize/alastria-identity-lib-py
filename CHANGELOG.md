## CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## v0.5.0

- Removed all the hardcoded services to make the code cleaner. This is a backwards incompatible change since
  the current methods to access smart contract functions weren't PEP8 standard, didn't comply with SRP nor DRY either. **IMPORTANT**: This makes the new library incompatible backwards, check the examples to see how to implement it.

## v0.4.0

- Fix presentations registry operations to use the correct smart contract address when delegated

## v0.3.0

- Fix credential registry operations to use the correct smart contract address when delegated

## v0.2.0

- Added CHANGELOG, homepage and url to pyproject file

## v0.1.0

- First version deployed on Pypi [url](https://pypi.org/manage/project/alastria-identity/release/0.1.0/).
