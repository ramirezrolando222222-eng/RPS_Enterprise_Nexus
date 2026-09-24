#!/bin/bash
set -euo pipefail

echo "🥷 Preparing Smart Ninja Cyber Defense for Enterprise Git Commit..."

cd smart-ninja-defense

# Create a LICENSE / Copyright attribution file
cat << 'EOT' > LICENSE
MIT License

Copyright (c) 2026 Rolando H Ramirez Jr (ramirezrolando242526@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy...
EOT

# Add a Header comment to the main backend file for attribution
sed -i '1i # Author: Rolando H Ramirez Jr <ramirezrolando242526@gmail.com>' backend/main.py

cd ..

# Stage and Commit
git add smart-ninja-defense/
git commit -m "Enterprise update: Smart Ninja Cyber Defense framework by Rolando H Ramirez Jr <ramirezrolando242526@gmail.com>"

# Push to origin
git push origin master || git push origin main

echo "✅ Smart Ninja framework successfully pushed to GitHub, Chief!"
