# Subdomain Enumeration Tool

A Python-based passive reconnaissance script for Red Team engagements.

## Why this matters?
During an engagement, the main website (e.g., `company.com`) might be heavily defended. However, subdomains like `dev.company.com` or `old-vpn.company.com` are often forgotten and vulnerable. Finding these expands the attack surface.

## How it works
This script queries **crt.sh**, a public Certificate Transparency log database. It is a purely passive technique, meaning it does not send any traffic to the target company's servers, keeping the initial recon stealthy.

## Usage
`python subdomain_enum.py <target_domain>`

*Disclaimer: Use only against domains you have permission to test.*
